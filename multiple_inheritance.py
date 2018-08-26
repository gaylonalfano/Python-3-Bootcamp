'''
Not super common but nice to know how things work behind the scenes. Multiple inheritance
is slightly controversial in coding community. Sometimes can seem to overcomplicate things.

When using multiple inheritance, the class that you put first class Penguin(Ambulatory, Aquatic)
When you create an instance of a class that uses multiple inheritance,
the class itself (Penguin) and the first inheritance class (Ambulatory) will run
the __init__, BUT the Aquatic __init__ DOES NOT run. However, the Penguin instance
still has access to the Aquatic class methods due to inheritance.

*TIP* When using multiple inheritance, it's better to be explicit when passing the parent __init__
So, instead of using super(), you should instead use Aquatic.__init__(self, name=name)
and Ambulatory.__init__(self, name=name)



'''

class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT!")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"{self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT!")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    print("PENGUIN INIT!")
    def __init__(self, name):
        # super().__init__(name=name)  # When inheriting multiple classes, better to call parent explicitly
        Ambulatory.__init__(self, name=name)  # self and name are referring to Penguin and Penguin's name attribute
        Aquatic.__init__(self, name=name)  # self and name are referring to Penguin and Penguin's name attribute


# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")  # To see the flow of initializing the inherited classes
#
# print(captain_cook.swim())  # Captain cook is swimming
# print(captain_cook.walk())  # Captain cook is walking
# print(captain_cook.greet())  # I am Captain Cook of the land!
#
# print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
# print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
# print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
# print(f"captain_cook is instance of base object: {isinstance(captain_cook, object)}")