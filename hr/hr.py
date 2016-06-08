# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year))


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()

common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()

path = os.path.dirname(os.path.abspath(__file__)) + "/persons.csv"
# start this manager by a menu
def start():
    title = "Human resources manager: "
    exit_message = "Back to the main menu"
    options = ["Show the table",
               "Add to table",
               "Remove form table",
               "Update the table",
               "Get the oldest person(s)",
               "Get the closest persons(s) to average"]
    while True:
        ui.print_menu(title, options, exit_message)
        inputs = ui.get_inputs(["\nPlease enter a number: "], "")
        option = int(inputs[0])
        if option == 1:
            show_table(data_manager.get_table_from_file(path))
        elif option == 2:
            add(data_manager.get_table_from_file(path))
        elif option == 3:
            id_ = ui.get_inputs(["Please enter the ID, that you want to remove: "], "")
            remove(data_manager.get_table_from_file(path), id_)
        elif option == 4:
            id_ = ui.get_inputs(["Please enter the ID, that you want to update: "], "")
            update(data_manager.get_table_from_file(path), id_)
        elif option == 5:
            get_oldest_person(data_manager.get_table_from_file(path))
        elif option == 6:
            get_persons_closest_to_average(data_manager.get_table_from_file(path))
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ["id", "names", "year of birth"])
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    ID = [common.generate_random(table)]
    name = ui.get_inputs(["Please enter the name: "], "")
    year_of_birth = ui.get_inputs(["Please enter the year of birth: "], "")
    new_item = [ID + name + year_of_birth]
    table += new_item
    data_manager.write_table_to_file(path, table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    correct_rem_id = id_[0]
    id_table = []
    for lines in table:
        # create a list to id-s
        id_table.append(lines[0])
    for y in range(len(id_table)):
        if correct_rem_id in id_table[y]:
            # remove ID's line
            table.pop(y)
            # write to file the new table(without removed id line)
            data_manager.write_table_to_file(path, table)
    show_table(table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    correct_upd_id = id_[0]
    id_table = []
    for lines in table:
        # create a list to id-s
        id_table.append(lines[0])
    for y in range(len(id_table)):
        if correct_upd_id in id_table[y]:
            name = ui.get_inputs(["Please enter the name: "], "")
            year_of_birth = ui.get_inputs(["Please enter the year of birth: "], "")
            # create a list with the updated info
            update_item = [correct_upd_id, name[0], year_of_birth[0]]
            table[y] = update_item
            # write to file the new table(update updating id line)
            data_manager.write_table_to_file(path, table)
    show_table(table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    years_list = []
    oldest_persons = []
    for line in table:
        years_list.append(int(line[2]))
    for line in table:
        if int(line[2]) == min(years_list):
            oldest_persons.append(line[1])
    return(oldest_persons)


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    ages =[]
    closest_ages = [[0, 0, 10000]]
    results = []
    for line in table:
        ages.append(int(line[2]))
    avg_age = common.list_summa(ages) / len(ages)
    print (avg_age)
    for line in table:
        difference = int(line[2])-avg_age
        if difference < 0:
            difference = difference*(-1)
        closest_dif = int(closest_ages[0][2])-avg_age
        if closest_dif < 0:
            closest_dif = closest_dif*(-1)
        if difference < closest_dif:
            closest_ages = [line]
        elif difference == closest_dif:
            closest_ages.append(line)
    for line in closest_ages:
        results.append(line[1])
    return results


    pass
