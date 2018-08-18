'''
# CLASS METHODS - These are pretty rare, not commonly used. Most you write are instance methods.
Class methods are methods (with the @classmethod DECORATOR) that are not concerned with instances,
but this class itself. Decorators are a little bit of Python magic or, "syntactic sugar", that
goes IN FRONT of a class method.

class Person():
    # ...

    @classmethod
    def from_csv(cls, filename):
        return cls(*params)  # This is the same as calling Person(*params)

Person.from_csv(my_csv)

'''


class User:  # Created the class but haven't used it yet. Need to create an instance of that class

    # import pdb; pdb.set_trace()
    active_users = 0  # Class attribute
    total_age = 0
    # if active_users == 0:
    #     average_age = total_age / (active_users + 1)
    # else:
    #     average_age = total_age / active_users


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        User.total_age += age
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