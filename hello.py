# Learn Python Coding 2023
# Feng Lin 
# Using Git on Git Bash
########################################
# Print Hello World To the Screen
#
########################################
# DATA TYPES
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean
#######################################
#
#
#

import os
os.system('clear')

first_name = "Feng"
last_name = "Lin"
age = 53

# list
names = ["John", "Bob", "Mary"]

# tuples
tuple_names = ('John', 'Bob', 'Mary')

# dictionary
fav_pizza= {
	"John": "Pepperoni",
	"Bob": "Mushroom",
	"Mary": "Cheese"
	}

print(first_name + " " + last_name + " " + str(age))
print(names)
print(tuple_names)
print(fav_pizza["John"])
print(fav_pizza["Mary"])