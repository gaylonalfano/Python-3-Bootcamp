# use the requests module. This is useful for web scraping/crawling, grabbing data
# from other APIs, etc. Were using HTTP protocol/schema so need to put that in the URL.
import requests

# url = "http://www.google.com"
# response = requests.get(url)
#
# print(f"Your request to {url} came back w/ status code {response.status_code}")

# Request Headers
response = requests.get(
    "http://wwww.example.com",
    headers={
        "header1": "value1", # please give me json, plaintext, etc.
        "header2": "value2"  # value represents the type of data we accept back
    }
)

# See headers.py