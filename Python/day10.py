# Inheritance

class A:
    def __init__(self):
        print("A")
    
    def method1(self):
        print("Parent method")

class B(A):
    def __init__(self):
        print("B")

    def method2(self):
        print("Child method")

# obj1 = A()
# obj2 = B()

# obj1.method1()
# obj2.method1()
# obj2.method2()


# Simple Inheritance
class Animal:
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")

class Dog(Animal):
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof Woof")

# dog1 = Dog()
# dog1.whoAmI()
# dog1.bark()

# a1 = Animal()
# a1.whoAmI()

# Multi Level Inheritance
class Vehicle:
    def details(self):
        print("Vehicle")

class Car(Vehicle):
    def details(self):
        print("Car")

class BMW(Car):
    def details(self):
        print("BMW")

# Multiple Inheritance
class A:
    def method1(self):
        print("A")

class B:
    def method1(self):
        print("B")

class C:
    def method3(self):
        print("C")

class D(A, B, C):
    # def method1(self):
    #     print("D")

    def method4(self):
        print("Class D")

x1 = D()
x1.method1()
x1.method3()

x2 = A()

a = 10
a = 20

a = 30
a = 'Hello'