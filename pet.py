'''
# CLASS ATTRIBUTES (*see pet.py)
Class attributes are defined only ONCE. It lives on the class itself and they're shared by all instances.
These class attributes/methods are used far less often vs instance attributes/methods. For example,
let's keep track of how many users have been created, or how many are currently online, etc.
These attributes you place up at the top of the class before all the instance methods, attributes.
You can refer to class variables via the individual instances but for now, let's use User.active_users

Common use cases for class attributes:
-Keeping track of things (active users, how many instances been made, the average of all of them, etc.
-Create validations (see pet.py -- allowed pets list). Don't want a person to change a species.
-If possible, you want to put your attributes only in the needed function

We can also define attributes directly on a class that are shared by all instances of a class and
the class itself. Example:
cat.name ("Blue")
dog.name ("Wyatt")
Pet.allowed (['cat', 'dog', 'fish', 'rat', 'pig'])

***BUT, cat and dog both have an attribute called allowed as well! They are NOT unique (use id(cat.allowed))
cat.allowed (['cat', 'dog', 'fish', 'rat', 'pig'])
dog.allowed (['cat', 'dog', 'fish', 'rat', 'pig'])


Class User:

    active_users = 0

    def __init__(self, ....)


Print(User.active_users)  # This is a class attribute you're printing


Create a new Pet class - name, species, etc.
Going to create a list of permitted pets (validation)

However, let's say we want to prevent a user from changing dog.species = 'tiger'.
This is when DECORATORS are handy but that comes later. For now, we could create
a method to set the allowed species.
'''


class Pet:

    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:  # Could use self.allowed (see below) but Pet.allowed preferred
            raise ValueError(f"You can't have a {species} pet.")
        self.name = name
        self.species = species

    def set_species(self, species):  # This method is preferred over simply typing cat.species = "whatever"
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet.")
        self.species = species


#tiger = Pet("Tony", "tiger")
cat = Pet("Blue", 'cat')
dog = Pet("Wyatt", "dog")

print(cat.species)  # cat

#cat.set_species("tiger")  # Error
print(cat.set_species("rat"))

Pet.allowed.append("pig")  # None
print(Pet.allowed)  # [ ..., "pig"]

cat.set_species("pig")
print(cat.species)  # pig

print(cat.allowed)
print(dog.allowed)

# These allowed attributes are NOT unique! Point to the exact same attribute! See below
print(id(cat.allowed))
print(id(dog.allowed))
print(id(Pet.allowed))

# However, if you wanted you could set an instance attribute allowed to be unique by:
cat.allowed = ['tiger', 'bear']
print(cat.allowed)  # ['tiger', 'bear']
print(Pet.allowed)  # ['cat', 'dog', 'fish', 'rat', 'pig']
print(dog.allowed)  # (['cat', 'dog', 'fish', 'rat', 'pig'])
