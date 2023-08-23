import solara
import pandas as pd

# Initial empty DataFrame
initial_df = pd.DataFrame(columns=['Name', 'Age', 'Address'])

@solara.component
def Page():
    # Use state for the DataFrame
    df, set_df = solara.use_state(initial_df)
    
    # Input fields
    name, set_name = solara.use_state('')
    age, set_age = solara.use_state('')
    address, set_address = solara.use_state('')
    
    # Selected row for updating
    selected_row, set_selected_row = solara.use_state(None)
    
    def handle_submit():
        new_data = {'Name': name, 'Age': int(age) if age.isdigit() else 0, 'Address': address}
        new_index = len(df)
        df.loc[new_index] = new_data
        set_df(df.copy())
        set_name('')
        set_age('')
        set_address('')
    
    def handle_update():
        if selected_row is not None:
            df.loc[selected_row] = {'Name': name, 'Age': int(age) if age.isdigit() else 0, 'Address': address}
            set_df(df.copy())
    
    def handle_row_selection(row_index):
        set_selected_row(row_index)
        row_data = df.loc[row_index]
        set_name(row_data['Name'])
        set_age(str(row_data['Age']))
        set_address(row_data['Address'])
    
    # Render components
    solara.InputText("Name", value=name, on_value=set_name)
    solara.InputText("Age", value=age, on_value=set_age)
    solara.InputText("Address", value=address, on_value=set_address)
    
    # Dropdown for selecting a row to update
    if not df.empty:
        solara.Dropdown("Select a row to update", options=list(df.index), value=selected_row, on_value=handle_row_selection)
    
    solara.Button("Submit", on_click=handle_submit)
    solara.Button("Update", on_click=handle_update)
    solara.Button("Clear", on_click=lambda: [set_name(''), set_age(''), set_address('')])
    solara.DataFrame(df)
