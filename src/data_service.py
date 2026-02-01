import os, sys
from pathlib import Path

project_root = Path.cwd()
while not (project_root / 'config.py').exists() and project_root != project_root.parent:
    project_root = project_root.parent
sys.path.insert(0, project_root.as_posix())

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from data_loader import read_csv_safe, Dataframes, load_municipality_shapefile
from dataframe_combiner import combine_dataframes
from dataframe_cleaner import clean_dataframe_aantallen_gemeente, clean_dataframe_ziekenhuisopnames
from config import SRC_DIR, CSV_DIR, PROV_SHAPEFILE, MUN_SHAPEFILE, RWZI_FILE, RNA_FILE, SHAPEFILES_DIR, EXPORTS_DIR, UTILS_DIR, PROV_FILE, GEM_PROV_FILE

from src.utils.mapping_utils import (
    get_metric_mapping_tab1,
    get_metric_mapping_tab2,
    get_metric_mapping_tab3
)

# Centrale COVID-19 Dataset
def get_prepared_covid_dataset() -> pd.DataFrame:
    dataframes = Dataframes()
    clean_dataframe_aantallen_gemeente(dataframes)
    clean_dataframe_ziekenhuisopnames(dataframes)

    merged_df = combine_dataframes(dataframes)

    # Extra kolommen: Year, Month, *_merged
    merged_df["Year"] = pd.to_datetime(merged_df["Date_of_publication"], errors="coerce", dayfirst=False).dt.year.astype("Int64")
    merged_df["Month"] = pd.to_datetime(merged_df["Date_of_publication"], errors="coerce", dayfirst=False).dt.month
    merged_df["Province_merged"] = merged_df["Province"]
    merged_df["Municipality_name_merged"] = merged_df["Municipality_name"]    

    # print("Columns after combine_dataframes():")
    # print(merged_df.columns.tolist())

    dataframes.set_merged_and_clean_dataset(merged_df)
    return merged_df

# Heatmap data: Provinces (Tab2)
def get_province_heatmap_data(year, column):
    from data_loader import Dataframes, load_province_shapefile
    from dataframe_combiner import combine_dataframes
    from dataframe_cleaner import clean_dataframe_aantallen_gemeente, clean_dataframe_ziekenhuisopnames, add_year_and_month_columns
    import pandas as pd

    # 1. Instantieer de data
    dfs = Dataframes()

    # 2. Reinig de brondata
    clean_dataframe_aantallen_gemeente(dfs)
    clean_dataframe_ziekenhuisopnames(dfs)

    # 3. Combineer tot samengevoegd dataframe
    df_combined = combine_dataframes(dfs)

    # 4. Voeg kolommen 'Year' en 'Month' toe
    df_combined = add_year_and_month_columns(df_combined)

    # 5. Merge kolommen (Province_merged etc.)
    df_combined["Province_merged"] = df_combined["Province"].combine_first(df_combined.get("Province_y"))
    df_combined["Municipality_name_merged"] = df_combined["Municipality_name"].combine_first(df_combined.get("Municipality_name_x"))

    # 6. Filter op jaar
    df = df_combined[df_combined["Year"] == int(year)]

    # 7. Groepeer per provincie
    df_grouped = df.groupby("Province_merged", as_index=False)[column].sum(numeric_only=True)

    # 8. Lees geopandas shapefile
    gdf = load_province_shapefile()

    # 9. Merge GeoDataFrame met data
    gdf = gdf.merge(df_grouped, left_on="NAAM", right_on="Province_merged", how="left")

    return gdf  

    
# Heatmap data: Municipalities (Tab3)
def get_municipality_heatmap_data(year, column):
    """
    Haalt een GeoDataFrame op met COVID-data per gemeente,
    en filtert 'Water == Ja' eruit vóór de merge.
    """
    from data_loader import load_municipality_shapefile
    from data_service import get_prepared_covid_dataset

    df = get_prepared_covid_dataset()
    df_filtered = df[df['Year'] == int(year)]
    df_grouped = df_filtered.groupby('Municipality_name_merged', as_index=False).agg({column: 'sum'})

    gdf = load_municipality_shapefile()

    # Filter: geen waterpolygonen meenemen
    if "water" in gdf.columns:
        gdf = gdf[~gdf["water"].str.strip().str.upper().eq("JA")]

    gdf = gdf.rename(columns={'gemeentenaam': 'Municipality_name_merged'})  # indien nog niet gestandaardiseerd
    gdf_merged = gdf.merge(df_grouped, on='Municipality_name_merged', how='left')

    return gdf_merged



# Placeholder voor Tab3 Riooldata
def get_prepared_riool_dataset() -> pd.DataFrame:
    try:
        return pd.read_csv(CSV_DIR / RNA_FILE, sep=";")
    except FileNotFoundError:
        return pd.DataFrame()
        
        
def get_gem_prov() -> pd.DataFrame:
    try:
        return pd.read_csv(CSV_DIR / GEM_PROV_FILE, sep=";")
    except FileNotFoundError:
        return pd.DataFrame()


def get_municipality_share_rwzi_dataset() -> pd.DataFrame:
    try:
        return pd.read_csv(CSV_DIR / RWZI_FILE, sep=";")
    except FileNotFoundError:
        return pd.DataFrame()

