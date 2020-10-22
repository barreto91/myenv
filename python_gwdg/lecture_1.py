a= 10
print(a)


####

b = 100    # new variable 'b' with a value of 100
print(b)   # display b in the command line

b = 50     # assign a new value to b
print(b)

b = b/2    # assign half of its former value to b
print(b)


###multiplication and exponentials

print(10 * 3)
print(10 ** 3)



### finding type of variable

# define variables a and b
a = 10
b = 3

# calculate a/b assign this value to c
c = a/b

# display the types of a, b, and c
print(type(a))
print(type(b))
print(type(c))
######
print("\n")
print("\n")
print("\n")
######

# c is a float at the moment
c = 3.7
print(c)

# now we convert c to a float
c = int(c)
print(c)

# a is an integer at the moment
a = 10
print(a)

# now we convert a to a float
a = float(a)
print(a)

#####strings#####

animal = "Black-tailed \
rattlesnake"
print(animal)

##
# declare a string with "..."
animal_1 = "cat"

# or with '...'
animal_2 = 'dog'

# these two alternatives allow us to use quotation marks in strings
animal_3 = '"bird"'

print(animal_1)
print(animal_2)
print(animal_3)

####
# a string which is too long for one line
quote = "Linus Torvalds once said, \
'Any program is only as good as it is useful.'"
print(quote)

print("\n")
print("\n")
# a string that covers multiple lines

multiline_string = '''This is a string in which I
can comfortably write on multiple lines
without worring about using the escape character "\\" as in
the previous example.

As you'll see, the original string formating is preserved.
'''

print(multiline_string)

###
# define two variables which each save one string
first_name = 'Margaret'
last_name = 'Hamilton'

# combine both variables
full_name = first_name + last_name
print(full_name)

####
# improved example with whitespace
whitespace = ' '
full_name = first_name + whitespace * 4 + last_name
print(full_name)

###
a = 15     # define variables
b = 3
c = a * b  # calculate something

# make the output more readable
print('if you multiply ' + str(a) + ' by ' + str(b) + \
          ', the result is ' + str(c))

###

calculation = '(5 * 4) + 2'
result = (5 * 4) + 2

# the curly brackets mark place holders which
# shall be replaced by str.format()
string_template = 'The result of {} is {}!'

print(string_template.format(calculation, result))


# tabs
print('Hello world!')
print('\tHello world!')
print('Hello \tworld!')

# New line at the start of the string
print('\nHello world!')

# New line at the end of the string
print('Hello world!\n')

# New line in the middle of the string
print('Hello \nworld!')
