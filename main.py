# Data types in Python.
from pyscript import display 

firstName = "Calvin"  # String
lastName = "Garcia"  # String
age = 16  # Integer
weight = 50.5  # Float
is_newStudent = False  # Boolean
sections = ['Topaz', 'Emerald', 'Sapphire', 'Ruby']  # List

display(f'My name is {firstName} {lastName}. I am {age} years old and I weigh {weight} kilograms.', target='main')
display(f'I am from 10-{sections[0]}')