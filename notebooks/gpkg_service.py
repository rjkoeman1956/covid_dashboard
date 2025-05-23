from pathlib import Path
import geopandas as gpd
import fiona

def list_gpkg_files(directory: Path) -> list:
    return list(directory.glob("*.gpkg"))

def list_gpkg_layers(gpkg_path: Path) -> list:
    return fiona.listlayers(str(gpkg_path))

def load_gpkg_layer(gpkg_path: Path, layer_name: str) -> gpd.GeoDataFrame:
    return gpd.read_file(gpkg_path, layer=layer_name)
