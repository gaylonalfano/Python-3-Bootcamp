'''
INHERITANCE - Imagine Reddit's platform and you're trying to create that. The users have
a few different levels (user, moderator, admin, etc.). You could create 3 different classes.
But they have a lot that is shared (email, username, password, comments, login, logout, etc.).
We could use INHERITANCE, which is a key feature of OOP is the ability to define a class
which inherits from another class (a "base" or "parent" class). So back to Reddit, you could
have a "base" class called User that has all the common shared parts (email, login, etc.).
Then you could have a Moderator class that inherits from User, etc.

So how do you tell Python that one thing is inheriting something from another?
In Python, inheritance works by passing the parent class as an argument to the definition
of a child class:


class Animal:

    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass  # Need to add this if empty Class


gandalf = Cat()
# gandalf.make_sound("meow")  # meow
# print(gandalf.cool)  # True
# print(Cat.cool)
# print(Animal.cool)

print(isinstance(gandalf, Cat))
print(isinstance(gandalf, object))


'''


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age  # change age to _age
        else:
            self._age = 0

    # Next, define a way to get and set age
    # def get_age(self):
    #     return self._age
    #
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    # Here is where PROPERTIES come in
    # Note that the decorator and function names need to match (age.setter, age(), age())
    @property  # GETTER. Alters how this function works as if it were an attribute
    def age(self):  # The function name becomes the "attribute" name in a way
        return self._age

    @age.setter  # SETTER. Takes in new value. Will learn more about decorators later.
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")
        
    @property  # GETTER
    def full_name(self):
        return f"{self.first} {self.last}"

    # NOT recommended since you're setting property full_name and it's changing two class attributes
    @full_name.setter  # SETTER. Takes in new value.
    def full_name(self, name):
        self.first, self.last = name.split(" ")




jane = Human("Jane", "Goodall", 34)
# print(jane.get_age())
# jane.set_age(45)
# print(jane.get_age())
# jane.age = -100  # People can always do this on accident
print(jane.age)  # age just becomes a proxy for _age internally
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"  # Not ideal but this does work
print(jane.__dict__)  # {'first': 'Tim', 'last': 'Minchin', '_age': 20}
