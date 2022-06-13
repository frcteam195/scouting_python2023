# A little formatting in Python to get started

# everything after a pound sign is a comment
# comment
from re import A


print("hello") # comment

"""
Everything
between
the triple
quotes
is a comment.
Nice for multiline comments
"""
print("hello again")

# Sometimes it is nice to temporarily block a chunk of code
""" num1 = 3
num2 = 7
product = num1 * num2
print("the product is " + str(product)) """
# In VS Code highlight the block to toggle and select "Ctrl, Shift, A"

# Python indenting should ALWAYS be four spaces
num = 31
if num == 32:
    print("num equals 32")
else:
    print("num does not equal 32")
# note that the end of the "if" statement and the end of the "else" statement are defined by the indentation

# Handling long lines of code with continuation (the line spans multiple lines in the code)
# Implicit line continuation (any content between brackets can be separated on multiple lines)
a = [[1, 2, 5], [7, 9, 11], [9, 8, 7]]
print(a)
b = [
    [1, 2, 5],
    [7, 9, 11],
    [9, 8, 7],
]
print(b)
# Explicit line continuation - use the "\" character to indicate the line spans to the next line
answer = \
    3.14 * 5000 \
    + 500 + 400
print(answer)



