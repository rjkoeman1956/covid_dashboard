# Covid-19 Dashboard

## Codebase v9.17

### Working environment

`env` :

`Python executable` : /opt/anaconda3/envs/py312/bin/python
`Python version` : 3.12.9 | packaged by Anaconda, Inc.
`ipywidgets version` : 8.1.5
`geopandas version` : 1.0.1
`fiona version` : 1.10.1
`shapely version` : 2.1.1
`matplotlib version` : 3.10.0

### Working directory

`Working Directory, tree and file locations` : 

```textile
# Mappenstructuur en filelocaties

├── README.md
├── config.py
├── data
│   ├── csv
│   │   ├── 2006-gemeenten-per-provincie.csv
│   │   ├── COVID-19_aantallen_gemeente_per_dag.csv
│   │   ├── COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv
│   │   ├── COVID-19_rioolwaterdata.csv
│   │   ├── COVID-19_ziekenhuisopnames.csv
│   │   ├── COVID-19_ziekenhuisopnames_tm_03102021.csv
│   │   ├── RWZI-verzorgingsgebied-per-gemeente-2025.csv
│   │   └── gemeenten_per_provincie.csv
│   └── shapefiles
│       ├── B1_Provinciegrenzen_van_Nederland.gpkg
│       └── wijkenbuurten_2024_v1.gpkg
├── docs
│   ├── B1_Provinciegrenzen_van_Nederland.md
│   ├── COVID-19_aantallen_gemeente_per_dag.md
│   ├── COVID-19_rioolwaterdata.md
│   ├── COVID-19_ziekenhuisopnames.md
│   ├── RWZI-verzorgingsgebied-per-gemeente-2025.md
│   └── wijkenbuurten_2024_v1.md
├── notebooks
│   ├── COVID-19-Dashboard_NB_v9.17.ipynb
│   ├── exports
│   └── skip_kernel_extension.py
└── src
    ├── __init__.py
    ├── __main__.py
    ├── covid_dashboard_presenter.py
    ├── data_loader.py
    ├── data_service.py
    ├── data_writer.py
    ├── dataframe_cleaner.py
    ├── dataframe_combiner.py
    └── utils
        ├── __init__.py
        ├── debug_utils.py
        ├── export_utils.py
        ├── mapping_utils.py
        ├── notebook_setup.py
        ├── package_check.py
        └── plot_utils.py
```

### Path

De paden worden ingesteld via de module `config.py` in de Working Directory (project_root) van het project:

`config.py` :

```python
# config.sys, Path definitie

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()

SRC_DIR = PROJECT_ROOT / 'src'
UTILS_DIR = SRC_DIR / 'utils'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
CSV_DIR = PROJECT_ROOT / 'data' / 'csv'
SHAPEFILES_DIR = PROJECT_ROOT / 'data' / 'shapefiles'
EXPORTS_DIR = PROJECT_ROOT / 'notebooks' / 'exports'

LOG_FILE = EXPORTS_DIR / 'export_log.csv'

COVID_MUN1_FILE = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
COVID_MUN2_FILE = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag.csv'
COVID_HOS1_FILE = CSV_DIR / 'COVID-19_ziekenhuisopnames_tm_03102021.csv'
COVID_HOS2_FILE = CSV_DIR / 'COVID-19_ziekenhuisopnames.csv'
RNA_FILE = CSV_DIR / 'COVID-19_rioolwaterdata.csv'
GEM_PROV_FILE = CSV_DIR / 'gemeenten_per_provincie.csv'

PROV_FILE = CSV_DIR / 'gemeenten_per_provincie.csv'
RWZI_FILE = CSV_DIR / 'RWZI-verzorgingsgebied-per-gemeente-2025.csv'
PROV_SHAPEFILE = SHAPEFILES_DIR / 'B1_Provinciegrenzen_van_Nederland.gpkg'
MUN_SHAPEFILE = SHAPEFILES_DIR / 'wijkenbuurten_2024_v1.gpkg'


link1 = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
link2 = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag.csv'
link3 = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames_tm_03102021.csv'
link4 = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames.csv'
link5 = 'https://data.rivm.nl/data/covid-19/COVID-19_rioolwaterdata.csv'

link6 = 'https://www.cbs.nl/-/media/imported/onze-diensten/methoden/classificaties/documents/2005/22/2006-gemeenten-per-provincie.xls'
link6 = 'https://www.cbs.nl/-/media/cbs/onze-diensten/methoden/classificaties/overig/gemeenten-alfabetisch-2025.xlsx'
link7 = 'https://www.cbs.nl/-/media/_excel/2025/04/2025-aantal-inwoners-per-rwzi-verzorgingsgebied-1-jan-2024.xlsx'
link8 = 'https://download.geoportaaloverijssel.nl/download-result/2113f2eb-d79a-44d8-9091-b64866970fcc'
link9 = 'https://geodata.cbs.nl/files/Wijkenbuurtkaart/WijkBuurtkaart_2024_v1.zip'
```

