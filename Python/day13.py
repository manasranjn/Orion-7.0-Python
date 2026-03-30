#Abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def details(self):
        print("BMW")
    
    def start(self):
        print("Start")

class Audi(Car):
    def details(self):
        print("Audi")

    def start(self):
        print("Start")

car1 = BMW()
car2 = Audi()

# car1.details()
# car2.details()

# Modules
# Built-in modules
# import math
# print(math.pi)
# print(math.sqrt(25))
# print(math.ceil(4.5))
# print(math.floor(4.5))
# print(math.round(4.5)) # Not available in python

# import math as m
# print(m.pi)
# print(m.sqrt(25))
# print(m.ceil(4.5))

# from math import pi, sqrt, ceil
# print(pi)
# print(sqrt(25))
# print(ceil(4.5))

# from math import *
# print(pi)
# print(sqrt(25))
# print(ceil(4.5))

# from random import *
# print(random())
# print(uniform(1,10))

# from calendar import *
# print(calendar(2026))
# print(month(2026, 2))

# User defined modules
# import calculator
# print(calculator.add(10,20))
# print(calculator.sub(10,20))
# print(calculator.mul(10,20))
# print(calculator.div(10,20))

# from calculator import add, sub, mul, div
# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))
# print(div(10,20))

import calculator as c
# print(c.add(10,20))
# print(c.sub(10,20))
# print(c.mul(10,20))
# print(c.div(10,20))
print(c.power(10,2))