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




"""