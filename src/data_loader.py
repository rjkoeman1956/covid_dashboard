from config import CSV_DIR, SHAPEFILES_DIR, GPKG_FILE
import pandas as pd
import geopandas as gpd
from config import src_file1
from config import src_file2
from config import src_file3
from config import src_file4
from config import src_file5
from config import src_file6
from config import src_file7
from config import src_file8

class Dataframes:
    def __init__(self):
        file1 = src_file1
        file2 = src_file2
        file3 = src_file3
        file4 = src_file4

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

    def get_merged_and_clean_dataset(self) -> pd.DataFrame:
        return self.merged_clean_dataset



class Riool:
    # Class Dataframes stores different pandas dataframes. Merged_clean_dataset is the result of cleaning and enriching the original RIVM datasets
    def __init__(self):
        """
        TODO: Describe what this function does.
        """
        # get the location where the csv files are locally stored. Use joinpath to make the path platform independent
#        file5 = CSV_DIR / 'COVID-19_rioolwaterdata.csv'
#        file6 = CSV_DIR / 'gemeenten_per_provincie.csv'

        try:
            self.aantallen_riool = pd.read_csv(src_file5, sep=';', parse_dates=['Date_measurement'])
            self.gemeenten_per_provincie = pd.read_csv(src_file6, sep=';')
        except:
            self.aantallen_riool = None

        self.merged_clean_dataset_riool = None

    def set_merged_and_clean_dataset_riool(self, p_merged_clean_dataset_riool: pd.DataFrame):
        """
        :param p_merged_clean_dataset_riool which is a pandas dataframe
        """
        self.merged_clean_dataset_riool = p_merged_clean_dataset_riool


def load_province_shapefile():
    shapefile_path = src_file7
    return gpd.read_file(shapefile_path)

def load_municipality_shapefile():
    shapefile_path = src_file8
    gdf = gpd.read_file(GPKG_FILE, layer="gemeenten")
    return gdf


