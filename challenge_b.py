import re

# read generated file
def read_file(path):
    file = open(path, 'r')
    return file.read()

# turn text to array
def string_to_array(string):
    arr = string.split(',')
    arr.pop()
    return arr

# identify object
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
            type = "Alphabetic"

        new_arr.append((i,type))

    return new_arr

# print to console
def identify_object_in_file(path):
    string = read_file(path)
    arr = string_to_array(string)
    new_arr = identify_object(arr)

    for (object, type) in new_arr:
        print("Object:", object + ", Type:", type)

identify_object_in_file("test.txt")

