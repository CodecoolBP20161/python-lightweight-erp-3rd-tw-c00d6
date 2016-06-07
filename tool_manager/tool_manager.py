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
        list_of_column_names = ["Id.", "Name", "Manufacturer", "Purchase date(year)", "Durability(years)"]
        try:
            tool_option = int(inputs[0])
        except ValueError:
            continue
        path = os.path.dirname(os.path.abspath(__file__)) + "/tools.csv"
        table = data_manager.get_table_from_file(path)
        if tool_option == 1:
            show_table(table)
        elif tool_option == 2:
            data_manager.write_table_to_file(path, add(table))
        elif tool_option == 3:
            id_num = ui.get_inputs(["Please enter the ID of the element that you would like to remove:"], "")
            data_manager.write_table_to_file(path, remove(table, id_num[0]))
        elif tool_option == 4:
            id_num = ui.get_inputs(["Please enter the ID of the element that you would like to update:"], "")
            data_manager.write_table_to_file(path, update(table, id_num[0]))
        elif tool_option == 5:
            get_available_tools(table)
        elif tool_option == 6:
            names = ["Manufacturer", "Average durability"]
            get_average_durability_by_manufacturers(table)
        elif tool_option == 0:
            break

# print the default table of records from the file
def show_table(table):
    list_of_column_names = ["Id.", "Name", "Manufacturer", "Purchase date(year)", "Durability(years)"]
    ui.print_table(table, list_of_column_names)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_of_titles = ["Please enter the tool's name: ", "Please enter the manufacturer's name:", "Please enter the purchase date:", "Please enter the durability of the product:"]
    ID = (common.generate_random(table))
    new_element = [ID] + ui.get_inputs(list_of_titles, "")
    table.append(new_element)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for i in range(len(table)):
        if str(id_) == str(table[i][0]):
            table.pop(i)
            break
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    list_of_titles = ["Please enter the tool's name: ", "Please enter the manufacturer's name:", "Please enter the purchase date:", "Please enter the durability of the product:"]
    for i in range(len(table)):
        if str(id_) == str(table[i][0]):
            updated_element = ui.get_inputs(list_of_titles, "")
            table[i] = [id_] + updated_element
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
def get_available_tools(table):
    date = 2016
    list_of_column_names = ["Id.", "Name", "Manufacturer", "Purchase date(year)", "Durability(years)"]
    available_tools = [element for element in table if (int(element[3]) + int(element[4])) >= date]
    ui.print_table(available_tools, list_of_column_names)
    for x in range(len(available_tools)):
        available_tools[x][3] = int(available_tools[x][3])
        available_tools[x][4] = int(available_tools[x][4])
    return available_tools


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
def get_average_durability_by_manufacturers(table):
    average_durability = {}
    average_durability = {manufacturer[2]: 0 for manufacturer in table if average_durability.get(manufacturer[2]) == None}
    keys = average_durability.keys()
    counter_dict = {key: 0 for key in keys}
    for tool in table:
        average_durability[str(tool[2])] = average_durability[str(tool[2])] + int(tool[4])
        counter_dict[str(tool[2])] += 1
    for key in average_durability.keys():
        average_durability[key] /= counter_dict[key]
    return(average_durability)
