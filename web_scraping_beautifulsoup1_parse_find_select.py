"""
BEAUTIFUL SOUP BASICS

Use BS to extract from HTML code. BUT it does NOT download HTML for us! We have to manually get the
data. BS 

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

The point is that BS doesn't download the HTML!
"""
# Example: Going to begin  with mocked HTML and a variable html = " ... "

from bs4 import BeautifulSoup

# Let's suppose that we got this back after making a REQUEST:
# Need to INSTANTIATE an instance of Beautiful Soup with our HTML string:
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""


'''
PARSING AND NAVIGATING HTML:
We have to initialize BS and Parse and Navigate the HTML. HTML comes back as a 
giant string. We pass the string to BS. It goes through to parse and it saves to a variable.
We can then use this parsed HTML and navigate through it.

Ways to navigate:
-By Tag Name: paragraph tags, achor tags, H1. etc.
-Using find - returns ONE maching tag item
-Using find_all - returns LIST all matching tags
-Attributes - find_all(attrs={"data-example": "yes"})
    -source for an image
    -href for an anchor tags
    -class_=, id=, tag name, etc.
-Use CSS Selectors:
    -select - ALWAYS returns a LIST of elements matching a CSS selector
    SELECT CHEATSHEET:
        Select by a tag name of div: "div"
        Select by attribute data-example: "[data-example]"
        Select by id of foo (id name): "#foo"
        Select by class of bar (class name): ".bar"
        Select by children (p is the child): "div > p"
        Select by descendents (descend from div): "div p"


When we parse HTML, BS takes that giant string and takes each individual tag and
turns it into its own object. BS then puts them all together into the main variable
SOUP, which contains all the instances of elements. 
'''

soup = BeautifulSoup(html, "html.parser")
# USING FIND/FIND_ALL
# print(soup)  # looks just like HTML but it's not class STR! It's an instance of BS!
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup.body)
# print(soup.body.div)  # There are 2 div, but this only returns 1st div
# print(soup.find("div"))  # Same as body.div
# print(soup.find_all("div"))  # returns LIST all "div" elements
# print(len(soup.find_all("li")))  # 3
# print(soup.find(id="first"))  # Returns that div. Use find() since only one id
# print(soup.find_all(class_="special"))  # NOTE "_" for class_ since class in keyword
# print(soup.find_all(attrs={"data-example": "yes"}))  # LIST [<h3 ..., <div ...]

# USING SELECT (CSS Selectors)
print(soup.select("#first"))  # same as soup.find(id="first") BUT returns LIST!
print(soup.select("#first")[0])  # same as soup.find(id="first")
print(soup.select(".special"))  # same as soup.find_all(class_="special")
print(soup.select("div"))  # same as soup.find_all("div")
print(soup.select("[data-example]"))  # same as soup.find_all(attrs={"data-example": "yes"})

d = soup.select("[data-example]")

#print(d)

"""
ACCESSING DATA IN ELEMENTS:
Up to now we've learned to parse and select elements. Let's say we want to 
grab the temperatures from a weather website. Can use the following ways to
access data:

get_text - access the INNER text in an element (get the degree!)
name - retrieve tag name of given element
attrs - dictionary of attributes we can access
brackets - Can also access attribute values using brackets!

See the access_data file!!!!
"""