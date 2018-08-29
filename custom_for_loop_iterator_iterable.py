# Custom For Loop

'''
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
It keeps doing so until it raises a StopIteration error. It's actually using a
try/except block until it reaches the end and raises the StopIteration error.

'''

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
    # Need to add in try/except block to stop error from displaying to user
        try:
            # Would be nice to add some functionality to it (sum, mul, etc.) other than just print
            # print(next(iterator))
            i = next(iterator)
            func(i)
        except StopIteration:
            # print("End of loop")
            break
        # else:  Another syntax is to do the func() call in the else statement
        #     func(i)

def square(x):
    print(x**2)  # If you only use RETURN, then it won't PRINT




#my_for("hello")
my_for([1, 2, 3, 4], square)  # 1, 4, 9, 16
my_for('lol', print)
