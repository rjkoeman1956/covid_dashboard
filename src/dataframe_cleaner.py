import pandas as pd
from config import SRC_DIR, CSV_DIR

date_pattern1 = r'(?:^\d{2}-0[1-9]|1[0-2])-\d{4}$'  # DD-MM-YYYY pattern
date_pattern2 = r'(?:^\d{4}-0[1-9]|1[0-2])-\d{2}$'  # YYYY-MM-DD pattern
date_pattern3 = r'(?:^\d{2}/0[1-9]|1[0-2])/\d{4}$'  # DD/MM/YYYY pattern
date_pattern4 = r'(?:^\d{4}/0[1-9]|1[0-2])/\d{2}$'  # YYYY/MM/DD pattern

def determine_date_format_date_of_publication(dataframes: object) -> str:
    """
    Deze functie bepaalt in welke datumnotatie de gegevens in de kolom ‘Date_of_publication’ zijn opgeslagen. 
    Er worden vier datumnotaties gecontroleerd. Als een kolom die notatie bevat, kan die notatie worden gebruikt om de gegevens als datum te lezen
    :param een instantie van de class DataFrames : dataframes
    :return: string
    """
    if dataframes.aantallen_gemeente_df1['Date_of_publication'].str.contains(date_pattern1).any(): date_format = '%d-%m-%Y'
    elif dataframes.aantallen_gemeente_df1['Date_of_publication'].str.contains(date_pattern2).any(): date_format = '%Y-%m-%d'
    elif dataframes.aantallen_gemeente_df1['Date_of_publication'].str.contains(date_pattern3).any(): date_format = '%d/%m/%Y'
    elif dataframes.aantallen_gemeente_df1['Date_of_publication'].str.contains(date_pattern4).any(): date_format = '%Y/%m/%d'
    return date_format

def determine_date_format_date_of_statistics(dataframes: object) -> str:
    """
    Deze functie bepaalt in welke datumnotatie de gegevens in de kolom ‘‘Date_of_statistics’’ zijn opgeslagen
    Er worden vier datumnotaties gecontroleerd. Als een kolom die notatie bevat, kan die notatie worden gebruikt om de gegevens als datum te lezen
    :param een instantie van de class DataFrames : dataframes
    :return: string
    """
    if dataframes.ziekenhuisopnames_df1['Date_of_statistics'].str.contains(date_pattern1).any(): date_format = '%d-%m-%Y'
    elif dataframes.ziekenhuisopnames_df1['Date_of_statistics'].str.contains(date_pattern2).any(): date_format = '%Y-%m-%d'
    elif dataframes.ziekenhuisopnames_df1['Date_of_statistics'].str.contains(date_pattern3).any(): date_format = '%d/%m/%Y'
    elif dataframes.ziekenhuisopnames_df1['Date_of_statistics'].str.contains(date_pattern4).any(): date_format = '%Y/%m/%d'
    return date_format

def clean_dataframe_aantallen_gemeente(dataframes: object):
    """
    Deze functie reinigt het dataframe voor aantallen_gemeente
    - voegt een nieuwe kolom toe in een datumtype met behulp van een vooraf bepaalde datumnotatie
    - vervangt de waarden 9999 voor de kolom overleden door 0 voor alle rijen met een datum na 1-1-2023
    :param een instantie van de class DataFrames : dataframes
    """
    date_format = determine_date_format_date_of_publication(dataframes)
    
    # maak een nieuwe kolom van het type datum om later gemakkelijker het jaar en de maand te kunnen bepalen uit de ‘Date_of_publication’
    # en om de waarde voor de overleden records te vervangen door 9999 na de datum 01-01-2023 met de waarde 0
    
    dataframes.aantallen_gemeente_df1['Publication_date'] = pd.to_datetime(dataframes.aantallen_gemeente_df1['Date_of_publication'], format=date_format, errors='coerce')
    dataframes.aantallen_gemeente_df2['Publication_date'] = pd.to_datetime(dataframes.aantallen_gemeente_df2['Date_of_publication'], format=date_format, errors='coerce')

    # Harmoniseer 'Deceased' voor df1 (dagwaarden) en df2 (cumulatief)  
    # Dataset 1 (tot 2021): dagwaarden → alleen 9999 corrigeren
    df1 = dataframes.aantallen_gemeente_df1
    if 'Deceased' in df1.columns:
        df1['Deceased'] = df1['Deceased'].replace(9999, 0).fillna(0).astype(int)

    # Dataset 2 (2022–2023): cumulatieve waarden zijn per provincie → omzetten naar dagwaarden
    df2 = dataframes.aantallen_gemeente_df2
    
    # Controle: als er géén gemeentegegevens zijn → werk op provincie-niveau
    if "Province_merged" in df2.columns:
        
        # Aggregeer voor de zekerheid (ook 2020–21 data)
        # → provincie per dag
        df2 = (
            df2.groupby(["Province_merged", "Publication_date"], as_index=False)
                .agg({"Deceased": "sum"})
        )
    
        # Zet cumulatie → dagwaarden
        df2["Deceased"] = (
            df2.groupby("Province_merged")["Deceased"]
                .diff()
                .fillna(0)
                .astype(int)
        )
    
        # RIVM edge-case: diff kan negatief zijn door reset
        df2.loc[df2["Deceased"] < 0, "Deceased"] = 0
    
        # schrijf terug naar object
        dataframes.aantallen_gemeente_df2 = df2
    
    else:
        # Fallback als structureel anders
        df2["Deceased"] = df2["Deceased"].replace(9999, 0).fillna(0).astype(int)
        dataframes.aantallen_gemeente_df2 = df2