### Storage

`/data/csv` : CSV Datasets voor Covid-13 aantallen, ziekenhuisopnames en RNA data, RWZI verzorgingsgebieden per gemeente   

`/data/shapefiles` : GPKG shapefiles voor de provincie- en gemeentegrenzen van Nederland 

### Herkomst en attributen

`/docs` : Bevat de documentatie over de herkomst en de attributen in de datasets in markdown format:

| Specificatie:                                 | Origin dataset:                                     | Update dataset:                         |
| --------------------------------------------- | --------------------------------------------------- | --------------------------------------- |
| `COVID-19_aantallen_gemeente_per_dag.md`      | COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv | COVID-19_aantallen_gemeente_per_dag.csv |
| `COVID-19_rioolwaterdata.md`                  | COVID-19_rioolwaterdata.csv                         |                                         |
| `COVID-19_ziekenhuisopnames.md`               | COVID-19_ziekenhuisopnames_tm_03102021.csv          | COVID-19_ziekenhuisopnames.csv          |
| `RWZI-verzorgingsgebied-per-gemeente-2025.md` | RWZI-verzorgingsgebied-per-gemeente-2025.csv        |                                         |
| `B1_Provinciegrenzen_van_Nederland.md`        | B1_Provinciegrenzen_van_Nederland.gpkg              |                                         |
| `wijkenbuurten_2024_v1.md`                    | wijkenbuurten_2024_v1.gpkg                          |                                         |
| ToDo                                          | 2006-gemeenten-per-provincie.csv                    |                                         |
| ToDo                                          | gemeenten_per_provincie.csv                         |                                         |
|                                               |                                                     |                                         |

### Dictionary

**Referentie:** 

`Covid-13_Dashboard_DD_vXX.YYz.md` De Dictionary datasets beschrijft alle kolommen. Het document staat in de map `/docs`.

**Opmerking:** 

Bij de `GPKG shapefiles` zijn alleen `layers` beschreven die in gebruik zijn voor het project: 

- `B1_Provinciegrenzen_van_Nederland.gpkg` levert de layer: `B1_Provinciegrenzen_van_Nederland`

- `wijkenbuurten_2024_v1.gpkg` levert de layer `gemeenten` en gebruikt daarvoor de index op `gemeentenaam`

# Modules

## Notebook env

`skip_kernel_extension.py` :

```python
def skip(line, cell=None):
    """
    Notebook cell magic:
      %%skip <expr>     # True => sla cell over; False => voer uit
    """
    if eval(line):
        return
    get_ipython().run_cell(cell)

def load_ipython_extension(shell):
    # Registers the skip magic when the extension loads
    shell.register_magic_function(skip, 'line_cell')
    print("Skip kernel extension loaded!")

def unload_ipython_extension(shell):
    # Unregisters the skip magic when the extension unloads
    del shell.magics_manager.magics['cell']['skip']
    print("Skip kernel extension unloaded!")
```

