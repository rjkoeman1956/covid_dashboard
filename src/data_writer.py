from config import CSV_DIR, SHAPEFILES_DIR, GPKG_FILE
import pandas as pd
import geopandas as gpd


def Saveframes():

    # get the location of the datasets from the rivm website
    file1d = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag.csv'
    file2d = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
    file3d = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames.csv'
    file4d = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames_tm_03102021.csv'
    file5d = 'https://data.rivm.nl/data/covid-19/COVID-19_rioolwaterdata.csv'

    try:
        aantallen_gemeente_df1 = pd.read_csv(file1d, sep=';')
        aantallen_gemeente_df2 = pd.read_csv(file2d, sep=';')
        ziekenhuisopnames_df1 = pd.read_csv(file3d, sep=';')
        ziekenhuisopnames_df2 = pd.read_csv(file4d, sep=';')
        aantallen_riool = pd.read_csv(file5d, sep=';')
    except Exception:
        aantallen_gemeente_df1 = None

    # Write the DataFrame to a CSV file
    file1 = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag.csv'
    file2 = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
    file3 = CSV_DIR / 'COVID-19_ziekenhuisopnames.csv'
    file4 = CSV_DIR / 'COVID-19_ziekenhuisopnames_tm_03102021.csv'
    file5 = CSV_DIR / 'COVID-19_rioolwaterdata.csv'

    aantallen_gemeente_df1.to_csv(file1, sep=';')
    aantallen_gemeente_df2.to_csv(file2, sep=';')
    ziekenhuisopnames_df1.to_csv(file3, sep=';')
    ziekenhuisopnames_df2.to_csv(file4, sep=';')
    aantallen_riool.to_csv(file5, sep=';')





