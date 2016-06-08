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
path = os.path.dirname(os.path.abspath(__file__)) + "/items.csv"

# start this manager by a menu
def start():
    list_options = [
                    'Show_table',
                    'Add',
                    'Remove',
                    'Update',
                    'highest profit?',
                    'average (per item) profit',]
    exit_message = 'Back to main menu'
    title = "Accounting"
    while True:
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = str(inputs[0])
        if option == '1':
            show_table(data_manager.get_table_from_file(path))
        elif option == '2':
            add(data_manager.get_table_from_file(path))
        elif option == '3':
            remove(data_manager.get_table_from_file(path), 'id')
        elif option == '4':
            update(table, id_)
        elif option == '5':
            which_year_max(data_manager.get_table_from_file(path))
        elif option == '6':
            year_input = ui.get_inputs(["Please enter a year: "], "")
            year = year_input[0]
            avg_amount(data_manager.get_table_from_file(path), year)
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")


    pass
    # you code

    pass


# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ["id", "month", "day", "year", "type", "amount"])
    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_titles = ["id", "month", "day", "year", "type", "amount"]
    new_item = [common.generate_random(table)] + ui.get_inputs(list_titles, table)
    table.append(new_item)
    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for line in table:
        if id_ in line:
            table.remove(line)
    return table
    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):
    id_list =[]
    list_titles = ["id", "month", "day", "year", "type", "amount"]
    for line in table:
        if id_ in line:
            line = [id_] + ui.get_inputs(list_titles, table)
    return table
    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):
    #data_manager.get_table_from_file("items.csv")
    yearly_profit = {}
    for i in table:
        if i[4] == 'in':
            if i[3] not in yearly_profit.keys():
                yearly_profit.update({i[3]: float(i[5])})
            else:
                yearly_profit[i[3]] += float(i[5])
        elif i[4] == 'out':
            if i[3] not in yearly_profit.keys():
                yearly_profit.update({i[3]: (float(i[5]) * -1)})
            else:
                yearly_profit[i[3]] -= float(i[5])
    max_profit = max(yearly_profit.values())
    for key, val in yearly_profit.items():
        if val == max_profit:
            return int(key)







    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    profit = 0
    items_count = 0
    for line in table:
        if str(line[3]) == str(year):
            if str(line[4]) == str("in"):
                profit += int(line[5])
                items_count += (1)
            elif str(line[4]) == str("out"):
                profit -= int(line[5])
                items_count += (1)
    avg_profit = (profit / items_count)
    return avg_profit
