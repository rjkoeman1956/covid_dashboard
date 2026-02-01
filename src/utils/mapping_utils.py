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
