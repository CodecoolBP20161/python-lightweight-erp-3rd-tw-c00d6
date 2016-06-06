

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
# table: the list of results, title_list: the title of data, eg: id,
# title, ect.
def print_table(table, title_list):
    print (title_list)
    print ('')  # i will design it later, be patient ;)
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
# list_options is menu options, in a list. exit_message the last option,
# eg: back to main menu
def print_menu(title, list_options, exit_message):
    print ('%s \n \n' % title)
    for option in list_options:
        print ('(%i) %s' % ((list_options.index(option) + 1), option))
    print ('(0) %s' % exit_message)
    # your code

    pass


# see the function call in main.py
# please add the full question in your list_titles. eg: ["enter the
# title", ".....ect]
def get_inputs(list_titles, title):
    record = []
    for item in list_titles:
        record_to_add = input('%s')
        record.append(record_to_add)
    return record


# see the function call in main.py
def print_error_message(message):

    print ("Error!")

    pass
