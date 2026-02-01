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
