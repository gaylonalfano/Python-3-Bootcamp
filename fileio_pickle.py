"""
PICKLING - The process whereby a Python object hierarchy is converted nto a byte stream.
Use the pickle module. You pickle it and put it in a jar. You place it in a special
pickle file (converted to a byte stream). Can unpickle and it will be turned back into
whatever it was before.

So, say you're running the application (poker game) and you want to SAVE THE STATE 
of the poker game before shutting it down. You could use CSV, but could get complicated. 
Instead, we can use pickling it by serializing the data into a byte stream. 

PICKLING:
with open("file_name.pickle", "wb") as file:
    pickle.dump(object or (tuple of objects), file)

**Note that when writing, you need to use "wb" write binary mode
**When unpickling, you need to use "rb" read binary mode

UNPICKLING - **BE CAREFUL** Whenever you unpickle it's immediately being called
So if there's bad code it will execute, it could cause problems.

with open("file_name.pickle", "rb") as file:
    pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())

"""
import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

# blue = Cat("Blue", "Scottish Fold", "String")

# Now say we want to store away blue the Cat class object. This is where pickling comes in.
# Can pass multiple objects in a tuple ((blue, rusty)); (zombie_blue, zombie_rusty)

# with open("pets.pickle", "wb") as file:
#     pickle.dump(blue, file)

# pets.pickle output is all in binary 

# Next, if you want to restore/bring back then:
with open("pets.pickle", "rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)  # Blue is a Cat
    print(zombie_blue.play())  # Blue plays with String
        