class my_class:

    __my_variable = None

    def get_method(self):
        return my_class.__my_variable
    

    def set_method(self,value):

        my_class.__my_variable = value

        return value
    

obj = my_class()

obj.set_method(67)

print(obj.get_method())

