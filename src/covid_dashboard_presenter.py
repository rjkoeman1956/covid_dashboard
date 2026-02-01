import sys
import warnings
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from config import SRC_DIR, CSV_DIR, PROV_SHAPEFILE, MUN_SHAPEFILE, RWZI_FILE, RNA_FILE, SHAPEFILES_DIR, EXPORTS_DIR, UTILS_DIR
from src.utils.mapping_utils import (
    get_metric_mapping_tab1,
    get_metric_mapping_tab2,
    get_metric_mapping_tab3
)
from src.utils.plot_utils import plot_geodataframe 


# Tab 1 – COVID Bar Chart per provincie/gemeente
def plot_covid(df, year, total_reported, hospital_admission, deceased, province, municipalities, months):
    warnings.filterwarnings("ignore", message=".*user_version=.*", category=RuntimeWarning)

    if df.empty:
        print("⚠️ No data available for plot.")
        return

    # Filter op jaar en provincie
    df_filtered = df[df['Year'] == int(year)]
    if province != "Netherlands":
        df_filtered = df_filtered[df_filtered['Province_merged'] == province]

    if df_filtered.empty:
        print("⚠️ No data after filtering.")
        return

    # Selecteer kolommen
    selected_cols = []
    metric_colors = {}
    column_labels = {
        "Total_reported": "Total reported",
        "Hospital_admission": "Hospital admissions",
        "Deceased": "Deceased"
    }

    if total_reported:
        selected_cols.append("Total_reported")
        # metric_colors["Total_reported"] = "#1f77b4"
        metric_colors["Total_reported"] = "#FDDDB0"
    if hospital_admission:
        selected_cols.append("Hospital_admission")
        # metric_colors["Hospital_admission"] = "#ff7f0e"
        metric_colors["Hospital_admission"] = "#FA8757"

    if deceased:
        selected_cols.append("Deceased")   # gebruik bestaande naam voor label
        metric_colors["Deceased"] = "#870200"

        # Filter op echte dagwaarden
        df_filtered = df_filtered[df_filtered["Deceased"] > 0]

    if not selected_cols:
        print("⚠️ Geen metrics geselecteerd.")
        return

    # Aggregatie op basis van context
    if municipalities:
        if 'Municipality_name_merged' not in df_filtered.columns:
            print("❌ Kolom 'Municipality_name_merged' ontbreekt.")
            return
        group_col = "Municipality_name_merged"
        x_label = "Municipalities"
    elif months:
        if 'Month' not in df_filtered.columns:
            print("❌ Kolom 'Month' ontbreekt.")
            return
        group_col = "Month"
        x_label = "Months"
    else:
        group_col = "Province_merged"
        x_label = "Provinces"

    df_grouped = df_filtered.groupby(group_col)[selected_cols].sum().reset_index()
    if df_grouped.empty:
        print("⚠️ Geen gegroepeerde data.")
        return

    # Vertaal maandnummer → maandnaam
    if group_col == "Month":
        maand_namen = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df_grouped['Month'] = df_grouped['Month'].astype(int).apply(lambda x: maand_namen[x - 1])

    try:
        # Gebruik nette labels
        df_grouped = df_grouped.rename(columns=column_labels)

        # Maak kleurenlijst in juiste volgorde
        kleuren = [metric_colors[col] for col in selected_cols]

        # Vertaal kolomnamen → labels (ook als er rename is gedaan)
        plot_cols = [column_labels.get(col, col) for col in selected_cols]

        ax = df_grouped.set_index(group_col)[plot_cols].plot(
            kind='bar', figsize=(11, 5), color=kleuren
        )
        ax.set_title(f"COVID Metrics – {province} ({year})")
        ax.set_xlabel(x_label)
        ax.set_ylabel("Number")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Fout bij het plotten: {e}")


