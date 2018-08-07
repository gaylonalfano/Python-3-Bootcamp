'''
__len__() built-in method

Essentially when you start creating your own classes, you can specify what len() will do
by changing the __len__() function. Here's an example:

Class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50  # In this case, anytime the SpecialList() is called and len is ran, it'll = 50

l1 = SpecialList([1, 333, 442, 2, 1, 558])
l2 = SpecialList(1, 3, 2, 5])

print(len(l1))  # 50
print(len(l2))  # 50

'''
len({'a': 1, 'b': 2, 'c': 3})  # 3 -- number of key, value pairs

'hello'.__len__()  # "dunder" name
[1, 2, 3].__len__()