> De module `skip_kernel_extension.py` is nodig voor het werken met notebooks.  Daarvoor staat de module in ``/notebooks`, in de Working Directory dus van de notebooks. De module kan eventueel verwijderd worden als de cellen uit de notebook is opgeschoond.

## Codebase

### data_loader.py

`data_loader.py` : 

```python
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
```

**Opmerkingen:**

`class Dataframes` : deze class leest de aantallen Covid-13 meldingen en ziekenhuisopnames voor een gemeenschappelijke datum reeks tussen 2020 en 2025. 

> De class retourneert `merged_clean_dataset` aan `dataframe_combiner.py` om in de volgende stap de **aantallen gemeenten** samen te voegen met de **ziekenhuisopnames**.
> 
> Deze class blijkt goed te werken.

`class Riool` : deze class leest de RNA flow metingen per Rioolwater Zuiveringsinstallatie (RWZI) en het percentuele aandeel daarvan voor een bepaalde gemeente in het RWZI verzorgingsgebied. 

> Deze class is nog niet af want deze houdt nog niet rekening met `MUN_SHARE` uit de `RWZI_FILE` voor Tab3.  
> 
> De `RNA_FILE` levert de `RNA flow` per `RWZI` aan verschillende gemeenten in diens verzorgingsgebied. 
> 
> De `RWZI_FILE` levert aandeel `MUN_SHARE` per gemeente in een `RWZI` verzorgingsgebied .     

`def clean_mun_share_column(df, column='MUN_SHARE')` : converteert een percentage-string zoals '67%' naar een float zoals 0.67.

> Definitie moet nog gebruikt worden in de class `Riool`

`def load_province_shapefile()` : deze definitie levert de Geopanda polygonen voor de heatmap plot selectie: `Provinces` voor Tab 2 en 3. 

> De werking van deze definitie is nog niet gebleken in een werkende versie van het Dashboard.

`def load_municipalities_shapefile()` : deze definitie levert de Geopanda polygonen voor de heatmap plot selectie: `Municipalities` voor Tab 2 en 3.

> De werking van deze definitie is nog niet gebleken in een werkende versie van het Dashboard.

`def get_prepared_riool_dataset()` : de definitie levert de RNA flow per Rioolwater Zuiveringsinstallatie (RWZI).

> De werking van deze definitie is nog niet gebleken in een werkende versie van het Dashboard.

`get_municipality_share_rwzi_dataset()` : deze definitie levert het dataframe voor het gemeentelijk aandeel in een RWZI verzorgingsgebied.

> De werking van deze definitie is nog niet gebleken in een werkende versie van het Dashboard.

### dataframe_combiner.py

`dataframe_combiner.py` : 

```python
import pandas as pd

def combine_dataframes(dataframes: object) -> pd.DataFrame:
    """
    Verschillende dataframes worden samengevoegd tot een nieuwe dataframe. De nieuwe dataframe die is samengevoegd uit de dataframes en die is opgeschoond, wordt geretourneerd
    :param: dataframes, een instantie van de class DataFrames uit de module data_loader die meerdere pandas-dataframes bevat
    :return: een pandas-dataframe: merged_clean_dataset
    """
    # Maak een nieuwe dataframe op basis van de dataframes aantal_gemeente en ziekenhuisopnames.
    new_aantallen_gemeente_df = pd.concat([dataframes.aantallen_gemeente_df1, dataframes.aantallen_gemeente_df2.iloc[1:, :]], ignore_index=True, axis=0)
    new_ziekenhuisopnames_df = pd.concat([dataframes.ziekenhuisopnames_df1, dataframes.ziekenhuisopnames_df2.iloc[1:, :]], ignore_index=True, axis=0)

    # Voeg in twee stappen een nieuwe kolom Provincie toe aan het dataframe van ziekenhuisopnames, omdat deze ontbreekt.
    # Hiervoor groeperen we eerst het dataframe aantallen gemeente op twee kolommen: Province en Municipality_code
    # en wijzen we deze nieuwe gegevensgroep toe aan een variabele province_df.
    province_df = new_aantallen_gemeente_df.groupby(['Province', 'Municipality_code', 'Municipality_name'], as_index=False, sort=False).agg({'Version': 'count'})

    # Vervolgens voegen we dit nieuwe dataframe samen met het dataframe ziekenhuisopnames op basis van de gedeelde kolom Municipality_code
    # Het nieuwe dataframe merged_ziekenhuisopnames_df bevat ook een kolom Province
    merged_ziekenhuisopnames_df = new_ziekenhuisopnames_df.merge(province_df, left_on=['Municipality_code'], right_on=['Municipality_code'], how='inner')

    # Maak een nieuwe kolom ‘join_column’ in beide dataframes om de dataframes samen te voegen en om te voorkomen dat er op lege kolommen wordt samengevoegd,
    # wat verkeerde resultaten oplevert
    new_aantallen_gemeente_df['join_column'] = new_aantallen_gemeente_df['Date_of_publication'] + new_aantallen_gemeente_df['Municipality_code'].fillna(new_aantallen_gemeente_df.Province).fillna('leeg')
    merged_ziekenhuisopnames_df['join_column'] = merged_ziekenhuisopnames_df['Date_of_statistics'] + merged_ziekenhuisopnames_df['Municipality_code'].fillna('leeg')

    # Voeg de twee datasets samen op basis van de zojuist aangemaakte kolom ‘join_column’ met een outer join.
    merged_clean_dataset = new_aantallen_gemeente_df.merge(merged_ziekenhuisopnames_df, left_on=['join_column'], right_on=['join_column'], how='outer')

    # Na merge, expliciet kolom Province_x hernoemen 
    if "Province_x" in merged_clean_dataset.columns:
        merged_clean_dataset = merged_clean_dataset.rename(columns={"Province_x": "Province"})

    # retourneer samengevoegde_schone_dataset
    return merged_clean_dataset
