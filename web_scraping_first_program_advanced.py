"""
ADVANCED SCRAPING FIRST PROGRAM
Scrape through ALL pages and write to CSV

Order of Approach (I think):
1. Make request to main blog to get all page URLs
2. Get response back and send to BS
3. Use BS to navigate/extract/save all page URLs
4. Make request per page in blog
5. Get response back per page and send to BS
6. Use BS to navigate/extract title, url, date
7. Write all data to CSV


# KEY LEARNINGS:
1. soup.select(".class tag")  # List of all matches! Ex. soup.select(".pagination a")
2. pages[0].get("href") OR pages[0]["href"]  # /blog?page=n
3. time.sleep(10) to delay between requests
4. Call a function in another function: range(1, get_total_pages()+1)
5. soup.select("article a") returns a list of ALL articles on the site, regardless of pages

"""
# SECOND ATTEMPT:
import requests, time, csv
from bs4 import BeautifulSoup

def get_total_pages():
    r = requests.get("https://www.rithmschool.com/blog")
    soup = BeautifulSoup(r.text, "html.parser")
    last_page_elem = soup.select(".last [href]")
    total_pages = int(last_page_elem[0]["href"][-1])
    print(f"Total pages: {total_pages}")
    return total_pages

def get_page_urls():
    base_url = "https://www.rithmschool.com/blog?page="
    urls = [base_url+str(n) for n in range(1,get_total_pages()+1)]
    print(f"All URLs: {urls}")
    return urls 

