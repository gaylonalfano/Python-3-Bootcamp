"""
ACCESSING DATA IN ELEMENTS (reference):
Up to now we've learned to parse and select elements (see parse_select file). 
Let's say we want to grab the temperatures from a weather website. Can use 
the following ways to access data:

get_text() - Commonly used! Access the INNER text in an element (get the degree!). It will
    return text if it's there, otherwise it will return nothing (won't error)
    Ex. el = soup.select(".special")[0]  # first element of class special
       print(el)  # Instance of ELEMENT class. <li class="special">This list item is special.</li>
       print(el.get_text())  # This list item is special.

name - NOT a method. Retrieve tag name of given element (li, ol, meta, etc.)
    Ex. for el in soup.select(".special"):
            print(el.name)  # meta, li, li

attrs - dictionary of attributes we can access
    Ex. for el in soup.select(".special"):
            print(el.attrs)  # DICT k,v pairs of each item.

brackets - Can also access attribute values using brackets!
    Ex. for el in soup.select(".special"):
            print(el.attrs["class"])
        
        # Print out:
        meta
        {'charset': 'UTF-8', 'class': ['special']}  
        li
        {'class': ['special', 'super-special']} -- list bc elems can have more than one class

print(soup.find("h3").attrs["data-example"])  # yes
attr = soup.find("h3")["data-example"]  # yes  same as above
print(attr)  # yes
print(soup.find("div")["id"])  # first
print(soup.find("div").attrs)  # DICT {'id': 'first'}

======================================================

NAVIGATING WITH BEAUTIFUL SOUP
It means having a tag and finding elements relevant to that tag or that element.
So if we have an li, I can ask BS to find the parent of li, or parent of the next 
decendent of li, or to find the next sibling of that li, etc.

TWO MAIN WAYS TO DO THIS:
1. Via Tags - ATTRIBUTES! We'll be using attributes (not methods!) called:
    parent / parents - OUT a level
    contents - IN a level
    next_sibling / next_siblings - SAME level

2. Via Searching - METHODS!
    find_parent() / find_parents()
    find_next_sibling() / find_next_siblings()
    find_previous_sibling() / find_previous_siblings()

"""
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# NAVIGATING VIA TAGS:
#soup = BeautifulSoup(html, "html.parser")
# Select the body element: soup.body OR soup.find("body")
#data = soup.body.contents  # LIST of all the tags. Each is an object and "\n" chars!
#data = soup.body.contents[1]  # SILLY. But for first child/decendent <div id=.... </div>

# Siblings level
#next_sibling = soup.body.contents[1].next_sibling  # "\n" 
#next_sibling = soup.body.contents[1].next_sibling.next_sibling  # <ol> finally!

#print(soup.select(".super-special"))  # [<li class="special super-special">This list item is special.</li>]
#print(soup.find(class_="super-special").parent.parent)  # .parent = <ol>; .parent.parent = <body>
#print(soup.select(".super-special").parent)  # AttributeError: 'list' object has not attribute 'parent'


# NAVIGATING VIA SEARCHING:
soup = BeautifulSoup(html, "html.parser")
print(soup.find(id="first").find_next_sibling())  # SKIPS "\n"! Straight to <ol>
#print(soup.find(id="first").next_sibling)  # "\n"!!
print(soup.find(id="first").find_next_sibling().find_next_sibling())  # <div data-example...>
print(soup.find_all("div")[-1].find_previous_sibling())  # Last div. OR...
print(soup.select("[data-example]")[-1].find_previous_sibling())

# Skip siblings by adding arguments to find_next_sibling()
print(soup.find(class_="super-special").find_next_sibling(class_="special"))  # <li class="special">
print(soup.find("h3").find_parent())  # <div>
print(soup.find("h3").find_parent("body"))  # <body>

#help(BeautifulSoup)