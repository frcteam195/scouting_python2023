# Python datatypes with examples

"""
Data types are categories of data items that define the types of operations that can be performed on them.
In Python, everything is an object and thus data types are classes and variables are instances (objects) of the
    data type classes
"""

"""
Python is a 'strongly typed' and 'dynamically typed' language
strongly typed = variables have a type and the type matters when performing operations
dynamically typed = the type of variable is determined at runtime and is not declared when initialized
"""

"""
Python has 5 main data types with two having three sub-types each as outlined here:
1. Numeric
    a. Integer
    b. Complex Number
    c. Float
2. Dictionary
3. Boolean
4. Set
5. Sequence Type
    a. String
    b. List
    c. Tuple
"""

"""
Python type() method returns the class type of an object. It is helpful for debugging and can explain why
certain operations are not working as expected
"""

# ***************************************************************
# Numeric data types (int, float, and complex)
a = 42
print("Class type of the variable a is", type(a))
b = 3.14159
print("Class type of the variable a is", type(b))
c = 3.08E8
print("Class type of the variable a is", type(c))
d = 16 + 2j
print("Class type of the variable a is", type(d))
e = 42.
print("Class type of the variable a is", type(e))

# ***************************************************************
# Dictionary
# unordered collection of key:value pairs separated by a column, unlike Sequence data types such
#   as (string, list, tuple) which contain only a single value.
# values can be on any datatype can be duplicated, wheras keys cannot be duplicated and are immutable
dict1 = {'name': 'Mark Maciejewski', 'age': 53, 'kids': ['Emily', 'Matthew']}
print(dict1)
print(type(dict1))
dict2 = {1: 'high goals', 2: 'low goals', 3: 'climb-pts'}
print(dict2)
print(type(dict2))
# How to retrieve pieces if data from a dictionary
age = dict1['age']
print(age)
# How about a nested, or multi-dimensional, dictionary
scoring = {195: {'auto': 16, 'teleop': 45, 'climb': 34},
           230: {'auto': 16, 'teleop': 45, 'climb': 34},
           176: {'auto': 16, 'teleop': 45, 'climb': 34},
           1073: {'auto': 16, 'teleop': 45, 'climb': 34}}
print(scoring)
print(scoring[230])
print(scoring[230]['teleop'])

# ***************************************************************
# Boolean
# Boolean data values are either True or False
bool(3==3)
3==3
type(True)
# type(true)   # This will fail because the t is not capitalized
bool(3==4)
3==4
type(False)
# type(false)
# True = 'hello'   # This will fail becuase "True" and "False" are reserved in Python

# example of useing boolean in code
x=9
if(bool(x%3==0)):
  print(x,"is divisble by 3")
else:
   print(x,"is not divisble by 3")

# ***************************************************************
# Set
# A set is an unordered collection of data type that is iterable, mutable and has no duplicate elements
#   They are created with the set command or by the use of curly brackets
set1 = set("Hello World!")
print(set1)
type(set1)
set2 = {1, 3, 6, 9, 34}
type(set2)
print(set2)
# Sets can be mixed types
set3 = {1, 5, "hi", (3, 4, 5), "bye", 4.56}
print(set3)


# ***************************************************************
# Sequence Type - String
query = 'select * from Teams where Team = 195;'
print(query)
print(type(query))
# String characters can defined by an index that starts at zero
print(query[0])   # Prints the first character
print(query[-1])   # Prints the last character
print(query[9:13])   # Prints characters 9, 10, 11, & 12. Not character 13!
# The len() method will show you the length of a string or any object
print(len(query))

# ***************************************************************
# Sequence Type = List
animals = ["dog", "cat", "horse", "frog", "cow"]
print(type(animals))
primes = [1,2,4,5,7,11]
print(type(primes))
# elements of a list can be changed
primes[2] = 3   # change the third element of the list to the number 3
print(primes)
primes.append(13)   # Can add one, and only one, element to a list
print(primes)
more_primes = [17,19,23]
primes = primes + more_primes
print(primes)
# Python allows multidimensional lists (arrays)
mlist = [[1, 3, 5, 9], [2, 4, 6, 8, 10], [21, 23, 25, 27, 29, 31], [32, 34, 36]]
print(mlist)
for record in mlist:
    print(record)
    print(len(record))

# ***************************************************************
# Sequence Type = Tuple
# A tuple is just like a list except that it is immutable (it cannot be changed once created)
# Lists have built-in methods. Tuples have not built-in methods
tuple1 = 1, 4, 5, 7   # a sequence of values w/o bracketing is a tuple
print(type(tuple1))
tuple1 = (1, 4, 5, 7)   # however, tuples are typically defined with () for brackets
print(type(tuple1))
primes = [1,2,4,5,7,11]   # A list called primes
tuple2 = tuple(primes)
print(tuple2)
print(type(tuple2))
mlist = [[1, 3, 5, 9], [2, 4, 6, 8, 10], [21, 23, 25, 27, 29, 31], [32, 34, 36]]
print(tuple(mlist))