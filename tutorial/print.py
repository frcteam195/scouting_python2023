# Print a blank line
print()

# Single or double quotes and escape characters?
print('text sits inside quotes')
print("both single and double quotes work just fine")
print()
print("'Use double quotes when you want to print single quotes'")
print('"Use single quotes when you want to print double quotes"')
print()
# What if you want both double and single quotes?
print('Two options:\n(1) use a backslash as an escape character like this Scouter\'s Rock!')
print("""(2) use a triple double quotes to so 'You' can use "either"!""")
print()
# Notice that \n creates a newline
print()

# Space or no space after print?
print('no space after print command')
print ('space before the print command, both work')
# Proper convention is to not use a space
print()

# Let's print with variables
animals = 'dog, cat, horse'    # Notice that the varialbe must be inclosed in quotes
print(animals)
animals = "dog, cat, horse"    # double quotes also work
print (animals)
print()

# How do we mix string variables and text?
print('The value is ' + animals + '!')

# How to mix numeric variable and text?
value = 300
print(value)
try:
    print('The value is ' + value + '!')
except:
    pass
# That last command will fail as Python cannot concatanate a string and a numeric value
# To fix use the str() funtion to convert the numeric variable to a string first
print('The value is ' + str(value) + '!')
print()

# Printing lists
list = []
print(list)   # Prints an empty list
list = ['dog', 'cat', 'horse']  # Prints list of strings
print(list)
list = [1,3,6,9,12]   # Prints lists of numeric values
print(list)
print()

# What if we only wanted a particular element in the list to be printed?
list = [1,3,6,9,12]
print(list[0])   # list items are zero indexed
print(list[1], list[4])
print()

# What if we want to print the last item of a list of unknown length?
list = [1,3,6,9,12]
print(list[-1])   # Negative indexing counts backwards from the end of the list
print(list[-2])
print(list.pop())
print()

# What if we want to set a variable to the last item of a list?
list = [1,3,6,9,12]
var = list.pop()
print(var)
print()

# Above we used "+" concatenation for print variables and text together.
# There are other options
# Here is old school string formatting
age = 53.46735
name = 'Mark Maciejewski'
print("%s is %s years old" % (name, age))
print("%s is %d years old" % (name, age))
print("%s is %f years old" % (name, age))
print("%s is %.2f years old" % (name, age))
print()

# Antoher way is to use f-strings
age = 53.46735
name = 'Mark Maciejewski'
print(f"{name} is {age} years old")
print(F"{name} is {age} years old")   # lowercase or uppercase F works fine
print()

# Other fun stuff with f-strings
print(f"{6 * 12}")
num1 = 6
num2 = 13
print(f"The product of num1 and num2 is {num1 * num2}")



# Data types
# https://www.geeksforgeeks.org/python-data-types/#:~:text=Data%20types%20are%20the%20classification,(object)%20of%20these%20classes.