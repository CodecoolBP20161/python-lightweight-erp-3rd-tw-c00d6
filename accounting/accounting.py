# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    list_options = [
                    'Show_table',
                    'Add',
                    'Remove',
                    'Update',
                    'highest profit?',
                    'average (per item) profit'
                    'Back to main menu']
    exit_message = 'Back to main menu'
    title = "accounting"
    while True:
        ui.print_menu(title, list_options, exit_message)
        option = ui.get_inputs(["Please enter a number: "], "")
        if option == '1':
            show_table(data.manager.get_table_from_file('items.csv'))
        elif option == '2':
            add(data_manager.get_table_from_file("items.csv"))
        elif option == '3':
            remove(data_manager.get_table_from_file("items.csv"), 'id')
        elif option == '4':
            update(table, id_)
        elif option == '5':
            which_year_max(table)
        elif option == '6':
            avg_amount(table, year)
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")


    pass
    # you code

    pass


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
# than return the @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
