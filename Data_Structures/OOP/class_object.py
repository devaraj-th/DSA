class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):

        print(f"Hello my name is {self.name} and my age is {self.age}")



obj = Person('Dev',67)

obj.greet()
print(obj.age)

#Class
#Object
#Instance Variable
#__init__method
#instance variables
#instance methods
#instance object