with open("scrape_blog_all_pages_functions.csv", "a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "url", "date"])

    for page in get_page_urls():
        r = requests.get(page)
        soup = BeautifulSoup(r.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            title = article.find("a").get_text()
            url = article.find("a")["href"]
            date = article.find("time")["datetime"]
            csv_writer.writerow([title, url, date])
        
        time.sleep(5)
        print(f"Completed page: {page}. Waiting 5 seconds")



# FIRST WORKING SOLUTION
# import requests
# from bs4 import BeautifulSoup
# import csv
# import time


# # 1. Make request to main blog to get all page URLs
# r = requests.get("https://www.rithmschool.com/blog")

# # 2. Get response back and send to BS
# soup = BeautifulSoup(r.text, "html.parser")

# # 3. Use BS to navigate/extract/save all page URLs
# pages_elements = soup.select(".pagination a")
# number_of_pages = len(pages_elements) + 1  # home/first page doesn't have <a> tag so +1 to account for it
# base_url = "https://www.rithmschool.com/blog?page="
# links = [base_url+str(n) for n in range(1,number_of_pages+1)]
# page_numbers = [link[-1] for link in links]
# pages_urls_dict = dict(zip(page_numbers, links))

# # 4. Make request per page in blog -- Loop through pages
# for page in pages_urls_dict:
#     r = requests.get(pages_urls_dict[page])

# # 5. Get response back per page and send to BS
#     pages_soup = BeautifulSoup(r.text, "html.parser")
#     time.sleep(3)

# # 6. Use BS to navigate/extract title, url, date
#     articles_elements = pages_soup.find_all("article")

# # 7. Write all data to CSV
#     if page == '1':  # Create file and write headers
#         with open("scrape_blog_all_pages.csv", "w") as file:
#             csv_writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Date"])
#             csv_writer.writeheader()
#             for article in articles_elements:
#                 a_tag = article.find("a")
#                 title = a_tag.get_text()
#                 url = a_tag["href"]
#                 date = article.find("time")["datetime"]
#                 csv_writer.writerow({"Title": title, "URL": url, "Date": date})
#     else:
#         with open("scrape_blog_all_pages.csv", "a") as file:
#             csv_writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Date"])
#             # csv_writer.writeheader()  - Not necessary with append
#             for article in articles_elements:
#                 a_tag = article.find("a")
#                 title = a_tag.get_text()
#                 url = a_tag["href"]
#                 date = article.find("time")["datetime"]
#                 csv_writer.writerow({"Title": title, "URL": url, "Date": date})




# STUDENT SOLUTION W/ FUNCTIONS AND NESTED FOR LOOPS
# import requests, time, re
# from bs4 import BeautifulSoup
# from csv import writer
 
# sleep_time = 2
# home_url = 'https://rithmschool.com/blog'
 
# def get_last_page():
#     r = requests.get(home_url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     last_page_url = soup.find(class_='last').find('a')['href']
#     last_page = re.findall(r'\d+',last_page_url )[-1]
#     return int(last_page)
 
# def get_urls():
#     urls = []
#     for num in range(1, get_last_page() + 1):
#         url = f"{home_url}?page={str(num)}"
#         r = requests.get(url)
#         urls.append(url)
#         time.sleep(sleep_time)
#     return urls
 
# # newline='' removes the extra newlines that python 3 on windows is inserting for me
# with open('blog_data.csv', 'w', newline='') as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title","link","date"])
 
#     for url in get_urls():
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, 'html.parser')
#         articles = soup.find_all('article')
 
#         for article in articles:
#             a_tag = article.find('a')
#             title = a_tag.get_text()
#             link = a_tag['href']
#             date = article.find('time')['datetime']
#             csv_writer.writerow([title,link,date])
 
#         time.sleep(sleep_time)
#         print(f"URL {url} done")




# STUDENT SOLUTION TRY/EXCEPT WHILE LOOP
# import requests
# from bs4 import BeautifulSoup
# from csv import writer
 
# num = 1
# with open('blog_data.csv', 'a') as file:
#         csv_writer = writer(file)
#         csv_writer.writerow(['Title', 'URL', 'Date'])
#         while True:
#                 response = requests.get('https://www.rithmschool.com/blog?page='+str(num)) #returns response code/ .text returns html               
#                 soup = BeautifulSoup(response.text, 'html.parser')
#                 try:
#                         pageNo = int(soup.find(class_='page current').get_text())
#                 except AttributeError:
#                         print('You have reached the last page. Total no. of pages = ' + str(num-1))
#                         break
#                 articles = soup.find_all('article')
#                 for i in articles:
#                         a_tag = i.find('a')
#                         title = a_tag.get_text()
#                         url = a_tag['href']
#                         date = i.find('time')['datetime']
#                         csv_writer.writerow([title, url, date])
                                
#                 num += 1











# =============================== WORKING THROUGH SOLUTION (BELOW) / CLEAN SOLUTION ABOVE ========================

# # 1. Make request to main blog to get all page URLs
# response = requests.get("https://www.rithmschool.com/blog")

# # 2. Get response back and send to BS
# soup = BeautifulSoup(response.text, "html.parser")

# # 3. Use BS to navigate/extract/save all page URLs

# # pages = soup.find_all(class_="page")  # <span> level - not best
# #print(soup.select(".page a"))  # [<a href="/blog?page=2" rel="next">2</a>, ..., <a href="/blog?page=5">5</a>]
# #print(soup.select(".pagination a"))  # BEST!
# #print(soup.select(".page [href]"))  # [<a href="/blog?page=2" rel="next">2</a>, ..., <a href="/blog?page=5">5</a>]

# pages = soup.select(".pagination a")
# number_of_pages = len(pages) + 1
# #print(number_of_pages)
# # print(pages[0].get("href"))  # /blog?page=2  FINALLY!
# # print(pages[0]["href"])  # Same as above:  /blog?page=2
# hrefs = set([page.get("href") for page in pages])  # Has two page=2 entries so added set()
# #print([href[-1] for href in hrefs])  # ['4', '7', ...]

# # Sort of a cheating way since I'm not using hrefs:
# domain = "https://www.rithmschool.com/blog?page="
# links = [domain+str(n) for n in range(1,number_of_pages+1)]
# page_numbers = [link[-1] for link in links]
# # print(links)
# # print(page_numbers)  # ['1', '2', '3',...]

# # Create a Dict("page": page_number, "url": "https://....")
# pages_urls = dict(zip(page_numbers, links))

# # print(pages_urls["1"])
# # print(type(pages_urls["1"]))  # <class 'str'>
# # for page in pages_urls:
# #     print(pages_urls[page])  # https://www....1, 2, 3, ...

# #print(dict(pages_urls_zip))
# #print(pages_urls)

# # for i in pages_urls_zip:
# #     dict()

# # print(list(zip(page_numbers, links)))  # ('1', 'https://...1)
# # test_dict = {}.fromkeys(page_numbers, links)
# #print(test_dict)

# # for k, v in zip(page_numbers, links):
# #     print({"page": k, "url": v})

# # print(pages)
# # print(len(pages))  # 6
# # print(len(hrefs))  # 5

# # Attempt 1 -- Meh.
# # for page in pages:
# #     #print(page.find(""))
# #     print(page.find("a"))  # <a href="/blog?page=2" rel="next">2</a>
# #     # print(page.attrs)  # {'class': ['page', 'current']}
# #     # print(page.contents)  # ['\n', <a href="/blog?page...</a>, '\n"]
# #     # print(page.get_text())  # 1 , 2 , 3
# #     print(page.findChild("href"))  # None, <a href=...>, None, <a href=...>



# # 4. Make request per page in blog -- Use a loop?
# for page in pages_urls:
#     r = requests.get(pages_urls[page])
# # 5. Get response back per page and send to BS
#     pages_soup = BeautifulSoup(r.text, "html.parser")
#     time.sleep(5)

# # 6. Use BS to navigate/extract title, url, date
#     articles = pages_soup.find_all("article")

# REDUNDANT CODE (for article in articles... create a function instead!)
# def extract_write_article(articles):
#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag["href"]
#         date = article.find("time")["datetime"]
#         csv_writer.writerow({"Title": title, "URL": url, "Date": date})

# Possible function?:
    # def extract_write_article():
#     a_tag = article.find("a")
#     title = a_tag.get_text()
#     url = a_tag["href"]
#     date = article.find("time")["datetime"]
#     return 


# # 7. Write all data to CSV
#     if page == '1':  # Create file and write headers
#         with open("scrape_blog_all_pages.csv", "w") as file:
#             csv_writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Date"])
#             for article in articles:
#                 a_tag = article.find("a")
#                 title = a_tag.get_text()
#                 url = a_tag["href"]
#                 date = article.find("time")["datetime"]
#                 csv_writer.writerow({"Title": title, "URL": url, "Date": date})
#     else:
#         with open("scrape_blog_all_pages.csv", "a") as file:
#             csv_writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Date"])
#             # csv_writer.writeheader()  - Not necessary with append
#             for article in articles:
#                 a_tag = article.find("a")
#                 title = a_tag.get_text()
#                 url = a_tag["href"]
#                 date = article.find("time")["datetime"]
#                 csv_writer.writerow({"Title": title, "URL": url, "Date": date})