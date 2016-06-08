

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
def print_to_center(item, half_column):
    if len(item) % 2 == 0:
        begin_space = int(half_column - len(item)/2)
        end_space = begin_space
    else:
        begin_space = int(half_column - (len(item)+1)/2)
        end_space = begin_space + 1
    print((' '* begin_space) + item + (' '*end_space) + '|',  end=(''))

def print_table(table, title_list):
    item_length = []
    num_of_titles = len(title_list)
    for line in table:
        for item in line:
            item_length.append(len(item))
    if max(item_length) % 2 == 0:
        half_column = int((max(item_length) + 2)/2)
    else:
        half_column = int((max(item_length) + 3)/2)
    print ('\n')
    for item in title_list:
        print_to_center(item, half_column)
    print ('\n' + ('=' * (num_of_titles*(half_column*2 + 1))))
    for line in table:
        for item in line:
            print_to_center(item, half_column)
        print ("\n" + (('-'*2*half_column) + '|')*num_of_titles)


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
    num = 1
    for option in list_options:
        print ('(%i) %s' % (num, option))
        num += 1
    print ('(0) %s' % exit_message)
    # your code

    pass


# see the function call in main.py
# please add the full question in your list_titles. eg: ["enter the
# title", ".....ect]
def get_inputs(list_titles, title):
    record = []
    for item in list_titles:
        record_to_add = input('%s' % (item))
        record.append(record_to_add)
    return record


# see the function call in main.py
def print_error_message(message):

    print ("Error!")

    pass
