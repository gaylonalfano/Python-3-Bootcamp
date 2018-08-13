'''
Write Python code that talks to websites, gets data from APIs, builds simple
apps that uses data from APIs, etc. If you like this stuff, check out web
development with Python.


# What happens when you type a URL in the URL bar:
1. DNS Lookup - It takes 'google.com' and it actually finds the correct IP address
for google.com. DNS Lookup is like a giant phonebook for the internet! It takes
domain names (google.com) and turns them into an IP address.

2. Computer makes an HTTP REQUEST to a server saying, "Hello server @ google.com, Colt
is looking for the homepage of google.com, can you give it to me?"

3. Server receives/processes the REQUEST and says, "Oh ok this person is looking
for google.com, did they search for anything? No? Okay, send them the homepage."

4. The server then compiles the homepage and sends it back/issues a RESPONSE.



# Describe the request/response cycle
Steps 2-4 above are what we call the request/response cycle. Send a request to
a server, and then the server sends something back to us. If you actually search
for "Salmon" on google.com, then at step 3, the server goes finds all the salmon
results in the google database and then build a different webpage but with all
the salmon details. Notice, it's the same place that your sending the request to
(google.com), it's just all the extra stuff that translates into a different/unique
HTTP REQUEST.

CLIENT sends a GET request to an IP address (172.217.9.142) to that SERVER. Then the
server, assuming everything is fine, sends you an HTTP RESPONSE containing everything
you asked for in a webpage with various STATUS CODES (okay, not found, forbidden, etc.).

Then the last step, the server sends something back in that RESPONSE, which is called
the RESPONSE BODY, and this is what we call HTML (it is what is sent back to your CLIENT
and rendered in your browser).

*Hit Cmd+Option+J in Chrome > Network Tab >



# Explain what a request or response header is, and give examples
HTTP Headers - are like meta data of the request. They are sent with both requests
and responses. The provided additional information about the request or response.

REQUEST Headers:
Accept -- Acceptable content-types for response (e.g. html, json, xml). Basically computers
way of saying these are the type of responses we will take back.
Cache-Control -- Specifies how the caching should behave
User-Agent -- Information about the software used to make the request

RESPONSE Headers:
Access-Control-Allow-Origin -- Specify domains that can make requests
Allowed -- HTTP verbs that are allowed in requests



# Explain the different categories of response codes
However, the most important part of the response are the STATUS codes.
Every request gets a response. Example status codes:
2xx - Success
3xx - Redirect
4xx - Client Error (your fault)
5xx - Server Error (not your fault)


# HTTP Verbs: Compare GET and POST requests (aka Request Verb or Request Method):
There are other verbs but these are the most fundamental requests we can make.

GET - Useful for retrieving data (not trying to write data). Think of it as just
browsing the web. Data can be passed in a query string. Should have NO side-effects.
Get requests can be cached, can be bookmarked (think of your bookmarks).

POST - Useful for writing data (trying to submit a new comment, or photo, updating, etc.).
You're actually sending something to the server that then HAS side-effects.
Data is passed in request body. Cannot be cached and cannot be bookmarked.




# API - Application Programming Interface
It's a version of a website intended for computers in order for it to talk to computers, etc.
For example, if you go to: www.reddit.com and then tack on /.json (www.reddit.com/.json) it's
the API version.

APIs allow us to get data from another application without needing to understand how the
application works, without having to be human. Can often transfer data back and forth in different formats.
Lots of examples of companies with APIs: GitHub, Spotify, Google, etc.

Ex. GitHubs API allows you to get code, make a new repo, etc. Spotify has an API you can write Python code
to retrieve your playlist.

The whole point is that we'll write Python code to send a request to a URL (eg. weather.com). For example,
all we want is design an app that displays the temperature in a city. An API just says, "Hey, I'm a computer,
we just want some information please send it back in a format we specify/care about." A couple of key formats are
json and xml. json is reining king nowadays. We're going to interact with websites that have APIs, a special
"back door" into a server that our code can take advantage of.

'''