'''
What's a Query String?
A way to pass data to the server as part of a GET request.
http://www.example.com/?key1=value1&key2=value2

Fairly similar to a Python DICt.  It's a way to send data to a server to
get more information about the request.

Ex:  https://www.google.com/search?q=american+marten&oq=american+marten&aqs=chrome..69i57j69i60l3j69i65j69i60.3146j0j7&sourceid=chrome&ie=UTF-8

https://www.google.com/search?
q=american+marten
oq=american+marten
aqs=chrome..69i57j69i60l3j69i65j69i60.3146j0j7
sourceid=chrome
ie=UTF-8

Key point from above is this is additional info that's being sent as part of the request

So why do we care about sending additonal info to the server? A lot of times we make
an application that allows the user to tell us what they wish to search for.
For example using the dad jokes site: App that allows user to provide a joke topic (dog, car, etc.)

We're going to focus on how we can take this data and pass it into a QUERY STRING into
the request! Example with dad jokes, if you search using "flower"

Here's the syntax for passing a request using Query String:

import requests

response = requests.get(
    "http://www.example.com",
    params={
        "key1": "value1",
        "key2": "value2"
    }
)
'''

import requests
url = "https://icanhazdadjoke.com/search"
'''
API doc: https://icanhazdadjoke.com/api  > Search for dad jokes
page - which page of results to fetch (default: 1)
limit - number of results to return per page (default: 20) (max: 30)
term - search term to use (default: list all jokes)

If you don't use the params parameter, then you can do the same doing:
Ex: https://icanhazdadjoke.com/search?term=golf&limit=1

However, better is to pass params={"k
'''

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}  # "text/plain", "term": user_input
)

data = response.json()  # .json() returns a DICT
print(data["results"])  # Returns a list of dictionaries
# print(data['joke'])
# print(f"status: {data['status']}")