# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
import common
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager",
    current_file_path +
    "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common",
    current_file_path +
    "/../common.py").load_module()

title = "selling manager"


# start this manager by a menu
def start():
    list_options = ['Show_table',
                    'Add',
                    'Remove',
                    'Update',
                    'Get the id of the lower price item',
                    'Get itmens sold between the given days']
    exit_message = 'Back to main menu'

    while True:
        ui.print_menu(title, list_options, exit_message)
        path = os.path.dirname(os.path.abspath(__file__)) + "/sellings.csv"
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
            get_lowest_price_item_id(table)
        elif option == '6':
            get_items_sold_between(
                table,
                month_from,
                day_from,
                year_from,
                month_to,
                day_to,
                year_to)
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")
    # you code

    pass


# print the default table of records from the file
def show_table(table):
    list_titles = ['id',
                   'title',
                   'price',
                   'month',
                   'day',
                   'year']
    ui.print_table(table, list_titles)


# Ask a new record as an input from the user than add it to @table, than
# return @table
def add(table):
    list_titles = ['title',
                   'price',
                   'month',
                   'day',
                   'year']
    new_item = [common.generate_random(
        table)] + ui.get_inputs(list_titles, table)
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
    list_titles = ['title: ',
                   'price: ',
                   'month: ',
                   'day: ',
                   'year: ']
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_titles, table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of
# descending alphabetical order
def get_lowest_price_item_id(table):
    smallest_prices = [[1, 1, 10000]]
    names = []
    for line in table:
        if int(line[2]) < int(smallest_prices[0][2]):
            smallest_prices = [line]
        if int(line[2]) == int(smallest_prices[0][2]):
            smallest_prices.append(line)
    for line in smallest_prices:
        names.append(line[1])
    for line in table:
        if line[1] == max(names):
            return line[0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(
        table,
        month_from,
        day_from,
        year_from,
        month_to,
        day_to,
        year_to):
    from_date = int(str(year_from) + str(month_from) + str(day_from))
    to_date = int(str(year_from) + str(month_from) + str(day_from))
    results = []
    for line in table:
        date_today = int(str(line[5]) + str(line[3]) + str(line[4]))
        if (date_today > from_date) and (date_today < to_date):
            results.append(line)
    return results

    # your code

    pass
