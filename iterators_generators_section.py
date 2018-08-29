'''
Objectives:
DEFINE AND UNDERSTAND ITERATOR VS. ITERABLE

ITERATOR - An object that can be iterated upon. An object which returns data,
ONE element at a time when next() is called on it. Think of it as anything we can
run a for loop on, but behind the scenes there's a method called next() working.

ITERABLE - An object which will return an ITERATOR when iter() is called on it.
IMPORTANT: A list is also just an iterable. The list is actually never directly
looped over. What actually happens is the for loop calls iter("HELLO"), which
returns the iterator that is then the loop will call next() on that iterator
over and over again until it hits the end!


UNDERSTAND THE ITER() AND NEXT() METHODS
ITER() - Returns an iterator object.

NEXT() - When next() is called on an iterator, the iterator returns the next ITEM.
It keeps doing so until it raises a StopIteration error.


Example:
"HELLO" is an iterable, but it is not an iterator
iter("HELLO") returns an iterator

for char in "Oprah" -- first the for loop calls iter("Oprah"). THEN, in order
for the "for" loop to loop through the iterator, it then calls the NEXT()
function




-Build our own for loop

-Define what generators are and how they can be used

-Compare generator functions and generator expressions

-Use generators to pause execution of expensive functions


'''
name = "Oprah"
#next(name)  # TypeError: 'str' object is not an iterator
print(iter(name))  # <str_iterator object at 0x108aaa668>

it = iter(name)
# for char in it:
#     print(char)

print(next(it))  # O
print(next(it))  # p
print(next(it))  # r


nums = [1, 2, 3, 4, 5]  # a list isn't an iterator but is ITERABLE!
# next(nums)  # TypeError: 'list' object is not an iterator
it2 = iter(nums)
print(it2)  # <list_iterator object at 0x10c7a4550>
