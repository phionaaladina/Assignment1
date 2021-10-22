# 1. variable
x = 8
y = 2
print(x)
print(y)

print (x*y) # multiple of x and y

print(x**y) # exponential of x and y

print(x/y) # division of x and y, 

print(x//y) # floor division only, keeps the integer part


#2. a)code that prompts user's name
name = input('What is your name?:')

#b) program that prints (displays) your name, address,telephone number
name = input('What is your name?:')

address = input('What is your address?:')

number = input('What is your telephone number?:')

#3. program that accepts user's name as text and age as number
# output a sentence to display user's name and age
name = str(input('What is your name?:'))

age = int(input('What is your age?:'))
    
print(name,age)

#b) To calculate year of birth given age.
YearNow = 2021
age = int(input('What is your age?'))
BirthYear = YearNow - age
print('You were born in {}'.format(BirthYear))


#4. python program to calculate radius of a circle
import math

radius = float(input('Enter radius of the circle:') )

area = math.pi * radius * radius

print('Area of the circle is: {0}'.format(round(area)))

#5a) A python script is a collection of commands in a file designed to be executed like a program.

#b) Behind the scenes when running a python program
# The interpreter reads the python code, checks for syntactical errors,
# If any error found, it halts the process and returns an error message.
# If no error found, it converts the statement into a low level language called byte-codes
# The byte code is executed by a python virtual machine (PVM), which checks for errors.
# If the PVM finds an error, it halts the execution process and returns an error message.
#If no error found by PVM then it gives the final output.
