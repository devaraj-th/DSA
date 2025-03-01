""""
The copy constructors can be implemented using __copy__ method and it copies the attributes of original object.
"""

class MyClass:

    def __init__(self,attr1,attr2):
        self.attr1=attr1
        self.attr2=attr2

    def __copy__(self):

        new_object = type(self)(self.attr1,self.attr2)

        return new_object
    

obj = MyClass('Dev', 'Ram')
copy_obj = obj.__copy__()

print(f"The original attributes are {obj.attr1} and {obj.attr2}")

print(f'The duplicates are {copy_obj.attr1} and {copy_obj.attr2}')