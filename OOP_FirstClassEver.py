'''
We're going to make a USER class.

Some naming conventions:
classes: Use the singular and "camel case" ie. FirstClass, PokerDeck
variables, functions: Use "snake_case"

# __init__ method -- This method gets called every time you create an instance of
the class (instantiate), if the class contains data (most times). You could create
a class that only holds methods (no data), then you wouldn't need an __init__ method (rare!).

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# self parameter -- Use self parameter to help initialize the data of each user. It refers
to the specific instance of the User class (or any class we're working with). It's behind
the scenes Python magic. Use instance.attribute_name to access specific attrs on
an instance, so: user1.name will return "Joe". The self keyword refers to the current class INSTANCE.
self must always be the FIRST parameter to __init__ and any methods and properties on class instances.

    class User:
        def __init__(self, first):
            self.name = first

    user1 = User("Joe")
    user2 = User("Blanca")

Typically you would name the attribute and the value the same (self.first = first).
However, you don't have to name them the same. Think of them like key: value pairs in a dict.


# Instantiating a Class -- Creating an object that is an instance of a class is called
instantiating a class.

v = Vehicle("Honda", "Civic", 2017)  # Passing the data/arguments that correspond to the __init__ params

In this case v becomes a Honda Civic a new instance of Vehicle.



# ADDING INSTANCE ATTRIBUTES AND METHODS
Attributes are just pieces of data associated with each individual User. Each intance of
user has first, last, age.

This is where OOP gets really useful. Could instead just create a dictionary like this:
dict("first": "Joe", "last": "Smith", "Age": 68). But once we add methods things get a lot
more useful.

# GETTERS VS. SETTERS - Just terms for describing some methods. For example, the instance methods
we created (full_name, initials, is_senior) are all "GETTERS" - only retrieving information.
SETTERS are where you update/edit the original attributes (see birthday method below).
Ex. age for user1 was originally 68 but then birthday method changes it to 69.




Social Media Comment class - Users on social media can comment on posts/photos.
Each comment should have username, text, likes

class Comment:
     def __init__(self, username, text, likes=0):
         self.username = username
         self.text = text
         self.likes = likes
'''

class User:  # Created the class but haven't used it yet. Need to create an instance of that class
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # Used to initialize the data for each user

    def full_name(self):  # INSTANCE METHOD - must add self param
        return f"{self.first} {self.last}"

    def initials(self):  # INSTANCE METHOD - must add self param
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        # if self.age >= 65: return True
        return self.age >= 65

    def birthday(self):  # INSTANCE METHOD (a "setter")
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!"




user1 = User("Joe", "Smith", 68)  # This instantiates a new User class object.
user2 = User("Blanca", "Lopez", 41)
# user3 = User("Archie")
# user4 = User("Aaron")
# print(user1)  # <__main__.User object at 90x0xx0...>
# print(type(user1))  # <class '__main__.User'>
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
print(user1.full_name(), user1.initials())
print(user2.full_name(), user2.initials())

print(user1.likes(thing="candy"))
print(user2.likes(thing="chips"))

print(user2.is_senior())  # False
print(f"Before birthday: {user1.age}")  # 68
print(user1.birthday())
print(f"After birthday: {user1.age}")  # 69