# Converteer MUN_SHARE naar float
def clean_mun_share_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Zet kolom 'MUN_SHARE' van percentage met komma (bv. '67,5%') naar decimaal (bv. 0.675)
    """
    df = df.copy()
    df["MUN_SHARE"] = (
        df["MUN_SHARE"]
        .astype(str)
        .str.strip()
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)  
        .astype(float) / 100.0
    )
    return df

 
def get_riool_heatmap_data(year, region, column):
    """
    Laadt en combineert rioolwaterdata, aandeel per gemeente, en geometrie
    om een heatmap op gemeentelijk of provinciaal niveau te maken.
    """
    # --- 1. CSV-bestanden veilig inlezen ---
    df_rna = pd.read_csv(CSV_DIR / RNA_FILE, sep=';')
    df_share = pd.read_csv(CSV_DIR / RWZI_FILE, sep=';')

    # --- 2. Validatie ---
    if df_rna.empty or df_share.empty:
        print("⚠️ Eén van de datasets is leeg of kon niet worden gelezen.")
        return gpd.GeoDataFrame()
    
    # --- 3. Filter en aggregeer riooldata ---
    df_share = clean_mun_share_column(df_share)
    df_rna["RWZI_AWZI_code"] = df_rna["RWZI_AWZI_code"].astype(str)
    df_rna["Date_measurement"] = pd.to_datetime(df_rna["Date_measurement"], errors='coerce')
    df_rna["Year"] = df_rna["Date_measurement"].dt.year

    # --- 4. Join datasets op RWZI-code
    df = df_rna.merge(df_share, left_on="RWZI_AWZI_code", right_on="RWZI_CODE", how="inner")

    # --- 5. Filter op jaar (geen filter op 'water', die kolom bestaat hier niet)
    df = df[df["Year"] == int(year)]

    return df


# Sewer Heatmap data: Provincie (Tab3)
def get_province_riool_heatmap_data(year, region, column):
    """
    Combineert rioolwaterdata met provinciegrenzen
    voor de provinciale heatmap in Tab3.
    """
    from data_loader import load_province_shapefile

    # --- 1. CSV-bestanden veilig inlezen ---
    df = get_riool_heatmap_data(year, region, column)
    df_prov = get_gem_prov()

    # --- 2. Validatie ---
    if df_prov.empty:
        print("⚠️ Eén van de datasets is leeg of kon niet worden gelezen.")
        return gpd.GeoDataFrame()

    # --- 3. Filter en aggregeer riooldata ---
    df_prov.loc[df_prov['Provincienaam'] == 'Friesland', 'Provincienaam'] = 'Fryslân'
    df = df.rename(columns={'RWZI_AWZI_name': 'Gemeentenaam'})
    merged_df = pd.merge(df, df_prov, on='Gemeentenaam', how='inner')

    # --- 4. Lees geopandas shapefile
    gdf = load_province_shapefile()

    # --- 5. Merge GeoDataFrame met data
    df_grouped = merged_df.groupby('Provincienaam')[['RNA_flow_per_100000']].sum().reset_index()
    gdf = gdf.rename(columns={'NAAM': 'Provincienaam'})
    gdf = gdf.merge(df_grouped, on='Provincienaam', how='left')
       
    return gdf


# Sewer Heatmap data: Municipalities (Tab3)
def get_municipality_riool_heatmap_data(year, region, column):
    """
    Combineert rioolwaterdata met RWZI-verdeling en gemeentelijke grenzen
    voor de gemeentelijke heatmap in Tab3.
    """
   # --- 1. CSV-bestanden veilig inlezen ---
    df = get_riool_heatmap_data(year, region, column)

    # --- 2. Gewicht berekenen
    df["Weighted"] = df["RNA_flow_per_100000"] * df["MUN_SHARE"]

    # --- 3. Aggregatie per gemeente
    df_agg = df.groupby("MUN_CODE").agg({
        "Weighted": "sum",
        "MUN_NAME": "first"
    }).reset_index()

    df_agg["RNA_flow_per_100000"] = df_agg["Weighted"]

    # --- 4. Laad geometrie van gemeenten – expliciet juiste layer
    gdf = gpd.read_file(MUN_SHAPEFILE, layer="gemeenten")

    # --- 5. Merge GeoDataFrame met data
    gdf["gemeentecode"] = gdf["gemeentecode"].astype(str)
    gdf = gdf.merge(df_agg, left_on="gemeentecode", right_on="MUN_CODE", how="left")
        
    return gdf       


# Bepaal de jaartallen in een dataframe
def get_available_years(df, prefer_year="2020"):
    """
    Retourneert een lijst van geldige jaartallen (als int) en een default jaar.
    """
    # Zorg dat Year als integer wordt geïnterpreteerd
    df["Year"] = pd.to_datetime(df["Date_of_publication"], errors="coerce", dayfirst=False).dt.year
    df["Year"] = df["Year"].astype("Int64")

    available_years = sorted(df["Year"].dropna().unique().tolist())
    
    if not available_years:
        raise ValueError("❌ Geen geldige jaartallen gevonden in dataset.")

    default_year = int(prefer_year) if int(prefer_year) in available_years else available_years[0]
    return available_years, default_year