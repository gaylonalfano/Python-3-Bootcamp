'''
# CLASS METHODS - Commonly these are used when you are actually creating a new instance of a class.
These are pretty rare, not commonly used. Most you write are instance methods.
Class methods are methods (with the @classmethod DECORATOR) that are not concerned with instances,
but this class itself. Decorators are a little bit of Python magic or, "syntactic sugar", that
goes IN FRONT of a class method.

class Person():
    # ...

    @classmethod
    def from_csv(cls, filename):
        return cls(*params)  # This is the same as calling Person(*params)

Person.from_csv(my_csv)


Class methods can be placed anywhere really. When you use @classmethod, Python automatically
passes the class 'cls' into the class method.

    @classmethod
    def some_method(cls):
        ...


Remember dict.fromkeys? Well this is a class method.
dict.fromkeys(['name', 'age', 'city'], 'unknown')

This generates a new instance for us by calling the dict class. We're going to do the same
thing with User and it will return a new User instance. Pretend we have a CSV file like:

Sample CSV file:
"Tom, Jones, 89"
"Sue, Prichett, 12"

But if we wanted to add a method to our class to handle/import this data where it could
create a new instance like this: User("Sue, Prichett, 12"). Example:

@classmethod
def from_string(cls, data_string):  # Remember cls is User class itself
    first, last, age = data_string.split(",")
    # cls("Jon", "Stones", 64)
    return cls(first, last, int(age))  # Creates a new user. cls() is like User()

Again, only write class methods if you do NOT need access to any data about the instances
or particular instance, and you're doing something on the entire class level
(like creating a new instance of the class). So if you have data coming in one way or you
need to validate data, you need to do something BEFORE a user (or any class) is created.

So why add this class method when we have the __init__ method to create a new instance?
Here's Zarko's opinion:

"We don't have to use it, it just enhances the functionality of our User class, allowing
us to pass a single string argument and create a user from it, as I mentioned above.
If we didn't use from_string method, we would have to pass the 3 arguments that correspond
to the __init__ method parameters, and not a single string as the only argument."

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
print(tom.first)
print(tom.full_name())
print(tom.age)
print(tom.birthday())
print(tom.age)