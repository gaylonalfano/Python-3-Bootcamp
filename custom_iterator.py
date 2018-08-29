'''
Creating a custom iterator. Need to use __iter__ and __next__ TOGETHER
in your custom iterator class or it will not work! Normally


'''

class Counter:
    def __init__(self, low, high):
        #self.low = low
        self.current = low  # Changed after we added __next__ below
        self.high = high

    def __iter__(self):  # Need to call this and whatever it returns must be an ITERATOR. iter() won't work w/o it.
        # return iter("hello")  # Just an example of functionality. This actually works since it's an iterator
        # What you need is to return self.
        return self  # if you return self you MUST add __next__ method in your class!

    # In order to use a For Loop, it needs to be an ITERATOR that can then call next() on it
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

    # COULD TRY TO REPLICATE RANGE() BY ADDING A STEP FUNCTIONALITY


c = Counter(0, 10)
iter(c)

for x in c:
    print(x)

#
# for n in Counter(50, 55):
#     print(n)

# Expect it to print 50, 51, 52, ...