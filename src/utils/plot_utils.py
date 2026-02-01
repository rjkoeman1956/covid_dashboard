import geopandas as gpd
import matplotlib.pyplot as plt


def plot_geodataframe(gdf: gpd.GeoDataFrame, column: str, ax=None, cmap="YlOrRd", edgecolor="black"):
    """
    Plot een GeoDataFrame met heatmapstijl.
    - gdf: GeoDataFrame met geometrie en kolom
    - column: te visualiseren kolom
    - ax: optionele matplotlib-as
    - cmap: colormap
    - edgecolor: kleur van grenzen
    """
    if ax is None:
        fig, gdf = plot_riool_heatmap(year=2024, region="Municipalities", metric="RNA flow per 100k", debug=True)
        # fig, ax = plt.subplots(figsize=(10, 10))

    gdf.plot(
        column=column,
        ax=ax,
        legend=True,
        cmap=cmap,
        edgecolor=edgecolor,
        linewidth=0.5,
        missing_kwds={"color": "lightgrey", "label": "No data"},
    )

    ax.set_title(f"{column} (heatmap)", fontsize=13)
    ax.axis("off")

    return ax
