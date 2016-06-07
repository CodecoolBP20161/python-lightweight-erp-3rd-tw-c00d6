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
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()

title = 'Store Manager'
list_titles = ['id',
               'title',
               'manufacturer',
               'price',
               'in_stock']

# start this manager by a menu
def start_module():

    # you code

# start this manager by a menu
def start_module():
    list_options = ['(0) Exit',
                    '(1) Show_table',
                    '(2) Add',
                    '(3) Remove',
                    '(4) Update',
                    '(5) Get counts by manufacturer',
                    '(6) Get avarage by manufacturer'
                    '(7) Back to main menu']
    exit_message = 'Back to main menu'

    while True:
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = int(inputs[0])
        if option == 1:
            show_table(data.manager.get_table_from_file('games.csv'))
        elif option == 2:
            add(table)
        elif option == 3:
            remove(table, id_)
        elif option == 4:
            update(table, id_)
        elif option == 5:
            get_counts_by_manufacturers(table)
        elif option == 6:
            get_average_by_manufacturer(table, manufacturer)
        elif option == 0:
            break
        else:
            raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    # your code

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

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
