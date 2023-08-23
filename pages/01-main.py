""" import solara
import pandas as pd

# Initialize an empty dataframe for demonstration
data = {
    'Name': [],
    'Age': [],
    'Address': []
}
df = pd.DataFrame(data)

@solara.component
def Page():
    # State for input fields
    name = solara.reactive('')
    age = solara.reactive(0)
    address = solara.reactive('')

    # Handle form submission
    def handle_submit():
        global df
        new_data = pd.DataFrame([{'Name': name.value, 'Age': age.value, 'Address': address.value}])
        df = pd.concat([df, new_data], ignore_index=True)
        print(df)  # Let's print the DataFrame to see if the data is being appended
        name.set('')
        age.set(0)
        address.set('')


    # Display the input form
    with solara.Column(margin=4):
        solara.InputText(label="Name", value=name)
        solara.InputInt(label="Age", value=age)
        solara.InputText(label="Address", value=address)
        with solara.Row():
            solara.Button("Submit", on_click=handle_submit)
            solara.Button("Clear", on_click=lambda: (name.set(''), age.set(0), address.set('')))

    # Display the data
    solara.DataFrame(df, items_per_page=10) """
""" import solara
import pandas as pd

# Initial empty DataFrame
initial_df = pd.DataFrame(columns=['Name', 'Age', 'Address'])

@solara.component
def Page():
    # Use state for the DataFrame
    df, set_df = solara.use_state(initial_df)
    
    # Input fields
    name, set_name = solara.use_state('')
    age, set_age = solara.use_state(0)
    address, set_address = solara.use_state('')
    
    def handle_submit():
        new_data = pd.DataFrame([{'Name': name, 'Age': age, 'Address': address}])
        updated_df = pd.concat([df, new_data], ignore_index=True)
        set_df(updated_df)  # Update the DataFrame state
        set_name('')
        set_age(0)
        set_address('')
    
    # Render components
    solara.InputText("Name", value=name)
    solara.InputInt("Age", value=age)
    solara.InputText("Address", value=address)
    solara.Button("Submit", on_click=handle_submit)
    solara.Button("Clear", on_click=lambda: [set_name(''), set_age(0), set_address('')])
    solara.DataFrame(df)
 """

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
        
    def handle_submit():
        # Ensure data is captured correctly
        new_data = {'Name': name, 'Age': int(age) if age.isdigit() else 0, 'Address': address}
        new_index = len(df)
        df.loc[new_index] = new_data
        set_df(df.copy())  # Update the DataFrame state with a copy to trigger re-rendering
        set_name('')
        set_age('')
        set_address('')

    
    # Render components
    solara.InputText("Name", value=name, on_value=set_name)
    solara.InputText("Age", value=age, on_value=set_age)  # Using InputText for age to handle non-integer inputs gracefully
    solara.InputText("Address", value=address, on_value=set_address)
    solara.Button("Submit", on_click=handle_submit)
    solara.Button("Clear", on_click=lambda: [set_name(''), set_age(''), set_address('')])
    solara.DataFrame(df)