```

> De werking van deze definitie is goed gebleken.

### dataframe_cleaner.py

`dataframe_cleaner.py` : 

```python
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
```

> De werking van deze definitie is goed gebleken.

### data_service.py

`data_service.py` : 

```python
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
```

> Under contruction

### covid_dashboard_presenter.py

`covid_dashboard_presenter.py` :

```python
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

# Plot Province heatmap voor Tab 2
def plot_province_heatmap(gdf, column):
    plot_heatmap(gdf, column=column, title="Provinces RIVM Covid-19")

# Plot Municipality heatmap voor Tab 2
def plot_municipality_heatmap(gdf, column):
    plot_heatmap(gdf, column=column, title="Municipalities RIVM Covid-19")

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

# Plot provincie heatmap voor Tab 3
def plot_province_heatmap_riool(gdf, region, column):
    plot_riool_heatmap(gdf, region="Municipalities", column="RNA_flow_per_100000", title="Provinces RWZI RNA-flow")

# Plot Municipality heatmap voor Tab 3
def plot_municipality_heatmap_riool(gdf, region, column):
    plot_riool_heatmap(gdf, region, column=column, title="Municipalities RWZI RNA-flow")
```

> Under construction

### data_writer.py

`data_writer.py` :

```python
import pandas as pd
import geopandas as gpd
import os
import shutil
import urllib.request
import requests
import zipfile

from pathlib import Path
from config import link1, link2, link3, link4, link5, link6, link7, link9
from config import CSV_DIR, SHAPEFILES_DIR, COVID_MUN1_FILE, COVID_MUN2_FILE, COVID_HOS1_FILE, COVID_HOS2_FILE, RNA_FILE, PROV_FILE, RWZI_FILE, MUN_SHAPEFILE, PROV_SHAPEFILE

def download_file(url, dest):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        dest.write_bytes(r.content)
        print(f"✅ {dest} downloaded")
        return True
    except Exception as e:
        print(f"❌ Download mislukt voor {dest} ({e})")
        return False

def safe_open_csv(file_path):
    """
    Controleert of een CSV-bestand leesbaar is met een van de bekende encodings.
    Geeft de gevonden encoding terug of None bij mislukking.
    """
    for enc in ("utf-8", "ISO-8859-1", "cp1252"):
        try:
            with open(file_path, encoding=enc) as f:
                f.read(2048)  # kleine test
            return enc
        except UnicodeDecodeError:
            continue
        except Exception:
            break
    return none

def open_prov():
    """
    Download Municipalities per province. De links komen uit config.py

    """
    urls2 = {
        PROV_FILE: link6
    }

    results2 = {}
    for fname, url in urls2.items():
        try:
            df = pd.read_excel(url, sheet_name="Gemeenten_alfabetisch")
            df.to_csv(CSV_DIR / fname, sep=';', index=False, encoding='utf-8')
            print(f"✅ {fname} is downloaded")
        except Exception as e:
            print(f"❌ Download mislukt voor {fname}: {e}")

