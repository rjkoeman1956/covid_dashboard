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