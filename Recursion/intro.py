"""
Any function which call itself is a recursive function, it solves the problem by calling a copy of itself to work on a smaller problem.

Base case: At some point a function can perform sub task without calling itself called base case
Recursive case: The function calls itself to perform the sub task.

"""

def factorial(n):

    if n ==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)



num = 5

print(factorial(num))