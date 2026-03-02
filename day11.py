# Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
    
class Dog(Animal):
    def bark(self):
        print("Dog Barking")

class Cat(Animal):
    def meow(self):
        print("Cat Meowing")

dog1 = Dog()
# dog1.bark()
# dog1.speak()

cat1 = Cat()
# cat1.meow()
# cat1.speak()

# Hybrid Inheritance
class A:
    def method1(self):
        print("A")

class B(A):
    def method2(self):
        print("B")
    
class C(B):
    def method3(self):
        print("C")
    
class D(B):
    def method4(self):
        print("D")

#Encapsulation
class Student:
    def __init__(self, name):
        self.name = name #Public

    def display(self):
        print(self.name)
	
s1 = Student("Allen")
# print(s1.name)
# s1.display()

class Student1:
    def __init__(self, name):
        self._name = name #Protected

    def display(self):
        print(self._name)

s2 = Student1("Allen")
# print(s2._name)
# s2.display()

class Student3:
    def __init__(self, name):
        self.__name = name #Private

    def display(self):
        print(self.__name)

s3 = Student3("Allen")
# print(s3.__name)
s3.display()