def open_rwzi():
    """
    Download rwzi file. De links komen uit config.py

    """
    urls3 = {
        RWZI_FILE: link7
    }

    results3 = {}
    for fname, url in urls3.items():
        try:
            df = pd.read_excel(url, sheet_name="Tabel 1", skiprows=3)
            df['regio_code'] == df['regio_code'].str.strip()
            df.drop(df[df['regio_code'].str[:2] == "VR"].index, inplace=True)
            df.columns = df.columns.str.replace('aandeel\n(%)', 'aandeel')
            df["MUN_SHARE"] = (df["aandeel"] * 100).astype(str) + "%"
            df["MUN_NAME"] = df["regio_naam"]
            df["MUN_CODE"] = df["regio_code"] 
            df["RWZI_CODE"] = df["rwzi_code"]
            df.to_csv(CSV_DIR / fname, sep=';', index=False, encoding='utf-8')
            print(f"✅ {fname} is downloaded")
        except Exception as e:
            print(f"❌ Download mislukt voor {fname}: {e}")


def Saveframes(verbose=True):
    urls = [link1, link2, link3, link4, link5, link6, link7, link9]
    files = [
        COVID_MUN1_FILE,
        COVID_MUN2_FILE,
        COVID_HOS1_FILE,
        COVID_HOS2_FILE,
        RNA_FILE #,
    ]
    # print("DOWNLOAD CSV")
    for url, dest in zip(urls, files):
        download_file(url, dest)

def Save_xlsx(verbose=True):
    open_prov()
    open_rwzi()


def Savepoly(verbose=True):
    """
    Download en verwerk het wijkenbuurten-archief (SHAPEFILES_DIR / 'wijkenbuurten_2024_v1.gpkg').
    De downloadlink komt uit config.py (link9).

    Werkwijze:
    1. Download archive.zip naar SHAPEFILES_DIR
    2. Pak uit in tijdelijke map
    3. Detecteer rootmap of losse bestanden in de ZIP
    4. Verplaats inhoud naar SHAPEFILES_DIR
    5. Verwijder tijdelijke map en ZIP-bestand
    """

    os.makedirs(SHAPEFILES_DIR, exist_ok=True)
    results = {}

    from config import link9

    try:
        url = link9
        zip_path = SHAPEFILES_DIR / "archive.zip"
        temp_extract = SHAPEFILES_DIR / "_temp_extract"

        # 1. Download ZIP
        urllib.request.urlretrieve(url, zip_path)
        if verbose:
            print(f"Downloaded: {zip_path}")

        # 2. Uitpakken naar tijdelijke map
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_extract)
        if verbose:
            print(f"Uitgepakt in: {temp_extract}")

        # 3. Detecteer of er een geneste map is
        extracted_items = list(temp_extract.iterdir())
        if len(extracted_items) == 1 and extracted_items[0].is_dir():
            root_folder = extracted_items[0]
            if verbose:
                print(f"Geneste map gedetecteerd: {root_folder.name}")
            source_folder = root_folder
        else:
            source_folder = temp_extract

        # 4. Verplaats alle inhoud naar SHAPEFILES_DIR
        for item in source_folder.iterdir():
            dest = SHAPEFILES_DIR / item.name
            if dest.exists():
                if dest.is_dir():
                    shutil.rmtree(dest)
                else:
                    dest.unlink()
            shutil.move(str(item), SHAPEFILES_DIR)
        if verbose:
            print(f"Inhoud verplaatst naar: {SHAPEFILES_DIR}")

        # 5. Opruimen
        shutil.rmtree(temp_extract, ignore_errors=True)
        if zip_path.exists():
            zip_path.unlink()
        if verbose:
            print("Tijdelijke map en ZIP-bestand verwijderd.")

        results["status"] = "success"
        results["file"] = MUN_SHAPEFILE

    except Exception as e:
        print(f"❌ Fout tijdens verwerking van {MUN_SHAPEFILE}: {e}")
        results["status"] = "error"
        results["error"] = str(e)

    return results
