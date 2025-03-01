class MyClass:

    static_variable =0

    def __init__(self,num1,num2):

        self.dynamic_variable_1 = num1 # Dynamic variable
        self.dynamic_variable_2 = num2

        MyClass.static_variable +=1


obj1 = MyClass(10,20)

obj2 = MyClass(78,9)

print(obj1.dynamic_variable_2)
print(MyClass.static_variable)