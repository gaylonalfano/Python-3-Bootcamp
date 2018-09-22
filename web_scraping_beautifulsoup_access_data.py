"""
PARSING AND NAVIGATING (reference):
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

===========================================

ACCESSING DATA IN ELEMENTS:
Up to now we've learned to parse and select elements (see parse_select file). 
Let's say we want to grab the temperatures from a weather website. Can use 
the following ways to access data:

get_text - access the INNER text in an element (get the degree!)
name - retrieve tag name of given element
attrs - dictionary of attributes we can access
brackets - Can also access attribute values using brackets!

"""
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
soup = BeautifulSoup(html, "html.parser")
d = soup.select(".special")
print(d)