from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()

SRC_DIR = PROJECT_ROOT / "src"
UTILS_DIR = PROJECT_ROOT / 'utils'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
CSV_DIR = PROJECT_ROOT / 'data' / 'csv'
SHAPEFILES_DIR = PROJECT_ROOT / 'data' / 'shapefiles'
EXPORTS_DIR = PROJECT_ROOT / 'notebooks' / 'exports'

GPKG_FILE = SHAPEFILES_DIR / "WijkBuurtkaart_2024_v1/wijkenbuurten_2024_v1.gpkg"
LOG_FILE = EXPORTS_DIR / "export_log.csv"

src_file1 = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag.csv'
src_file2 = CSV_DIR / 'COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
src_file3 = CSV_DIR / 'COVID-19_ziekenhuisopnames.csv'
src_file4 = CSV_DIR / 'COVID-19_ziekenhuisopnames_tm_03102021.csv'
src_file5 = CSV_DIR / 'COVID-19_rioolwaterdata.csv'
src_file6 = CSV_DIR / 'gemeenten_per_provincie.csv'
src_file7 = SHAPEFILES_DIR / "B1_Provinciegrenzen_van_NederlandPolygon.shp"
src_file8 = SHAPEFILES_DIR / 'WijkBuurtkaart_2024_v1/wijkenbuurten_2024_v1.gpkg'


link1 = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag.csv'
link2 = 'https://data.rivm.nl/data/covid-19/COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv'
link3 = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames.csv'
link4 = 'https://data.rivm.nl/data/covid-19/COVID-19_ziekenhuisopnames_tm_03102021.csv'
link5 = 'https://data.rivm.nl/data/covid-19/COVID-19_rioolwaterdata.csv'
#link6 = 
link7 = 'https://geodata.cbs.nl/files/Wijkenbuurtkaart/WijkBuurtkaart_2024_v1.zip'
