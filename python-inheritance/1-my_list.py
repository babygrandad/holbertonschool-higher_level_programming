#!/usr/bin/python3
"""
This script demonstrates the use of the MyList class which
inherits from the built-in list class, with additional functionality.
"""

# Importing the MyList class from the module '1-my_list'
MyList = __import__('1-my_list').MyList

# Creating an instance of MyList
my_list = MyList()

# Appending elements to the list
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Printing the original list
print(my_list)

# Printing the sorted version of the list using the custom print_sorted method
my_list.print_sorted()

# Printing the list again to show it remains unchanged
print(my_list)
