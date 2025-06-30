# Day 2: Python Basics

# Variables and data types

# Data types

1 # - Integer
12.3 # - Floats
"Boko Haram" # - string
True # - Boolean
False # - Boolean
# - NoneType
None # - NoneType   
# - List
[1, 2, 3, 4, 5] # - List of integers
["Boko", "Haram"] # - List of strings
[1, "Boko", True] # - Mixed list
# - Tuple
(1, 2, 3) # - Tuple of integers
("Boko", "Haram") # - Tuple of strings
(1, "Boko", True) # - Mixed tuple
# - Dictionary
# {"name": "Boko", "group": "Haram"} # - Dictionary with string keys and values
# - Set
{1, 2, 3} # - Set of integers
{"Boko", "Haram"} # - Set of strings
{1, "Boko", True} # - Mixed set

# Variables with data types
full_name = "OluwaTomi Savage" # - String variable
age = 45 # - Integer variable
height = 1.75 # - Float variable   
is_student = True # - Boolean variable
favorite_numbers = [1, 2, 3, 4, 5] # - List variable

# print(full_name,age,height,is_student,favorite_numbers) # - Print the string variable

print("Full Name:", full_name)

full_name = "Big Tee"  # - String variable

print("Updated Full Name:", full_name)

# Naming Variables
# - Variable names must start with a letter or underscore
# - Variable names can contain letters, numbers, and underscores
# - Variable names cannot contain spaces or special characters
# - Variable names are case-sensitive
# - Variable names should be descriptive and meaningful
# - Variable names should not be a reserved keyword in Python
# - Examples of valid variable names:
my_variable = 10  # - Valid variable name
_my_variable = 20  # - Valid variable name with underscore
myVariable = 30  # - Valid variable name with camel case
myVariable1 = 40  # - Valid variable name with number
# Examples of invalid variable names:
# 1my_variable = 50  # - Invalid variable name (cannot start with a number)
# my variable = 60  # - Invalid variable name (cannot contain spaces)
# my-variable = 70  # - Invalid variable name (cannot contain special characters)
# my@variable = 80  # - Invalid variable name (cannot contain special characters)
# my-variable = 90  # - Invalid variable name (cannot contain special characters)
# my variable = 100  # - Invalid variable name (cannot contain spaces)
# my variable = 110  # - Invalid variable name (cannot contain spaces)
# my_variable = 120  # - Valid variable name
# myVariable = 130  # - Valid variable name
# myVariable1 = 140  # - Valid variable name
# my_variable = 150  # - Valid variable name

# Operators
# Arithmetic Operators
a = 10
b = 5   
print("Addition:", a + b)  # - Addition
print("Subtraction:", a - b)  # - Subtraction   
print("Multiplication:", a * b)  # - Multiplication
print("Division:", a / b)  # - Division
print("Modulus:", a % b)  # - Modulus
print("Exponentiation:", a ** b)  # - Exponentiation
print("Floor Division:", a // b)  # - Floor Division
# Comparison Operators
print("Equal:", a == b)  # - Equal
print("Not Equal:", a != b)  # - Not Equal
print("Greater Than:", a > b)  # - Greater Than 
print("Less Than:", a < b)  # - Less Than
print("Greater Than or Equal:", a >= b)  # - Greater Than or Equal
print("Less Than or Equal:", a <= b)  # - Less Than or Equal

# f-strings literal strings
name = "OluwaTomi"
age = 45
ChildBirthage = 34
BalanceBeginningOfTheWeek = 20000000
CarryOSwerey = 100000000
AccountBalance = 30000

print(f"My name is {name} and my child is {age - ChildBirthage} years old, My Balance is {BalanceBeginningOfTheWeek - CarryOSwerey} after spending {CarryOSwerey} on Necessary Miscellaneous,")  #
# print("My name is $name and I am $age years old.") 
# concatenation
greeting = "Hello"
name = "World"
greeting_message = greeting + " " + name
print(greeting_message)  # - Hello World

# Inbuilt-in Features and keywords
# with in for def if else elif while try except import from as class pass break continue return yield global nonlocal assert lambda del raise async await

# logical operators
x = True
y = False
print("Logical AND:", x and y)  # - Logical AND

# add numbers
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
print("adding.........")
addition = float(first_number) + float(second_number)

print(f"The sum of  {first_number} and {second_number} is: {addition}")

# comparisons

'''
== - Equal to
!= - Not equal to   
> - Greater than
< - Less than
>= - Greater than or equal to
<= - Less than or equal to
# is - Identity operator
is not - Identity operator
'''

num3 = 10
num4 = 20

compare = num3 == num4
# compare = "Telma" != "telma"
print(compare)

# Logical Operators - or and is not

val =  1
vall = 1

compare1 = (val == vall) and (val != vall) and ("Telma" == 'telma')
compare2 = (2 >4) or (9<14) 
compare3 = (3<4) or not (3<4)
print(compare1)  # - True

bool = 4>2
compare = not bool #looks for what is false