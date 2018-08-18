# _name - Simply a convention. Supposed to be "private" and not used outside of the class
# __name - Name Mangling. Python will mangle/change the name of that attribute. Ex. p._Person__lol to find it
# Used for INHERITANCE. Python mangles the name and puts the class name in there for inheritance purposes.
# Think of hierarchy (Person > [Teacher, Cop, Coach, Student, etc.]). Teacher could also have self._Teacher__lol
# __name__ - Don't go around making your own __dunder__ methods

class Person:
    def __init__(self):
        self._secret = 'hi!'
        self.name = 'Tony'
        self.__msg = "I like turtles"
        self.__lol = "hahahaha"
        # In other programming languages to make private do:
        # private self._secret = "hi!"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         let them in


p = Person()
print(p.name)
print(p._secret)
# print(p.__msg)  # AttributeError: 'Person' object has no attribute '__msg'
print(dir(p))  # list ['_Person__msg', '_Person_lol', '__class__', '__delattr__', ...]
print(p._Person__msg)
print(p._Person__lol)