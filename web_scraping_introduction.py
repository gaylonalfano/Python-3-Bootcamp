"""
PREVIOUS NOTES FROM HTTP_INTRODUCTION:

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


======================================================================================================

WEB SCRAPING INTRODUCTION
Potential uses - 

Scrape government sites? Competitor sites? Internal corporate

DEFINE WHAT WEB SCRAPING IS AND THE ISSUES SURROUNDING IT
Scraping involves programmatically grabbing data from a web page. They have data. Usually in HTML.
Sometimes it comes in the form of an API where we can get JSON data. We can still write code
to scrape the HTML. You can write code to scrape the data. If they don't have a nice API, you can
write Python to REQUEST this webpage. You have to ID where the info you want is located in the 
page source code. Ethically could be grey but you want to programmatically grab the data instead 
of lots of manual copying/pasting.

*Three general steps:
1. Download
2. Extract
3. Profit

Is it ethically OK? 
Some websites don't want people scraping them. Best practice: consult the robots.txt file
If making many requests, time them out. If you're too aggressive (making too many requests), your IP 
could get blocked. The robots.txt file will tell you want the site allows/disallows.
Scrape IMDB for all directors in England. FIRST, you'd want to consult their robots.txt file located 
at:  www.imdb.com/robots.txt  Here's an example:

User-agent: Slurp
Crawl-delay: .1

Another example:
User-agent: *
Allow: /
Sitemap: https://www.rithmschool.com/sitemap.xml.gz


HTML/CSS CRASHCOURSE: 
Typically you create one file for HTML and another file for your CSS code. Then you place references to 
your CSS file within the HTML file. But for the sake of the overview, we embedded it all within a single
file (see: html_css_crashcourse.html). Commonly things are styled using CLASSES and IDs. 

IDs: 
With CSS styles, anything you place in style for say, li (list items), will change all of the other 
li on the page the same. If you want to single-out an li to be something other than what the style is set as, 
then you can add a simple id (<li id="first">Flour</li). **NOTE** IDs are only meant to be used ONCE. 
You can move it around but you need to create another unique ID if you have others to add.

CLASSES:
Allows us to create a grouping/class of items that are styled similarly, so you apply changes to multiple items.
This matters because we can use classes to help us identify info we want to scrape from a page. For example,
on Craiglist they may have a tag, say a paragraph tag: <p class="apt-details"></p>. This can refine our search
to select things using Beautiful Soup because we know that CLASSES use a "." in front (.green).



<!DOCTYPE html>
<html>
<head>
    <title>A Bread Recipe</title>
    <style type="text/css">
        h1{
            color: purple;
            background: yellow;
        }
        li {
            color: red;
            font-size: 20px;
        }
        #first {
            color: blue;
        }
        .green {
            color: teal;
        }
    </style>
    
</head>
<body>
    <h1>SF Sourdough Loaf</h1>
    <em>written by Colt Steele</em>
    <h3>Ingredients</h3>
    <ul>
        <li id="first">Flour</li>
        <li>Water</li>
        <li>Yeast</li>
        <li class="green">Yeast</li>
        <li class="green">Yeast</li>
    </ul>
</body>
</html>




USE THE REQUESTS AND BEAUTIFULSOUP MODULES TO PARSE HTML
Actual name is bs4 instead of Beautiful Soup. Key getting started items:
1. To extract data from HTML, we'll use Beautiful Soup
2. Install it with pip (or conda)
3. Beautiful Soup lets us navigate through HTML with Python
4. BS does NOT download HTML! For this, we need the REQUESTS module!

PROCESS OVERVIEW:
Essentially, say we're scraping IMDB spacing out requests by 3 secs. You would use the REQUESTS
module to send a GET request to one page. Get the data back. Then take the HTML that comes back
and send it to Beautiful Soup and then extract whatever information I want. Maybe I'm trying to
extract links that I can crawl across and then send a further request to every link that I get 
back to say, Danny DeVito's page. And then every link we get back from Danny DeVito's page we're 
then going to further scrape and then keep going.



EXPLAIN SOME COMMON TECHNICAL PROBLEMS WITH WEB SCRAPING




EXPLORE OTHER TOOLS THAT CAN INTERACT WITH WEB PAGES






"""
import bs4

