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