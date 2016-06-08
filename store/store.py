# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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

path = os.path.dirname(os.path.abspath(__file__)) + "/games_test.csv"
title = 'Store Manager'


# start this manager by a menu
def start():
    menu = ['Show table',
            'Add',
            'Remove',
            'Update',
            'Get counts by manufacturer',
            'Get avarage by manufacturer',
            'Exit']
    exit_message = 'Back to main menu'

    while True:
        ui.print_menu(title, menu, exit_message)
        table = data_manager.get_table_from_file(path)
        inputs = ui.get_inputs(["\nPlease enter a number: "], "")
        option = int(inputs[0])
        if option == 1:
            show_table(data_manager.get_table_from_file(path))
        elif option == 2:
            data_manager.dite_table_to_file(path, add(table))
        elif option == 3:
            id_remove = ui.get_inputs(['Please add ID to remove: '], '')[0]
            data_manager.write_table_to_file(path, remove(table, id_remove))
        elif option == 4:
            id_update = ui.get_inputs(['Please add ID to update: '], '')[0]
            data_manager.write_table_to_file(path, update(table, id_update))
        elif option == 5:
            (get_counts_by_manufacturers(data_manager.get_table_from_file(path)))
        elif option == 6:
            manufacturer = ui.get_inputs(['Please add manufacturer to count: '], '')[0]
            (get_average_by_manufacturer(data_manager.get_table_from_file(path), manufacturer))
        #elif option == '7':
        #    break
        else:
            raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):
    list_titles = ['ID',
                   'Title',
                   'Manufacturer',
                   'Price',
                   'In stock']
    ui.print_table(table, list_titles)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_titles = ['Please add tite: ',
                   'Please add manufacturer ',
                   'Please enter price ',
                   'Enter how many is in stock ']
    new_item = [common.generate_random(table)] + ui.get_inputs(list_titles, table)
    table.append(new_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for line in table:
        if id_ in line:
            table.remove(line)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    update_list = []
    list_titles = ['Please add tite: ',
                   'Please add manufacturer ',
                   'Please enter price ',
                   'Enter how many is in stock ']
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_titles, table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    my_dict = {}
    for line in table:
        if line[2] not in my_dict:
            my_dict[line[2]] = 1
        elif line[2] in my_dict:
            my_dict[line[2]] += 1
    return my_dict


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    counter = 0
    in_stock_list = []
    for line in table:
        if manufacturer == line[2]:
            counter += 1
            in_stock_list.append(int(line[4]))
    if counter == 0:
        return 'There is not any manufacturer with this name'
    else:
        return common.list_summa(in_stock_list) / counter
