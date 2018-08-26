'''
METHOD RESOLUTION ORDER - Whenever you create a class, Python sets a MRO for that
class, which is the order in which Python will look for methods on instances of that class.
It's like a hierarchy. Pretty complex algorithm for how Python does this.

Three different ways of accessing the MRO for your class:
* __mro__ attribute on the class
* use the mro() method on the class
* use the builtin help(cls) method

Penguin.__mro__

(<class '__main__.Penguin'>, <class '__main__.Ambulatory'>,
<class '__main__.Aquatic'>, <class 'object'>)

Penguin.mro()
[<class '__main__.Penguin'>, <class '__main__.Ambulatory'>,
<class '__main__.Aquatic'>, <class 'object'>]

help(Penguin)
BEST for HUMAN readability -> gives us a detailed chain

=============

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
        Ambulatory.__init__(self, name=name)  # Need to pass in self when not using super()
        Aquatic.__init__(self, name=name)  # self and name are referring to Penguin and Penguin's name attribute


print(Penguin.__mro__)

print(Penguin.mro())

help(Penguin)



Online example:

class C(A, B):
    def __init__(self):
        print("entering c")
        for base_class in C.__bases__:  # (A, B)
             base_class.__init__(self)
        print("leaving c")


'''
# MRO in more detail

# class A:
#     # pass
#     def do_something(self):
#         print("Method Defined in: A")
#
#
# class B(A):
#     # pass
#     def do_something(self):
#         print("Method Defined in: B")
#         super().do_something()  # C! Not totally sure why...
#
#
# class C(A):
#     # pass
#     def do_something(self):
#         print("Method Defined in: C")
#
#
# class D(B, C):
#     # pass  # If only pass here, then order is: D, B, C, A
#     def do_something(self):
#         print("Method Defined in: D")
#         super().do_something()  # Refers to next thing in line, B
#
#     #    A
#     #   / \
#     #  B   C
#     #   \ /
#     #    D
#
# # help(B)
# # thing2 = C()
#
# help(D)
# thing = D()  # Order is D, B, C, A
# thing.do_something()  # ... in: D


class Mother:

    def __init__(self):
        print("MOM INIT")
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:

    def __init__(self):
        print("DAD INIT")
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass

    # def __init__(self, eye_color, hair_color, hair_type):
    #     pass
        # print("CHILD INIT")
        # super().__init__(eye_color, hair_color, hair_type)
        # # Mother.__init__(self, eye_color=eye_color, hair_color=hair_color, hair_type=hair_type)
        # # Father.__init__(self, eye_color=eye_color, hair_color=hair_color, hair_type=hair_type)



# help(Child)
m = Mother()
print(m.__dict__)
f = Father()
print(f.__dict__)
c = Child()
print(c.eye_color)





