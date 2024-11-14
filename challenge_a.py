import random
import os
import string
from random import randint

# create file
def new_file(path):
    # create new text file if not exist
    if os.path.isfile(path) != True:
        open(path, "x")
    # clear text file content if exist
    else:
        open(path, 'w')

# write to file
def write_to_file(path, object):
    # open to file to append content
    if os.path.isfile(path) == True:
        file = open(path, "a")
        file.write(object)
        file.close()
    else:
        print("File does not exist.")

# generate alphabetical strings
def generate_alphabetical_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# generate real numbers
def generate_real_num(min, max):
    return str(random.uniform(min, max))

# generate integers
def generate_integer(min, max):
    return str(random.randint(min, max))

# generate alphanumerics
def generate_alphanum(length):
    return (' ' * random.randint(1, 10) + ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            + ' ' * random.randint(1, 10))

# generate random object file
def generate_random_object_file(path):
    new_file(path)
    
    # generate object until text file is 10 mb
    while os.path.getsize(path) < 10000000:
        # randomize object generation
        rand = randint(0, 3)

        if rand == 0:
            object = generate_alphabetical_string(randint(1, 100))
        elif rand == 1:
            object = generate_real_num(1, randint(1, 10000))
        elif rand == 2:
            object = generate_integer(1, randint(10000, 1000000000000))
        elif rand == 3:
            object = generate_alphanum(randint(1, 100))
        # save object to text file
        write_to_file(path, object + ',')
        # to show that the file is running
        print('.', end='')

    print("\nGeneration complete.")

generate_random_object_file("output.txt")