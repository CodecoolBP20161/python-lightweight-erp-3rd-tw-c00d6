

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):
    print (title_list)
    print ('')
    for line in table:
        print (line)


    pass


# An example output:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# see the function call in main.py
def print_menu(title, list_options, exit_message):

    # your code

    pass


# see the function call in main.py
def get_inputs(list_titles, title):
    record = []
    for item in list_titles:
        record_to_add = input('Enter the %s' %item)
        record.append(record_to_add)
    return record


# see the function call in main.py
def print_error_message(message):

    # your code

    pass
