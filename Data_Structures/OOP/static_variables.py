"""
Static Variables are defined with in the class and outside any instance method.
1. To maintain the consistency of the data across all the methods we can make use of static variable
2. Saves the memory

"""

class Number:

    magic_number= 2 # This is the static variable

    def __init__(self):
        Number.magic_number +=2


Number.magic_number = 8

ob1 = Number()
ob2 = Number()

print(Number.magic_number)

