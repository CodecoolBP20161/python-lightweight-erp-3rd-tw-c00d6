# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()


# start this manager by a menu
def start_module():
    title = "Human resources manager: "
    exit_message = "Back to the main menu"
    options = ["Show the table",
               "Add to table",
               "Remove form table",
               "Update the table",
               "Get the oldest person(s)",
               "Get the closest persons(s) to average",
               "Back to the main menu"]
    while True:
        ui.print_menu(title, options, exit_message)
        inputs = ui.get_inputs(["\nPlease enter a number: "], "")
        option = int(inputs[0])
        if option == 1:
            show_table(data_manager.get_table_from_file("persons.csv"))
        elif option == 2:
            add(data_manager.get_table_from_file("persons.csv"))
        elif option == 3:
            remove()
        elif option == 4:
            update()
        elif option == 5:
            get_oldest_person()
        elif option == 6:
            get_persons_closest_to_average()
        elif option == 0:
            break
        else:
            raise KeyError("There is no such option.")
        pass



# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ["id", "names", "year of birth"])
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    name = ui.get_inputs(["Please enter the name: "], "")
    year_of_birth = ui.get_inputs(["Please enter the year of birth: "], "")

    return table

# start()
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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
