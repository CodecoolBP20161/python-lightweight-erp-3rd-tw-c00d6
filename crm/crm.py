# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

title = "Customer Relationship Manager"


# start this manager by a menu
def start():
    list_options = ['Show table',
                    'Add',
                    'Remove',
                    'Update',
                    'Get the id of the customer with the longest name',
                    'Get the e-mail and name of subscribed customers']
    exit_message = 'Back to main menu'

    while True:
        ui.print_menu(title, list_options, exit_message)
        path = os.path.dirname(os.path.abspath(__file__)) + "/customers.csv"
        table = data_manager.get_table_from_file(path)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = str(inputs[0])
        if option == '1':
            show_table(table)
        elif option == '2':
            data_manager.write_table_to_file(path, add(table))
        elif option == '3':
            id = ui.get_inputs(['Enter the ID: '], '')[0]
            data_manager.write_table_to_file(path, remove(table, id))
        elif option == '4':
            id = ui.get_inputs(['Enter the ID: '], '')[0]
            data_manager.write_table_to_file(path, update(table, id))
        elif option == '5':
            get_longest_name_id(table)
        elif option == '6':
            get_subscribed_emails(table)
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")

    pass


# print the default table of records from the file
def show_table(table):
    list_titles = ['id',
                   'name',
                   'e-mail',
                   'subscribed']
    ui.print_table(table, list_titles)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_titles = ['id',
                   'name',
                   'e-mail',
                   'subscribed']
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
    id_list = []
    list_titles = ['id',
                   'name',
                   'e-mail',
                   'subscribed']
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_titles, table)
    return table

# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    longest_names = ['x']
    for line in table:
        if len(line[1]) > len(longest_names[0]):
            longest_names[0] = line[1]
        if len(line[1]) == len(longest_names[0]):
            longest_names.append(line[1])
    for line in table:
        if min(longest_names) in line[1]:
            return(line[0])


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribers = []
    for line in table:
        if '1' in line[3]:
            subscribers.append(line[2] + ';' + line[1])
    return(subscribers)
