"""
FileI/O - JSON Pickling!

It's just another data format, like CSV. It's anothe rway of 
representing data. JSON was created to send JS code from one PC to another
over the web. It's now all over the place. Python even has a module called json
that we can import. 

json.dumps() -- formats a python object as a STRING of JSON. It returns a STRING!
This means that None will be changed to null, single quotes will change to
double quotes, tuples will be turned to lists. Otherwise, it's basically the same.

Once in JSON, you could save it to a file by using file.write just using json.dumps(),
or create an API, etc. for a Java front end or backend could read. 

However, this only works easily with BUILT-IN types . If we try to do it with a 
custom class, it's much harder.

*** SCROLL DOWN FOR JSONPICKLE! ***

"""
# import json

# j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# print(j)  # This is easy since it's converting built-in types.

# Much harder if trying to do a custom class. It doesn't really know what to do.
# What you could do is:

import json

# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
# c = Cat("Charles", "Tabby")

# j = json.dumps(c.__dict__)  # {"name": "Charles", "breed": "Tabby"}

"""
JSONPICKLE
If you want to be able to look at your pickled data, JSON isn't going to cut 
it for us. Instead, you can look at jsonpickle module. Library that is like pickle
but instead it works with JSON. Serializes/de-serializes complex data into JSON.

jsonpickle.encode(object)
jsonpickle.decode()

"""
import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
#c = Cat("Charles", "Tabby")

#frozen = jsonpickle.encode(c)
#print(frozen)  # {"py/object": "__main__.Cat", "breed": "Tabby", "name": "Charles"}

# The __main__.Cat is useful. Let's first store into a file instead:
# with open("cat.json", "w") as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)
    # The cat.json file now has: {"py/object": "__main__.Cat", "breed": "Tabby", "name": "Charles"}

# Next, the cool thing is when we want to DECODE (be sure to comment out ENCODE!):
with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)


