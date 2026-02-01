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
























def print_debug_table(df, label_column, value_column, title="Debug info", unit=None, precision=1):
    print(f"\n{title}:\n")
    for _, row in df.iterrows():
        label = row[label_column]
        value = round(row[value_column], precision)
        suffix = f" {unit}" if unit else ""
        print(f"{label}: {value}{suffix}")

def print_debug_summary(df, column):
    print(f"Sample values in '{column}':")
    print(df[column].head(10).to_string(index=False))
    print("Max value:", df[column].max())
    print("Column type:", df[column].dtype)
    print("Non-NaN values:", df[column].notna().sum())

def print_merge_status(merged, df_grouped, key):
    debug_merge = merged.merge(df_grouped, on=key, how='left', indicator=True)
    print("Merge-status:\n", debug_merge['_merge'].value_counts())

def print_column_names(df):
    print("Column names:", df.columns.to_list())