```

> Under construction

### debug_utils.py

`debug_utils.py` :

```python
def print_clean_debug_info(df_filtered, df_grouped, group_col, metric, title, filters=None):
    print("")
    print("="*80)
    print(f"DEBUG: {title}")

    # Filter dataset    
    if filters:
        print(f"Filters: {filters}")
    print("-"*80)    
    print("Filtered dataset info:")
    print(f"• Shape: {df_filtered.shape}")
    print(f"• Columns: {list(df_filtered.columns)}")
    print(f"• Nulls:\n{df_filtered.isnull().sum()}\n")

    # Groeperen per metric       
    if metric in df_filtered.columns:
        print(f"• Min/Max {metric}: {df_filtered[metric].min()} / {df_filtered[metric].max()}")

    print("-"*80)
    print("Grouped table preview:")
    if group_col is None or group_col not in df_grouped.columns or metric not in df_grouped.columns:
        print("⚠️ Debug preview overgeslagen: group_col of metric ontbreekt.")
    else:
        print(df_grouped[[group_col, metric]].head(10).to_string(index=False))

    # print(df_grouped[[group_col, metric]].head(10).to_string(index=False))

    print("="*80)
```

> Under construction

### export_utils.py

`export_utils.py` :

```python
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

```

> Under construction

### mapping_utils.py

`mapping_utils.py` :

```python
# Utils mapping_utils

def get_metric_mapping_tab1():
    return {
        "Total reported": "Total_reported",
        "Hospital admissions": "Hospital_admission",
        "Deceased": "Deceased",
    }

def get_metric_mapping_tab2():
    return {
        "Total reported": "Total_reported",
        "Hospital admissions": "Hospital_admission",
        "Deceased": "Deceased"
    }


def get_metric_mapping_tab3():
    return {
        "RNA flow per 100k": "RNA_flow_per_100000"
    }

def get_all_metric_mappings():
    """
    Voor debugdoeleinden: overzicht van alle mappings per tab
    """
    return {
        "Tab1": get_metric_mapping_tab1(),
        "Tab2": get_metric_mapping_tab2(),
        "Tab3": get_metric_mapping_tab3()
    }
```

> Under construction

### notebook_setup.py

`notebook_setup.py` :

```python
import sys
from pathlib import Path

def init_notebook_environment():
    """
    Zorg dat de /src map beschikbaar is voor imports.
    """
    SRC_DIR = Path.cwd().parent / "src"
    if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))
        print(f"⚠️ SRC toegevoegd aan sys.path: {SRC_DIR}")
    else:
        print(f"✅ SRC aanwezig in sys.path: {SRC_DIR}")
```

> Under construction

### package_check.py

`package_check.py` :

```python
import importlib
import ipywidgets
import matplotlib.pyplot as plt
import sys
from IPython.display import display, clear_output


def check_required_packages(packages=None):
    """
    Controleer of opgegeven Python packages beschikbaar zijn.
    """
    if packages is None:
        packages = ['ipywidgets', 'geopandas', 'fiona', 'shapely', 'matplotlib', 'xlrd', 'zipfile', 'requests', 'shutil', 'reportlab', 'openpyxl']
    print("Checking required packages:")
    for pkg in packages:
        try:
            importlib.import_module(pkg)
            print(f"✅ {pkg} is installed")
        except ImportError:
            print(f"⚠️ {pkg} is NOT installed")


def get_environment_info():
    """
    Geef een dict terug met details over de huidige Python-omgeving.
    """
    return {
        "Python executable": sys.executable,
        "Python version": sys.version,
        "ipywidgets version": ipywidgets.__version__,
    }


def show_widget_test_plot():
    """
    Toon een eenvoudige testplot via ipywidgets en matplotlib om GUI-functionaliteit te controleren.
    """
    output = ipywidgets.Output()

    def show_plot(_=None):
        with output:
            clear_output(wait=True)
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [4, 5, 6])
            plt.show()
            plt.close(fig)

    button = ipywidgets.Button(description="Test Plot")
    button.on_click(show_plot)
    display(ipywidgets.VBox([button, output]))
```

> Under construction

### plot_utils.py

`plot_utils.py` :

```python
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
```

> Under construction
