'''
Goal is to model a typical permission setup on a website (Reddit, blog, etc.).
Have a hierarchy of users (users, moderators, admin).


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
    
class Moderator(User):  # Save lots of duplication by using inheritance
    total_mods = 0

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods."

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)  # same as super(Moderator, self).__init__(...)
        self.community = community
        Moderator.total_mods += 1
        
    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"


u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)

jasmine = Moderator("Jasmine", "O'Connor", 61, "Piano")  # This still updates active_users since Moderator calls User __init__ with super()
jasmine2 = Moderator("Jasmine", "O'Connor", 61, "Piano")  # This still updates active_users since Moderator calls User __init__ with super()
print(User.display_active_users())
print(Moderator.display_active_mods())



# print(jasmine.full_name())
# print(jasmine.community)

'''
ROLE PLAYING GAME

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = int(hp)
        self.level = int(level)
        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        
    def speak(self):
        print("I heard there were monsters running around last night!")



'''
