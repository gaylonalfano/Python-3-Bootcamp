'''
Animal
    species
    name

Cat
    species
    name
    breed
    favorite_toy


in the class Cat, you can call the parent/base class Animal by typing:
Animal.__init__(self, name, species)

However, better is to use super(), which refers to the parent/base class of
whatever the current class is.

'''

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):  # pass Animal into class Cat(Animal) for inheritance
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # self is automatically passed in. Basically: Animal.__init__(self, name, species)
        # Could manually define them like but this is DUPLICATION!
        # self.name = name
        # self.species = species
        self.breed = breed
        self.toy = toy
        # Better is to first use the __init__ in Animal and then setup anything for Cat()
        # Can use this by writing: Animal.__init__(self, name, species), OR just use super()

    def play(self):
        print(f"{self.name} plays with {self.toy}")  # usually would use return instead of print




blue = Cat("Blue", "Scottish Fold", "String")
blue.play()
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)

# gandalf = Cat()
# gandalf.make_sound("meow")  # meow
# print(gandalf.cool)  # True
# print(Cat.cool)
# print(Animal.cool)
# print(isinstance(gandalf, Cat))
# print(isinstance(gandalf, object))