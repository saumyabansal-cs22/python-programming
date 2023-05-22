class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
dog = Dog()
dog.walk() # inherited from Mammal
dog.bark() # defined in Dog 
