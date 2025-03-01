class Student:

    def __init__(self,name,age):

        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)


s1 = Student('Dev',25)
s2= Student('Mohan',89)


s1.display()
s2.display()