# Tab 2 – COVID Heatmap per provincie/gemeente
def plot_heatmap(gdf, column, title, cmap='OrRd', legend=True, edgecolor='0.8', figsize=(10, 10), dpi=300, save_as=None, arrow_position='bottomright', scale_max=None):
    """
    Plot heatmap met noordpijl en opslagoptie.

    Parameters:
    - gdf (GeoDataFrame): De geodata.
    - column (str): De kolom waarop de kleur gebaseerd wordt.
    - title (str): De titel van de kaart.
    - cmap (str): Kleurenkaart (default: 'OrRd').
    - legend (bool): Toon legenda (default: True).
    - edgecolor (str): Randkleur polygons (default: '0.8').
    - figsize (tuple): Grootte van de figuur (default: (10, 8)).
    - dpi (int): Resolutie voor opslag (default: 300).
    - save_as (str or None): Bestandsnaam om op te slaan (bv. 'kaart.png') of None om alleen te tonen.
    - arrow_position (str): Locatie van noordpijl ('topleft', 'topright', 'bottomleft', 'bottomright').

    Returns:
    - matplotlib.axes.Axes: De gegenereerde plot.
    """
    fig, ax = plt.subplots(figsize=figsize)
    # Bepaal de bovenwaarde van de schaal (vmax): neem scale_max als die is meegegeven, anders dataset-max
    vmax_value = float(scale_max) if scale_max is not None else float(gdf[column].max())
    gdf.plot(
        column=column,
        cmap=cmap,
        edgecolor=edgecolor,
        linewidth=0.5,
        legend=legend,
        vmin=0,
        # vmax=gdf[column].max(),
        vmax=vmax_value,
        legend_kwds={'label': column.replace('_', ' '), 'orientation': 'vertical'},
        missing_kwds={"color": "lightgrey", "label": "No data"},
        ax=ax
    )

    # Kop titel heatmap
    ax.set_title(
        title, 
        fontsize=12, 
        fontweight='normal', 
        color='black')
    ax.set_axis_off()

    # Voet titel met jaartal, indien aanwezig in gdf of via extra argument
    if "year_label" in gdf.attrs:
        ax.text(0.5, -0.07, f"Year: {gdf.attrs['year_label']}",
                ha="center", va="top", transform=ax.transAxes, fontsize=10, color="dimgrey")
    
    # Toon de bovengrens (vmax) boven de schaal, gecentreerd
    try:
        cbar_ax = next(a for a in fig.axes if a is not ax)
        # Voeg enkel verticale spacer toe zodat Tab2 en Tab3 dezelfde hoogte hebben
        cbar_ax.text(0.5, 1.02, " ", ha="center", va="bottom",
                     transform=cbar_ax.transAxes, fontsize=9, color=(1,1,1,0))
        fig.subplots_adjust(top=0.96)        
    except StopIteration:
        pass  # geen colorbar gevonden (legend=False?), dan doen we niets
   
    # Noordpijl
    pos_dict = {
        'topleft': (0.1, 0.9),
        'topright': (0.9, 0.9),
        'bottomleft': (0.1, 0.1),
        'bottomright': (0.9, 0.1)
    }
    x, y = pos_dict.get(arrow_position, (0.9, 0.1))
    arrowlength = 0.08
    angle = 90
    dx = arrowlength * np.cos(np.radians(angle))
    dy = arrowlength * np.sin(np.radians(angle))

    # Noordletter 'N'
    ax.annotate('N', xy=(x, y), xytext=(x - dx, y - dy),
                arrowprops=dict(facecolor='black', width=5, headwidth=15),
                ha='center', va='center', fontsize=16,
                xycoords=ax.transAxes)

    # Save parameters
    if save_as:
        plt.savefig(save_as, dpi=dpi, bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()
    return ax

# Tab2 wrappers: laat save_as/dpi door naar plot_heatmap

# Plot Province heatmap voor Tab 2
def plot_province_heatmap(gdf, column, title="Provinces heatmap", save_as=None, dpi=150, **kwargs):
    return plot_heatmap(gdf, column=column, title=title, save_as=save_as, dpi=dpi, **kwargs)
# def plot_province_heatmap(gdf, column):
#     plot_heatmap(gdf, column=column, title="Provinces RIVM Covid-19")

# Plot Municipality heatmap voor Tab 2
def plot_municipality_heatmap(gdf, column, title="Municipalities heatmap", save_as=None, dpi=150, **kwargs):
    return plot_heatmap(gdf, column=column, title=title, save_as=save_as, dpi=dpi, **kwargs)
# def plot_municipality_heatmap(gdf, column):
#     plot_heatmap(gdf, column=column, title="Municipalities RIVM Covid-19")










# Plot Sewer Heatmap per provincie/gemeente voor Tab 3
def plot_riool_heatmap(gdf, region, column, title, cmap='OrRd', legend=True, edgecolor='0.8', figsize=(10, 10), dpi=300, save_as=None, arrow_position='bottomright', scale_max=None):
    """
    Plot heatmap met noordpijl en opslagoptie.

    Parameters:
    - gdf (GeoDataFrame): De geodata.
    - column (str): De kolom waarop de kleur gebaseerd wordt.
    - title (str): De titel van de kaart.
    - cmap (str): Kleurenkaart (default: 'OrRd').
    - legend (bool): Toon legenda (default: True).
    - edgecolor (str): Randkleur polygons (default: '0.8').
    - figsize (tuple): Grootte van de figuur (default: (10, 8)).
    - dpi (int): Resolutie voor opslag (default: 300).
    - save_as (str or None): Bestandsnaam om op te slaan (bv. 'kaart.png') of None om alleen te tonen.
    - arrow_position (str): Locatie van noordpijl ('topleft', 'topright', 'bottomleft', 'bottomright').

    Returns:
    - matplotlib.axes.Axes: De gegenereerde plot.
    """

    fig, ax = plt.subplots(figsize=figsize)
    # Bepaal de bovenwaarde van de schaal (vmax): neem scale_max als die is meegegeven, anders dataset-max
    vmax_value = float(scale_max) if scale_max is not None else float(gdf[column].max())

    gdf.plot(
        column=column,
        cmap=cmap,
        edgecolor=edgecolor,
        linewidth=0.5,
        legend=legend,
        vmin=0,
        vmax=vmax_value,
        legend_kwds={'label': column.replace('_', ' '), 'orientation': 'vertical'},
        missing_kwds={"color": "lightgrey", "label": "No data"},
        ax=ax
    )

    # Titel heatmap
    ax.set_title(
        title, 
        fontsize=12, 
        fontweight='normal', 
        color='black')
    ax.set_axis_off()

    # Voet titel met jaartal, indien aanwezig in gdf of via extra argument
    if "year_label" in gdf.attrs:
        ax.text(0.5, -0.07, f"Year: {gdf.attrs['year_label']}",
                ha="center", va="top", transform=ax.transAxes, fontsize=10, color="dimgrey")
    
    # Toon de bovengrens (vmax) boven de schaal, gecentreerd
    try:
        cbar_ax = next(a for a in fig.axes if a is not ax)
        # Voeg enkel verticale spacer toe zodat Tab2 en Tab3 dezelfde hoogte hebben
        cbar_ax.text(0.5, 1.02, " ", ha="center", va="bottom",
                     transform=cbar_ax.transAxes, fontsize=9, color=(1,1,1,0))
        fig.subplots_adjust(top=0.96)        
    except StopIteration:
        pass  # geen colorbar gevonden (legend=False?), dan doen we niets

    
    # Noordpijl
    pos_dict = {
        'topleft': (0.1, 0.9),
        'topright': (0.9, 0.9),
        'bottomleft': (0.1, 0.1),
        'bottomright': (0.9, 0.1)
    }
    x, y = pos_dict.get(arrow_position, (0.9, 0.1))
    arrowlength = 0.08
    angle = 90
    dx = arrowlength * np.cos(np.radians(angle))
    dy = arrowlength * np.sin(np.radians(angle))

    # Noordletter 'N'
    ax.annotate('N', xy=(x, y), xytext=(x - dx, y - dy),
                arrowprops=dict(facecolor='black', width=5, headwidth=15),
                ha='center', va='center', fontsize=16,
                xycoords=ax.transAxes)

    # Save parameters
    if save_as:
        plt.savefig(save_as, dpi=dpi, bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()
    return ax

# Tab3 wrappers: laat save_as/dpi door naar plot_heatmap

# Plot provincie heatmap voor Tab 3
def plot_province_heatmap_riool(gdf, region, column, title="Provinces RWZI RNA-flow", save_as=None, dpi=150, **kwargs):
    return plot_riool_heatmap(gdf, region=region, column=column, title=title, save_as=save_as, dpi=dpi, **kwargs)
# def plot_province_heatmap_riool(gdf, region, column):
#     plot_riool_heatmap(gdf, region="Municipalities", column="RNA_flow_per_100000", title="Provinces RWZI RNA-flow")

# Plot Municipality heatmap voor Tab 3
def plot_municipality_heatmap_riool(gdf, region, column, title="Municipalities RWZI RNA-flow", save_as=None, dpi=150, **kwargs):
    return plot_riool_heatmap(gdf, region=region, column=column, title=title, save_as=save_as, dpi=dpi, **kwargs)
# def plot_municipality_heatmap_riool(gdf, region, column):
#     plot_riool_heatmap(gdf, region, column=column, title="Municipalities RWZI RNA-flow")
