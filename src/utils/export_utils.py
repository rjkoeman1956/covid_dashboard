# src/utils/export_utils.py
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, Optional, Any

import pandas as pd
import ipywidgets as widgets
from IPython.display import clear_output

from config import EXPORTS_DIR, LOG_FILE


EXPORTS_DIR = Path(EXPORTS_DIR)
LOG_FILE = Path(LOG_FILE)
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def _ts() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _safe_name(name: str) -> str:
    name = name.strip().replace(" ", "_")
    name = re.sub(r"[^A-Za-z0-9_\-]+", "", name)
    return name or "export"


def _is_geodataframe(df: Any) -> bool:
    return hasattr(df, "geometry") and "geometry" in getattr(df, "columns", [])


def _normalize_df_for_export(
    df: Any,
    *,
    include_geometry: bool = False,
    geometry_as_wkt: bool = False
) -> pd.DataFrame:
    if df is None:
        return pd.DataFrame()

    try:
        df2 = df.copy()
    except Exception:
        df2 = pd.DataFrame(df)

    if _is_geodataframe(df2):
        if include_geometry and geometry_as_wkt:
            try:
                df2["geometry"] = df2["geometry"].apply(lambda g: g.wkt if g is not None else None)
            except Exception:
                df2 = df2.drop(columns=["geometry"], errors="ignore")
        elif not include_geometry:
            df2 = df2.drop(columns=["geometry"], errors="ignore")

    # stringify "weird" objects
    for c in df2.columns:
        if df2[c].dtype == "object":
            sample = df2[c].dropna().head(3).tolist()
            if any(isinstance(x, (dict, list, set, tuple)) for x in sample):
                df2[c] = df2[c].apply(
                    lambda x: json.dumps(x, ensure_ascii=False)
                    if isinstance(x, (dict, list, set, tuple)) else x
                )
    return df2


def _append_log_row(row: Dict[str, Any]) -> None:
    fieldnames = ["timestamp", "label", "action", "format", "scope", "filepath", "rows", "cols", "meta"]

    row2 = dict(row)
    if "meta" in row2 and not isinstance(row2["meta"], str):
        row2["meta"] = json.dumps(row2["meta"], ensure_ascii=False)

    new_file = not LOG_FILE.exists()
    with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if new_file:
            w.writeheader()
        w.writerow({k: row2.get(k, "") for k in fieldnames})


def _export_markdown(df: pd.DataFrame, filepath: Path, title: str, meta: Dict[str, Any]) -> None:
    lines = [f"# {title}", "", f"Timestamp: {_ts()}", ""]
    if meta:
        lines.append("## Filters / Meta")
        for k, v in meta.items():
            lines.append(f"- **{k}**: {v}")
        lines.append("")
    lines.append("## Data")
    lines.append(df.to_markdown(index=False))
    filepath.write_text("\n".join(lines), encoding="utf-8")


def _export_pdf(df: pd.DataFrame, filepath: Path, title: str, meta: Dict[str, Any]) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        str(filepath),
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title=title,
    )

    story = []
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"Timestamp: {_ts()}", styles["Normal"]))
    story.append(Spacer(1, 10))

    if meta:
        story.append(Paragraph("Filters / Meta", styles["Heading2"]))
        for k, v in meta.items():
            if k == "plot_path":
                continue
            story.append(Paragraph(f"<b>{k}</b>: {v}", styles["Normal"]))
        story.append(Spacer(1, 10))

    # Table (cap rows for PDF sanity)
    df_pdf = df.copy()
    if len(df_pdf) > 40:
        df_pdf = df_pdf.head(40)

    if not df_pdf.empty:
        table_data = [list(df_pdf.columns)] + df_pdf.astype(str).values.tolist()
        t = Table(table_data, repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        story.append(Paragraph("Data", styles["Heading2"]))
        story.append(t)
        story.append(Spacer(1, 12))

    # Optional plot
    plot_path = meta.get("plot_path")
    if plot_path:
        p = Path(plot_path)
        if p.exists():
            story.append(Paragraph("Plot", styles["Heading2"]))
            story.append(Spacer(1, 6))

            max_width = A4[0] - (doc.leftMargin + doc.rightMargin)
            img = Image(str(p))
            # Keep aspect ratio; scale to page width
            scale = max_width / float(img.imageWidth) if img.imageWidth else 1.0
            img.drawWidth = img.imageWidth * scale
            img.drawHeight = img.imageHeight * scale

            story.append(img)

    doc.build(story)


def export_dataframe(
    df: Any,
    *,
    fmt: str,
    label: str,
    scope: str,
    meta: Optional[Dict[str, Any]] = None,
    include_geometry: bool = False,
    geometry_as_wkt: bool = False,
) -> Path:
    meta = meta or {}
    df2 = _normalize_df_for_export(df, include_geometry=include_geometry, geometry_as_wkt=geometry_as_wkt)

    filename = f"{_safe_name(label)}_{scope}_{_ts()}.{fmt}"
    filepath = EXPORTS_DIR / filename

    if fmt == "csv":
        df2.to_csv(filepath, index=False)
    elif fmt == "md":
        _export_markdown(df2, filepath, title=label, meta=meta)
    elif fmt == "pdf":
        _export_pdf(df2, filepath, title=label, meta=meta)
    else:
        raise ValueError(f"Unsupported format: {fmt}")

    _append_log_row({
        "timestamp": _ts(),
        "label": label,
        "action": "export",
        "format": fmt,
        "scope": scope,
        "filepath": str(filepath),
        "rows": int(getattr(df2, "shape", (0, 0))[0]),
        "cols": int(getattr(df2, "shape", (0, 0))[1]),
        "meta": meta,
    })
    return filepath


def create_export_widget(
    *,
    get_small: Callable[[], Any],
    get_full: Callable[[], Any],
    get_meta: Callable[[], Dict[str, Any]],
    label: str,
    width: str = "300px",
    get_plot_png: Optional[Callable[[], Optional[str]]] = None,
) -> widgets.VBox:
    dd = widgets.Dropdown(
        options=[
            ("Small CSV", "csv_small"),
            ("Full CSV", "csv_full"),
            ("Markdown (small)", "md_small"),
            ("PDF (small + plot)", "pdf_small"),
        ],
        description="Export:",
        layout=widgets.Layout(width=width),
    )
    btn = widgets.Button(description="Go", layout=widgets.Layout(width="70px"))
    out = widgets.Output()

    def _run_export(_):
        with out:
            clear_output(wait=True)
            choice = dd.value
            meta = dict(get_meta() or {})

            # On-demand plot render (scenario 2)
            if choice == "pdf_small" and get_plot_png is not None:
                try:
                    plot_path = get_plot_png()
                    if plot_path:
                        meta["plot_path"] = plot_path
                except Exception as e:
                    print(f"⚠️ Plot render faalde: {e}")

            if choice == "csv_small":
                df = get_small()
                p = export_dataframe(df, fmt="csv", label=label, scope="small", meta=meta)
            elif choice == "csv_full":
                df = get_full()
                p = export_dataframe(df, fmt="csv", label=label, scope="full", meta=meta)
            elif choice == "md_small":
                df = get_small()
                p = export_dataframe(df, fmt="md", label=label, scope="small", meta=meta)
            elif choice == "pdf_small":
                df = get_small()
                p = export_dataframe(df, fmt="pdf", label=label, scope="small", meta=meta)
            else:
                print("⚠️ Maak een keuze.")
                return

            print(f"✅ Export: {p}")

    btn.on_click(_run_export)

    return widgets.VBox([widgets.HBox([dd, btn]), out])
