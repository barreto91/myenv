import numpy as np
print("module loaded")

# this is a list
data_types = ['integer', 'float', 'string', 'list']

# and like this you can iterate its items
for typ in data_types:
    print ("{} is a data type in Python.".format(typ))

#
# access the element in position 0
first_type = data_types[0]
print(first_type)

#
print(data_types[3])### 4 is out of the range


###

# length of the list data_types
number_of_types = len(data_types)

print("There are {} elements in the list data_types." \
      .format(number_of_types))
#
# create a list
animals = ['cat', 'dog', 'bird', 'horse']
print(animals)

# assign a new value to the element at index 2 of the list
animals[2] = 'penguin'
print(animals)


###loop for a list

for typ in data_types:
    print(typ)
