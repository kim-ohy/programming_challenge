import re
import os

# read generated file
def read_file(path):
    file = open(path, 'r')
    return file.read()

# turn content of text file to array
def string_to_array(string):
    arr = string.split(',')

    # remove last element as it is empty
    arr.pop()
    
    return arr

# identify object in the array
def identify_object(arr):
    new_arr = []

    for i in arr:
        if i.__contains__(' '):
            type = "Alphanumeric"
            i = i.strip(' ')
        elif i.__contains__('.'):
            type = "Real number"
        elif re.search(r'[0-9]', i):
            type = "Integer"
        else:
            type = "Alphabetical String"

        # add to a new array for printing
        new_arr.append((i,type))

    return new_arr

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

# identify objects and print to console
def identify_object_in_file(path):
    string = read_file(path)
    arr = string_to_array(string)
    new_arr = identify_object(arr)
    new_file("final_output.txt")
    
    for (object, type) in new_arr:
        line = "Object: " + object + ", Type: " + type
        write_to_file("final_output.txt", line)
        print(line)

identify_object_in_file("output.txt")

