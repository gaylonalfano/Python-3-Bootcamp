'''
POLYMORPHISM - A key principle in OOP is the idea of polymorphism - an object can take
on many (poly) forms (morph). Here are two important practical applications:

1. Polymorphism & Inheritance - The same class method works in a similar way for different classes
Cat.speak()  # meow
Dog.speak()  # woof
Human.speak()  # Yo

A common implementation of this is to have a method in a base (or parent) class that is
overridden by a subclass. This is called METHOD OVERRIDING. If other people on a team
want to write their own subclass methods, this is useful.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())  # NotImplementedError: Subclass needs to implement this method - need a speak()


2. Special Methods (__dunder__ methods, etc) - The same operation works for different kinds of objects:
sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)

8 + 2 = 10
"8" + "2" = "82"

Python classes have special (aka "magic") methods that are dunders. These methods with special
names that give instructions to Python for how to deal with objects.

'''
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())  # NotImplementedError: Subclass needs to implement this method - need a speak()