def clean_dataframe_ziekenhuisopnames(dataframes: object):
    """
    Voegt een nieuwe kolom toe aan beide dataframes ziekenhuisopnames in een datumtype met behulp van een eerder bepaalde datumnotatie
    :param een instantie van de class DataFrames : dataframes
    """
    date_format = determine_date_format_date_of_statistics(dataframes)
    # maak een nieuwe kolom van het type datum om later gemakkelijker het jaar en de maand te kunnen bepalen uit de ‘Date_of_statistics’
    dataframes.ziekenhuisopnames_df1['Statistics_date'] = pd.to_datetime(dataframes.ziekenhuisopnames_df1['Date_of_statistics'], format=date_format, errors='coerce')
    dataframes.ziekenhuisopnames_df2['Statistics_date'] = pd.to_datetime(dataframes.ziekenhuisopnames_df2['Date_of_statistics'], format=date_format, errors='coerce')

def add_columns_clean_merged_dataframe(dataframes: object):
    """
    Deze method voegt nieuwe kolommen toe aan de merged_clean_dataset om een betere groepering van gegevens voor het covid-dashboard mogelijk te maken
    :param een instantie van de class Riool : dataframes
    """
    #create new columns for grouping the data on less columns and to ensure that the columns always have a value from one of the two original dataframes
    dataframes.merged_clean_dataset['Municipality_name_merged'] = dataframes.merged_clean_dataset['Municipality_name'].fillna(dataframes.merged_clean_dataset['Municipality_name_x'])
    dataframes.merged_clean_dataset['Province_merged'] = dataframes.merged_clean_dataset['Province_x'].fillna(dataframes.merged_clean_dataset['Province_y'])

    dataframes.merged_clean_dataset['Year'] = dataframes.merged_clean_dataset['Publication_date'].fillna(dataframes.merged_clean_dataset['Statistics_date']).dt.to_period('Y').astype(str)  # format YYYY
    dataframes.merged_clean_dataset['Month'] = dataframes.merged_clean_dataset['Publication_date'].fillna(dataframes.merged_clean_dataset['Statistics_date']).dt.month.astype(int)
    dataframes.merged_clean_dataset['Month_name'] = dataframes.merged_clean_dataset['Publication_date'].fillna(dataframes.merged_clean_dataset['Statistics_date']).dt.month_name().astype(str)

def ensure_merged_municipality_name(df):
    """
    Zorg dat de kolom 'Municipality_name_merged' correct is opgebouwd uit beschikbare kolommen.
    """
    if 'Municipality_name_merged' not in df.columns:
        if 'Municipality_name' in df.columns and 'Municipality_name_x' in df.columns:
            df['Municipality_name_merged'] = df['Municipality_name'].fillna(df['Municipality_name_x'])
        elif 'Municipality_name' in df.columns:
            df['Municipality_name_merged'] = df['Municipality_name']
        elif 'Municipality_name_x' in df.columns:
            df['Municipality_name_merged'] = df['Municipality_name_x']
        else:
            raise ValueError("Geen geschikte kolommen gevonden om 'Municipality_name_merged' op te bouwen.")
    return df

def add_year_and_month_columns(df):
    """
    Voeg kolommen 'Year' en 'Month' toe op basis van Date_of_statistics of Date_of_publication.
    """
    date_col = None
    if "Date_of_statistics" in df.columns:
        date_col = "Date_of_statistics"
    elif "Date_of_publication" in df.columns:
        date_col = "Date_of_publication"

    if date_col:
        df["Year"] = pd.to_datetime(df[date_col], errors="coerce").dt.year.astype("Int64")
        df["Month"] = pd.to_datetime(df[date_col], errors="coerce").dt.month.astype("Int64")

    return df

def clean_mun_share_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Zet kolom 'MUN_SHARE' van percentage (bv. '67%') naar decimaal (bv. 0.67)
    """
    df = df.copy()
    df["MUN_SHARE"] = (
        df["MUN_SHARE"]
        .astype(str)
        .str.strip()
        .str.replace("%", "", regex=False)
        .astype(float) / 100.0
    )
    return df
