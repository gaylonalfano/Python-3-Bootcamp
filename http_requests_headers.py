import requests
url = "https://icanhazdadjoke.com/"

#response = requests.get(url, headers={"Accept": "text/plain"})  # You won't always get plain text

# headers = "Accept": "application/json"
# Even better than plain text is JSON (Javascript Object Notation).
# It was historically used to request JS, etc. But Python can convert
# to Python code easily.

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()  # .json() returns a DICT
print(data['joke'])
print(f"status: {data['status']}")
#print(response.text)  # Returns a STR

'''
Running .json turns it into Python so then you can use that dictionary.
It's better to request json:

"story1": "terrorist attack",
"story2": "Tiger wins Masters!"

'''

