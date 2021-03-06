'''
Reference:  https://docs.python.org/3/library/operator.html

Sample of magic methods:
__add__
__mul__
__missing__
__setitem__
__getitem__
__len__
__iter__
__reversed__
__contains__


Operator overloading?
__eq__, __ne__, __lt__, __gt__



8 + 2  # 10
"8" + "2"

What's happening in these examples? How does Python know how to interpret the +
operator differently in these cases? ANSWER: The first argument has a SPECIAL METHOD
that defines what to do with the + operator. The actual operation Python performs
is something like: x.__add__(y)

The + operator is shorthand for a special method call __add__() that gets
called on the first operand.

If the first (left) operand is an instance of int, __add__() does mathematical
ADDITION. If it's a string, it does string CONCATENATION.

Therefore, you can declare special methods on your own classes to mimic
the behavior of builtin objects, like so using __len__:

class Human:
    def __init__(self, height):
        self.height = height  # in inches

    def __len__(self):
        return self.height


Colt = Human(60)
len(Colt)  # 60


The most common use-case for special methods is to make classes "look pretty"
in strings. For example, the __repr__ method is one of several ways to provide
a nicer string representation:

class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name


dude = Human()
print(dude)  # "somebody"


The whole point is that there are many magic methods that are available.
'''
# from copy import copy
#
# class Human:
#
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def __repr__(self):
#         return f"Human named {self.first} {self.last} aged {self.age}"
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         '''refers to whatever comes first in the calc ( A + b )'''
#         if isinstance(other, Human):
#             return Human(first="Newborn", last=self.last, age=0)  # self.last or other.last
#         raise TypeError("You can't add that!")
#
#     def __mul__(self, other):  # Cloning humans. self is first operand, other is the second operand
#         '''__mul__ actually creates multiple REFERENCES to EXACT SAME OBJECT
#         If you really want to clone, then need to import/use COPY builtin function'''
#         if isinstance(other, int):
#             # Better:
#             return [copy(self) for x in range(other)]
#             # return [Human(self.first, self.last, self.age) for x in range(other)]
#         raise TypeError("You can't multiply that!")
#
#
#
# j = Human("Jenny", "Larsen", 47)
# k = Human("Kevin", "Jones", 49)
# # print(j)  # Human named Jenny Larsen
# # print(len(j))  # 47
#
# # print(j + k)  # Human named Newborn Larsen
# # print(j + 2)  # TypeError
#
# #print(j * 2)  # If you switch it to 2 * j, __mul__ will look for the int on the __mul__ method and doesn't find it
#
# triplets = j * 3
# triplets[1].first = "Jessica"
# print(triplets)  # all 3 changed to Jessica! That's because mul just creates REFERENCES. Need to use COPY
#
# # Kevin and Jessica having triplets!
# triplets2 = (k + j) * 3  # Cloning the Human "Newborn Jones" three times.
# print(triplets2)


'''GRUMPY DICT EXAMPLE - Overriding Dict. No need to define our own __init__() since we're inheriting 
from dict directly and WE'RE NOT PASSING DATA OR ATTRIBUTES. The dict__init__() will run instead, 
which means you don't have to specify it (since we're only adding methods and no other data/attributes).
The dict__init__() runs due to MRO.

The key takeaway is that special methods and inheritance allows for some cool things. For example, 
if you inherit from any builtin type (list, dict, etc.) or any other class someone else wrote,
you can run/call the parent's (super) special methods and expand/extend on them but still being
able to use the base special/magic methods.

'''
# class GrumpyDict(dict):
#     def __repr__(self):
#         print("None of your business!")
#         # return super(GrumpyDict, self).__repr__()  # Sort of like the super OF GrumpyDict, which is dict
#         return super().__repr__()  # this is dict's version of __repr__ {k:v, k:v, k:v}
#
#     def __missing__(self, key):
#         print(f"You want {key}? Well it ain't here!")
#
#     def __setitem__(self, key, value):
#         print("You want to change the dictionary?\nOkay fine...")
#         super().__setitem__(key, value)
#
#     def __contains__(self, item):  # Returns True/False
#         print(f"No {item} here! Scram!")
#         return False  # Even if it's in there! It's just grumpy :)
#
#
#
# data = GrumpyDict({"first": "Tom", "animal": "cat"})
# print(data)
# data['city']  # Error -- see def __missing__ method
# data['city'] = 'Austin'
# print(data)
# data.__contains__("dog")
# "city" in data

# d = GrumpyDict({"name": "Yoko", "city": "New York"})
# print(d)  # None of your business {"name": "Yoko", "city": "New York"}
# d["city"] = "SF"
# print(d)  # Why do you always have to change things? \nUgh fine, setting city to SF\nNone of your business

'''
SPECIAL METHODS TRAIN EXERCISE - Create a class Train with one attribute: num_cars
Also has two special/magic/dunder methods __print__ and __len__
'''
class Train:

    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return f"{self.num_cars} car train"

    def __len__(self):
        return self.num_cars

a_train = Train(4)
print(a_train)
print(len(a_train))

# b_train = Train("seven")
# print(b_train)
# print(len(b_train))
