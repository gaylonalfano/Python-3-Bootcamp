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

Hi Alan,

Good question. So the only reason that the Animal class has a name attribute is because of the Animal init method.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
If we take a step back from Inheritance and just focus on simple OOP for a second...The only way an Animal instance gets a name and a species if when __init__  is called and we pass in the information.  When we create a new Animal like this:

fish = Animal("Bubbles", "Goldfish")
Python automatically calls the Animal __init__  method behind the scenes, and it passes in "Bubbles" as name and "Goldfish" as species.  Then inside of __init__ we are able to set:

self.name = name
self.species = species
So just to reiterate, the only way to set a name and species is by calling __init__.  It just happens that Python takes care of that for you when you call:

Animal("Bubbles", "Goldfish")
Now on to an example with inheritance...If we have a Cat class and want it to take advantage of the attributes defined in the parent Animal class, we have to manually call the Animal __init__ method.

In order for an instance of Animal or Cat to have a name or species attribute, the Animal init method must be called.  It doesn't do anything on its own just sitting there inside the init method.  Any child classes like Cat or Dog, etc. do not automatically inherit name and species.  They do inherit the method named init, but it still has to be called in order to initialize name and species.

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="cat")
        self.breed = breed
The first line def __init__(self, name, breed)  simply says that the Animal init method should accept 2 parameters, name and breed. You can name those whatever you want. At this point, they are not attributes on the instance of Cat.  We're just saying that init should accept two arguments.  It might be easier to understand what's happening if we change the code to this:

class Cat(Animal):
    def __init__(self, first, second):
        super().__init__(first, species="cat")
        self.breed = second
Next we call super().__init__(first, species="cat") which just passes along the first argument as well as a default "cat" species to the Animal __init__ method.  Then, that's where breed and species are actually initialized as attributes:

class Animal:
    def __init__(self, thing1, thing2):
        self.name = thing1
        self.species = thing2
I changed some of the parameter names to make it clearer that they don't mean anything on their own.

Let's try walking through it step by step and tracing values as we go along. Suppose I called:

kitty = Cat("Monty", "Maine Coon")
Here's the order of things that happen:

1. Inside Cat.__init__, first  is "Monty" and second  is "Maine Coon".

2. When it calls super().__init__(first, species="cat") It's really calling super().__init__("Monty", species="cat")  .

3. Then, inside of the Animal __init__, thing1  is equal to "Monty" and thing2  is equal to "cat".

4. Finally, self.name  and self.species  are set to those 2 values.

5. Then, back in the Cat __init__, self.breed  is set to the value of second  which is "Maine Coon"

So at the end of the day, remember that attributes are not inherited from a parent class unless we run the __init__ method of the parent class.  All methods are inherited by a child class, but you still have to call the method in order to run the code inside of it.  So we have to actually call super().__init__ and pass in the correct data in order to get the code inside of Animal.__init__ to run.

Colt







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