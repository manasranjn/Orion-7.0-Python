# Functions
# Pre-defined Function
# print()
# input()

# User-defined Function
# def function_name():
#     statements

# def sayHello():
#     print('Hello Everyone')

# sayHello()

def greet():
    return 'Hello Everyone'

# message =greet()
# print(message)
# print(greet())

# Function without parameter
def add():
    return 10 + 20

# print(add())
# print(add())

# Function with parameter
def addition(a,b):
    return a + b

# print(addition(10,20))
# print(addition(30,60))

# Function with default parameter
# print(addition(10))

def subtract(a=0, b=0):
    print(a)
    print(b)
    return a - b

# print(subtract(50,10))
# print(subtract(50))
# print(subtract())
# print(subtract(b=50))
# print(subtract(b=50, a=10))

# OOPs - Object Oriented Programming System
class Example:
    def __init__(self):
        print("This is class constructor")

    def sayHello(self):
        print("Hello Everyone")

    def sayGoodbye(self):
        print("Good Bye")

obj1 = Example()
# obj1.sayHello()
# obj1.sayGoodbye()