class Animal:
    def makeSound(self):
        print("Animal Sound")
    
class Dog(Animal):
    def makeSound(self):
        print("Dog Barks")

class Cat(Animal):
    def makeSound(self):
        print("Cat Meows")

dog1 = Dog()
dog1.makeSound()

cat1 = Cat()
cat1.makeSound()