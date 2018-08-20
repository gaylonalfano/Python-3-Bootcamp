'''
__repr__method is one of several ways to provide a nicer string representation of an instance,
so that when print or turn a class into a string, we can control what it looks like. There are
also several other dunders to return classes in string formats (__str__ and __format__), and
choosing one is a bit complicated! Think of when we print a list or dict, the results are in
a nice format that we can read. But in truth, behind the scenes, that list or dict are just
instances of their respective classes so without __repr__, when you print() them they would
look ugly (<xxxxx.Dict object at 0980982sx0>). __repr__ just gives us a nice readable format.

Without __repr__ print(tom)  # <__main__.User object at 0x10df32eb8>
With __repr__  print(tom)    # Tom is 89


class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name

dude = Human()
print(dude)  # "somebody"
colt = Human(name='Colt Steele')
print(f"{colt} is totally rad (probably)")


'''

class User:  # Created the class but haven't used it yet. Need to create an instance of that class

    # import pdb; pdb.set_trace()
    active_users = 0  # Class attribute

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."
        #  print(cls)  # Is the class User itself, not some instance of the class

    @classmethod
    def from_string(cls, data_string):  # Remember cls is User class itself
        first, last, age = data_string.split(",")
        # cls("Jon", "Stones", 64)
        return cls(first, last, int(age))  # Creates a new user. cls() is like User()

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        # Used to initialize the data for each user

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1  # Remember there is only ONE User.active_users
        return f"{self.first} logged out."

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


# user1 = User("Joe", "Smith", 68)  # This instantiates a new User class object.
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user1 = User("Joe", "Smith", 68)  # This instantiates a new User class object.
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user1.display_active_users() -- Same as below but preferred to use class name instead (User.display...)
# User.display_active_users() # <class '__main__.User'> **Don't have all the numbers at the end like instances

tom = User.from_string("Tom,Jones,89")

j = User("Judy", "Steele", 18)
print(j)  # With __repr__ returns "Judy is 18"
j = str(j)  # Even when converting to str(), __repr__ is called  "Judy is 18"

# print(tom)
# print(tom.first)
# print(tom.full_name())
# print(tom.age)
# print(tom.birthday())
# print(tom.age)