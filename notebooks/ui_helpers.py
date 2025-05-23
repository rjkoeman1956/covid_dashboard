from ipywidgets import widgets

def setup_tab_controls(tab_id, year_dropdown, province_dropdown,
                       municipalities_checkbox=None, months_checkbox=None,
                       yearsync_checkbox=None,
                       all_year_dropdowns=None):
    """
    Zet synchronisatie en zichtbaarheid op basis van dropdownwaarden per tabblad.
    - tab_id: int (1, 2, 3, 4)
    - year_dropdown: widgets.Dropdown
    - province_dropdown: widgets.Dropdown
    - municipalities_checkbox: widgets.Checkbox | None
    - months_checkbox: widgets.Checkbox | None
    - yearsync_checkbox: widgets.Checkbox | None
    - all_year_dropdowns: dict (keys: tab_id, values: year_dropdown widgets)
    """

    # Synchronisatie van jaar
    def sync_years(change):
        if yearsync_checkbox and yearsync_checkbox.value and all_year_dropdowns:
            selected_year = year_dropdown.value
            for other_id, other_dropdown in all_year_dropdowns.items():
                if other_id != tab_id:
                    other_dropdown.value = selected_year

    if yearsync_checkbox:
        year_dropdown.observe(sync_years, names='value')

    # Verberg checkboxes als provincie 'All Provinces' is
    if municipalities_checkbox and months_checkbox:
        def update_visibility(*args):
            is_filtered = province_dropdown.value != "All Provinces"
            municipalities_checkbox.layout.display = 'inline-block' if is_filtered else 'none'
            months_checkbox.layout.display = 'inline-block' if is_filtered else 'none'

        province_dropdown.observe(update_visibility, names='value')
        update_visibility()
