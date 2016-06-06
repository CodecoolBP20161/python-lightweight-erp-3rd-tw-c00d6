# implement commonly used functions here
import random
import string

# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):
    id_list = []
    for line in table:
        id_list.append(line[0])
    while True:
        new_id = ''
        new_id = new_id.join(random.choice(string.ascii_lowercase) for i in range (2))
        new_id = new_id.join(random.choice(string.ascii_uppercase) for i in range (2))
        new_id = new_id.join(random.choice(string.digits) for i in range (2))
        new_id = new_id.join(random.choice(string.punctuation) for i in range (2))
        if new_id not in id_list:
            return new_id
        else:
            continue

    pass
