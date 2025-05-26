import pandas as pd
import data_loader
import dataframe_cleaner
import dataframe_combiner

from data_loader import load_province_shapefile
from data_loader import load_municipality_shapefile

# from utils.debug_utils import (print_debug_table, print_debug_summary, print_merge_status, print_column_names)
# debug_show_dataset_in_gui = True

write_dataset_to_csv_file = False
remove_non_required_data = True

def get_prepared_covid_dataset() -> pd.DataFrame:
    """
    This function call the data_loader (dataframed) and cleans the data and call the datafram_cleaner for aantallen_gemeente, ziekenhuisopnames. After that it calls the 
    dataframe_combiner to merge the different dataframes to a new dataframe. 
    :return: DataFrame
    """
    dfs = data_loader.Dataframes()
    dataframe_cleaner.clean_dataframe_aantallen_gemeente(dfs)
    dataframe_cleaner.clean_dataframe_ziekenhuisopnames(dfs)
    clean_dataset = dataframe_combiner.combine_dataframes(dfs)
    dfs.set_merged_and_clean_dataset(clean_dataset)
    dataframe_cleaner.add_columns_clean_merged_dataframe(dfs)
    if remove_non_required_data:
        clean_small_dataset = dataframe_cleaner.remove_non_required_columns(clean_dataset)
    else:
        clean_small_dataset = clean_dataset
    dfs.set_merged_and_clean_dataset(clean_small_dataset)
    if write_dataset_to_csv_file:
        dfs.merged_clean_dataset.to_csv('merged_clean_data.csv', index=False)
    return dfs.merged_clean_dataset

def get_prepared_riool_dataset() -> pd.DataFrame:
    """
    This function call the data_loader and cleans the data (riool). 
    :return: DataFrame
    """

    dfs_riool = data_loader.Riool()
    dfs_riool.aantallen_riool['Year'] = dfs_riool.aantallen_riool['Date_measurement'].dt.to_period('Y').astype(str)
    dfs_riool.aantallen_riool['Month'] = dfs_riool.aantallen_riool['Date_measurement'].dt.month.astype(int)
    return dfs_riool

def get_heatmap_data(df, gdf, geo_colname, df_colname, group_by, metric_column, year):
    df_year = df[df['Year'] == year]
    df_grouped = df_year.groupby(group_by)[[metric_column]].sum().reset_index()
    gdf = gdf.rename(columns={geo_colname: group_by})
    merged = gdf.merge(df_grouped, on=group_by, how='left')
    return merged

def get_province_heatmap_data(year, metric_column):
    """
    This function combine the covid_dataset and the province shapefill
    :param: year, metric_column
    :return: heatmap_data
    """

    df = get_prepared_covid_dataset()
    gdf = load_province_shapefile()
    return get_heatmap_data(
        df=df,
        gdf=gdf,
        geo_colname='PROV_NAAM',
        df_colname='Province_merged',
        group_by='Province_merged',
        metric_column=metric_column,
        year=year
    )

def get_municipality_heatmap_data(year, metric_column):
    """
    This function combine the covid_dataset and the municipality shapefill
    :param: year, metric_column
    :return: heatmap_data
    """
    df = get_prepared_covid_dataset()
    gdf = load_municipality_shapefile()
    return get_heatmap_data(
        df=df,
        gdf=gdf,
        geo_colname='gemeentenaam',
        df_colname='Municipality_name_merged',
        group_by='Municipality_name_merged',
        metric_column=metric_column,
        year=year
    )

def get_province_heatmap_riool_data(year, metric_column):
    """
    This function combine the riool_dataset and the province shapefill
    :param: year, metric_column
    :return: heatmap_data
    """
    df = get_prepared_riool_dataset()
    df.aantallen_riool = df.aantallen_riool.rename(columns={'RWZI_AWZI_name': 'Gemeentenaam'})
    df_prov = df.gemeenten_per_provincie
    df_merged = pd.merge(df.aantallen_riool, df_prov, on='Gemeentenaam', how='inner')
    return get_heatmap_data(
        df=df_merged,
        gdf=load_province_shapefile(),
        geo_colname='PROV_NAAM',
        df_colname='Gemeentenaam',
        group_by='Provincie',
        metric_column=metric_column,
        year=year
    )

def get_municipality_heatmap_riool_data(year, metric_column):
    """
    This function combine the riool_dataset and the municipality shapefill
    :param: year, metric_column
    :return: heatmap_data
    """
    df = get_prepared_riool_dataset()
    return get_heatmap_data(
        df=df.aantallen_riool,
        gdf=load_municipality_shapefile(),
        geo_colname='gemeentenaam',
        df_colname='RWZI_AWZI_name',
        group_by='RWZI_AWZI_name',
        metric_column=metric_column,
        year=year
    )

def get_metric_mapping_covid():
    return {
        'Total reported': 'Total_reported',
        'Hospital admission': 'Hospital_admission',
        'Deceased': 'Deceased'
    }

def get_metric_mapping_sewer():
    return {
        'RNA flow per 100000': 'RNA_flow_per_100000'        
    }

def get_available_years(df=None):
    if df is None:
        df = get_prepared_covid_dataset()
    return df['Year'].dropna().sort_values().unique().tolist()
