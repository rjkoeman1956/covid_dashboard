#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:00:27 2025

@author: hvingen
"""

# Cel 1
# Import modules
import sys
from pathlib import Path

# Zoek project root waar config.py staat
project_root = Path.cwd()
while not (project_root / 'config.py').exists() and project_root != project_root.parent:
    project_root = project_root.parent
sys.path.insert(0, project_root.as_posix())

# Voeg ook src/ toe aan sys.path
SRC_DIR = project_root / "src"
if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# Importeer paden en hulpfuncties
from config import SRC_DIR, CSV_DIR, SHAPEFILES_DIR, EXPORTS_DIR, UTILS_DIR
# from notebook_setup import init_notebook_environment
# from ui_helpers import setup_tab_controls

# Init-actie (optioneel print info)
# init_notebook_environment()


# Cel 2
# 📂 List of columns in the clean COVID dataset
import data_service

df = data_service.get_prepared_covid_dataset()
print("Beschikbare kolommen in df:", df.columns.tolist())



# Cel 3
# 📦 Widget imports
import ipywidgets as widgets



# Cel 4
# 📂 Paden instellen + modules laden
import os, sys
from pathlib import Path

project_root = Path.cwd()
while not (project_root / 'config.py').exists() and project_root != project_root.parent:
    project_root = project_root.parent
sys.path.insert(0, project_root.as_posix())

from config import SRC_DIR, CSV_DIR
if SRC_DIR.as_posix() not in sys.path:
    sys.path.insert(0, SRC_DIR.as_posix())

import data_service 
from data_service import get_metric_mapping, get_available_years
import covid_dashboard_presenter
from IPython.display import display
from ipywidgets import Button, Layout, Textarea, HBox, VBox

from data_service import get_province_heatmap_data
from data_service import get_municipality_heatmap_data
from data_service import get_province_heatmap_riool_data
from data_service import get_municipality_heatmap_riool_data

from covid_dashboard_presenter import plot_province_heatmap
from covid_dashboard_presenter import plot_municipality_heatmap
from covid_dashboard_presenter import plot_province_heatmap_riool
from covid_dashboard_presenter import plot_municipality_heatmap_riool

# Let Municipalities checkbox flip exclusive
def on_municipalities_change(change):
    if change['new'] == True:
        months_checkbox.value = False

# Let Months checkbox flip exclusive
def on_months_change(change):
    if change['new'] == True:
        municipalities_checkbox.value = False

# Plot Covid GUI
def plot_covid(year, total_reported, hospital_admission, deceased, province, municipalities, months):
    covid_dashboard_presenter.plot_covid(df,
                                        year, 
                                        total_reported, 
                                        hospital_admission, 
                                        deceased, 
                                        province, 
                                        municipalities, 
                                        months)  

# Functie om de heatmap bij te werken
def update_province_heatmap(year, column):
    gdf = get_province_heatmap_data(year)
    plot_province_heatmap(gdf, column=column)

# Functie om de heatmap bij te werken
def update_municipality_heatmap(year, metric):
    gdf = get_municipality_heatmap_data(year)
    plot_municipality_heatmap(gdf, metric=metric)

# Plot Rioolwater GUI
def plot_covid_riool(year):
    covid_dashboard_presenter.plot_covid_riool(year)  

# Create a list of outs for tabs
out1 = widgets.Output()
out2 = widgets.Output()
out3 = widgets.Output()
out4 = widgets.Output()

# Create a list of tabs for GUI
tabs = widgets.Tab(children = [out1, out2, out3, out4])
tabs.set_title(0, 'Covid Barcharts')
tabs.set_title(1, 'Covid Heatmap')
tabs.set_title(2, 'Sewer Heatmap')
tabs.set_title(3, 'Download dataset')

print('Werkdirectory ingesteld op:', os.getcwd())





# Cel 5
with out1:
    title_widget1 = widgets.HTML("<h3 style='text-align:left; margin-left:90px;'>COVID-Dataset</h3>")
    year_dropdown = widgets.Dropdown(description='Year:', options=get_available_years(df))
    total_reported_checkbox = widgets.Checkbox(value=True, description='Total reported')
    hospital_admission_checkbox = widgets.Checkbox(value=True, description='Hospital admission')
    deceased_checkbox = widgets.Checkbox(value=True, description='Deceased')
    province_dropdown = widgets.Dropdown(description='Level:', options=['Netherlands', 'All provinces'] + df['Province_merged'].dropna().unique().tolist(), value='Netherlands')
    municipalities_checkbox = widgets.Checkbox(value=True, description='Municipalities')
    months_checkbox = widgets.Checkbox(value=False, description='Months')
    months_checkbox.observe(on_months_change, names='value')
    municipalities_checkbox.observe(on_municipalities_change, names='value')

    row1 = VBox( [year_dropdown, total_reported_checkbox, hospital_admission_checkbox, deceased_checkbox, province_dropdown, municipalities_checkbox, months_checkbox])
    ui = VBox( [title_widget1, row1])
    out = widgets.interactive_output(plot_covid, {
        'year':year_dropdown, 
        'total_reported':total_reported_checkbox, 
        'hospital_admission':hospital_admission_checkbox, 
        'deceased':deceased_checkbox, 
        'province': province_dropdown, 
        'municipalities': municipalities_checkbox, 
        'months': months_checkbox
    } )
    display(ui, out)
    
    
    
# Cel 6
with out2:              
    title_widget2 = widgets.HTML("<h3 style='text-align:left; margin-left:90px;'>Heatmap Provinces</h3>")       
    year_dropdown = widgets.Dropdown(description='Year:', options=get_available_years(df))    
    region_dropdown = widgets.Dropdown(description='Level:', options=['Provinces', 'Municipalities'], value='Provinces')       
    metric_options = get_metric_mapping()
    metric_dropdown = widgets.Dropdown(description='Metric:', options=list(metric_options.keys()), value='Total reported')
    # metric = metric_options[metric_label]
    
    def update_heatmap(year, metric_label, region_type):
        title_text = 'Covid Heatmap ' + region_type
        title_widget2.value = f"<h3 style='text-align:left; margin-left:90px;'>{title_text}</h3>"
        metric = metric_options[metric_label]
        if region_type == 'Provinces':
            gdf = get_province_heatmap_data(year)
            plot_province_heatmap(gdf, column=metric)
        else:
            gdf = get_municipality_heatmap_data(year, metric)
            plot_municipality_heatmap(gdf, column=metric)
            
    ui = VBox([title_widget2, year_dropdown, region_dropdown, metric_dropdown])
    out = widgets.interactive_output(update_heatmap, {
        'year': year_dropdown,
        'metric_label': metric_dropdown,
        'region_type': region_dropdown
    })
    display(ui, out)



# Cel 7
with out3:          
    title_widget3 = widgets.HTML("<h3 style='text-align:left; margin-left:80px;'>Heatmap Riool</h3>")
    year_dropdown = widgets.Dropdown(
        description='Year:',
        options=get_available_years(df)
    )
    region_dropdown = widgets.Dropdown(
        description='Level:',
        options=['Provinces', 'Municipalities'],
        value='Provinces'
    )
    def update_heatmap_riool(year, region_type):
        title_text = 'Sewer Heatmap ' + region_type
        title_widget3.value = f"<h3 style='text-align:left; margin-left:90px;'>{title_text}</h3>"
        if region_type == 'Provinces':
            gdf = get_province_heatmap_riool_data(year)
            plot_province_heatmap_riool(gdf, column='RNA_flow_per_100000')
        else:
            gdf = get_municipality_heatmap_riool_data(year)
            plot_municipality_heatmap_riool(gdf, column='RNA_flow_per_100000')

    ui = VBox([title_widget3, year_dropdown, region_dropdown])
    out = widgets.interactive_output(update_heatmap_riool, {
        'year': year_dropdown,
        'region_type': region_dropdown
    })
    display(ui, out)
    
    
    
    
# # Cel 8
# with out4:
#     # Tab 4 - Download RIVM-data
#     title_widget4 = widgets.HTML("<h3 style='text-align:left; margin-left:90px;'>Download data</h3>")
#     from IPython.display import display, Markdown
#     from data_writer import Saveframes
#     from data_writer import Savepoly
    
#     def run_download_poly(*args):
#         output.clear_output()
        
#         try:
#             result = Savepoly()
#             for fname, status in result.items():
#                 print(f"{fname}: {status}")
#         except Exception as e:
#             print(f"❌ Fout bij opslaan of ophalen van resultaten: {e}")
        
#     def run_download(*args):
#         output.clear_output()
        
#         try:
#             result = Saveframes()
#             for fname, status in result.items():
#                 print(f"{fname}: {status}")
#         except Exception as e:
#             print(f"❌ Fout bij opslaan of ophalen van resultaten: {e}")

#     download_button = widgets.Button(description='Download RIVM', button_style='success')
#     download_button.on_click(run_download)
#     download_poly_button = widgets.Button(description='Download CBS', button_style='success')
#     download_poly_button.on_click(run_download_poly)

#     output = widgets.Output()
#     display(widgets.VBox([
#         title_widget4,
#         download_button, download_poly_button,
#         output
#     ]))
    
    
    


# Cel 9
display(tabs)
















