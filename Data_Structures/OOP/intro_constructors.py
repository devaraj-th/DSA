"""
With in OOP, There are two two types of constructors
1. Default
2. Parameterized

Example : __init__(self). ->default
__init__(self,par1,par2) -> parameterized

"""

class Person:

    def __init__(self):
        pass


ob = Person()

print(ob)


class Vehicle:

    def __init__(self,fuel_type,milage):
        self.fuel_type = fuel_type
        self.milage = milage


obj = Vehicle('petrol',22)

print(obj.fuel_type)
print(obj.milage)