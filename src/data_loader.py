from pathlib import Path
from config import CSV_DIR, COVID_MUN1_FILE, COVID_MUN2_FILE, COVID_HOS1_FILE, COVID_HOS2_FILE, RWZI_FILE, RNA_FILE, MUN_SHAPEFILE, PROV_SHAPEFILE

import urllib.request
import pandas as pd
import geopandas as gpd

def read_csv_safe(path, sep=';', encodings=('utf-8', 'latin1', 'cp1252')):
    """
    Leest een CSV-bestand met meerdere encoding-fallbacks en tolerante parser.
    Toont foutmeldingen direct in de notebook-output bij problemen.
    """
    for enc in encodings:
        try:
            df = pd.read_csv(path, sep=sep, encoding=enc, engine='python', on_bad_lines='skip')
            print(f"✅ Loaded {path.name} ({len(df)} rows, encoding={enc})")
            return df
        except (UnicodeDecodeError, pd.errors.ParserError) as e:
            print(f"⚠️ Encoding/parse error with {enc}: {e}")
            continue
        except Exception as e:
            print(f"⚠️ General read error for {path.name}: {e}")
            continue
    print(f"❌ Failed to read {path.name} with encodings {encodings}")
    return pd.DataFrame()


# Class lees de Covid data uit de CSV files, voor Tab1
class Dataframes:
    def __init__(self):
        """
        Leest de aantallen Covid-13 meldingen en ziekenhuisopnames voor een gemeenschappelijke datum reeks tussen 2020 en 2025.
        Vervolgens worden de twee datasets samengevoegd tot één schone nieuwe dataset voor de datumreeks. 
        """
        # Covid-13 ziekenhuis meldingen per gemeente per per dag
        file1 = COVID_MUN1_FILE
        file2 = COVID_MUN2_FILE
        # Covid-13 ziekenhuis opnames per gemeente per per dag
        file3 = COVID_HOS1_FILE
        file4 = COVID_HOS2_FILE
        
        try:
            self.aantallen_gemeente_df1 = pd.read_csv(file1, sep=';')
            self.aantallen_gemeente_df2 = pd.read_csv(file2, sep=';')
            self.ziekenhuisopnames_df1 = pd.read_csv(file3, sep=';')
            self.ziekenhuisopnames_df2 = pd.read_csv(file4, sep=';')
        except Exception:
            self.aantallen_gemeente_df1 = None

        self.merged_clean_dataset = self.prepare_merged_dataset()

    def prepare_merged_dataset(self) -> pd.DataFrame:
        try:
            if self.aantallen_gemeente_df1 is None:
                raise ValueError("aantallen_gemeente_df1 is niet beschikbaar.")
            return self.aantallen_gemeente_df1.copy()
        except Exception:
            return None

    def set_merged_and_clean_dataset(self, df: pd.DataFrame):
        self.merged_clean_dataset = df

    # Merged_clean_dataset is het resultaat van het samenvoegen van de oorspronkelijke RIVM-datasets.
    def get_merged_and_clean_dataset(self) -> pd.DataFrame:
        return self.merged_clean_dataset


# Class leest de RNA flow metingen per Rioolwater Zuiveringsinstallatie (RWZI) en het percentuele aandeel van een bepaalde gemeente in een RWZI verzorgnigsgebied.
class Riool:
    def __init__(self):
        """
        Leest de aantallen NRA flow in het rioolwater per RWZI verzorgingsgebied en de aandeel van de gemeenten in het
        verzorgingsgebied ziekenhuisopnames voor een gemeenschappelijke datum reeks tussen 2020 en 2025.
        Vervolgens worden de twee datasets samengevoegd tot één schone nieuwe dataset voor de datumreeks. 
        """
        # get the location where the csv files are locally stored. Use joinpath to make the path platform independent
        file1 = CSV_DIR / RWZI_FILE
        file2 = CSV_DIR / RNA_FILE
        
        try:
            self.rwzi_verzorgingsgebied_per_gemeente = pd.read_csv(file1, sep=';')
            self.aantallen_riool = pd.read_csv(file2, sep=';', parse_dates=['Date_measurement'])
        except:
            self.aantallen_riool = None

        self.merged_clean_dataset_riool = None

    def set_merged_and_clean_dataset_riool(self, p_merged_clean_dataset_riool: pd.DataFrame):
        """
        :param p_merged_clean_dataset_riool which is a pandas dataframe
        """
        self.merged_clean_dataset_riool = p_merged_clean_dataset_riool


# converteert een percentage-string van de kolom MUN_SHARE naar een float
def clean_mun_share_column(df, column='MUN_SHARE'):
    """
    Converteert een percentage-string zoals '67%' naar een float zoals 0.67.
    """
    if column in df.columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.replace('%', '', regex=False)
            .astype(float) / 100.0
        )
    return df


# Lees de polygonen voor de provincies, voor Tab2 en Tab3
def load_province_shapefile():
    gdf = gpd.read_file(PROV_SHAPEFILE, layer="B1_Provinciegrenzen_van_Nederland")
    return gdf


# Lees de polygonen voor de gemeenten, voor Tab2 en Tab3
def load_municipality_shapefile():
    gdf = gpd.read_file(MUN_SHAPEFILE, layer="gemeenten")
    return gdf


# Lees de RNA flow per RWZI uit de CSV file, voor Tab 3 
def get_prepared_riool_dataset():
    from config import RNA_FILE
    return read_csv_safe(CSV_DIR / RNA_FILE)

# Lees het gemeentelijk aandeel RWZI uit de CSV file, voor Tab 3 
def get_municipality_share_rwzi_dataset():
    from config import RWZI_FILE
    return read_csv_safe(CSV_DIR / RWZI_FILE)