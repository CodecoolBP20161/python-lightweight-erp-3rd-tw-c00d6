# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start():
    menu_options = ["Show tool table",
                    "Add tool",
                    "Remove tool",
                    "Update tool",
                    "Get available tools",
                    "Get average durability by manufacturers"]
    while True:
        ui.print_menu("Tool Manager", menu_options, "Back to Main menu")
        inputs = ui.get_inputs(["Please select an option: "], "")
        tool_option = int(inputs[0])
        path = os.path.dirname(os.path.abspath(__file__)) + "/tools.csv"
        table = data_manager.get_table_from_file(path)
        if tool_option == 1:
            show_table(table)
        elif tool_option == 2:
            data_manager.write_table_to_file(path, add(table))
        elif tool_option == 3:
            data_manager.write_table_to_file(remove(data_manager.get_table_from_file(path)))
        elif tool_option == 4:
            data_manager.write_table_to_file(update(data_manager.get_table_from_file(path)))
        elif tool_option == 5:
            get_available_tools(data_manager.get_table_from_file(path))
        elif tool_option == 6:
            get_average_durability_by_manufacturers(data_manager.get_table_from_file(path))
        elif tool_option == 0:
            break


# print the default table of records from the file
def show_table(table):
    print("3. bejutott")
    list_of_column_names = ["Id.", "Name", "Manufacturer", "Purchase date(year)", "Durability(years)"]
    ui.print_table(table, list_of_column_names)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_of_titles = ["Please enter the person's name: ", "Please enter the manufacturer's name:", "Please enter the purchase date:", "Please enter the durability of the product:"]
    ID = (common.generate_random(table))
    new_element = [ID] + ui.get_inputs(list_of_titles, "")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
def get_average_durability_by_manufacturers(table):

    # your code

    pass
