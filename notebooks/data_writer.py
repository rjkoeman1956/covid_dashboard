from config import CSV_DIR
from config import SHAPEFILES_DIR
import pandas as pd
import geopandas as gpd
import os
from config import link1
from config import link2
from config import link3
from config import link4
from config import link5
from config import link7
import urllib.request
import zipfile

def Saveframes(verbose=True):
    """
    Download COVID-19 datasets van RIVM en sla ze op in /data/csv. De links are from config.py

    Returns:
        dict: Mapping van bestandsnaam → status (geslaagd of fout).
    """
    urls = {
        'COVID-19_aantallen_gemeente_per_dag.csv': link1,
        'COVID-19_aantallen_gemeente_per_dag_tm_03102021.csv': link2,
        'COVID-19_ziekenhuisopnames.csv': link3,
        'COVID-19_ziekenhuisopnames_tm_03102021.csv': link4,
        'COVID-19_rioolwaterdata.csv': link5
    }

    os.makedirs(CSV_DIR, exist_ok=True)

    results = {}
    for fname, url in urls.items():
        try:
            df = pd.read_csv(url, sep=';')
            df.to_csv(CSV_DIR / fname, sep=';', index=False)
            results[fname] = '✅ Geslaagd'
            if verbose:
                print(f"✅ {fname} opgeslagen.")
        except Exception as e:
            results[fname] = f"❌ Fout: {str(e)}"
            if verbose:
                print(f"❌ Mislukt voor {fname}: {e}")

    return results

def Savepoly(verbose=True):
    """
    Download file wijkenbuurten. De links are from config.py
    
    """
    urls = {
        'wijkenbuurten_2024_v1.gpkg': link7
    }

    os.makedirs(SHAPEFILES_DIR, exist_ok=True)

    results = {}
    try:
        url = link7
        file_name = SHAPEFILES_DIR / 'archive.zip'
        zip_file = SHAPEFILES_DIR / 'archive.zip'
        urllib.request.urlretrieve(url, file_name)

        destination_folder = SHAPEFILES_DIR
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
           zip_ref.extractall(destination_folder)
        results['CBS'] = '✅ Geslaagd'
        if verbose:
             print(f"✅ {fname} opgeslagen.")
    except Exception as e:
        results['CBS'] = f"❌ Fout: {str(e)}"
        if verbose:
            print(f"❌ Mislukt voor {fname}: {e}")

    # Province

    return results

