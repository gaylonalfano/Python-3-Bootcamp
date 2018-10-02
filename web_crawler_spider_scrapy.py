'''

http://books.toscrape.com/
Documentation:  https://doc.scrapy.org/en/latest/intro/tutorial.html

KEY LEARNINGS:
To execute:   scrapy runspider -o [file_to_save_to.csv/json] [name_of_python_file.py]
Our example: scrapy runspider -o scrapy_books.csv web_crawler_spider_scrapy.py

response.css() - returns a LIST. Kinda like soup.select()
extract_first() - Similar to get_text(). Since response.css() returns a LIST, you could use:
    response.css('title::text')[0].extract()   OR,
    response.css('title::text').extract_first()  *This avoids IndexError and returns None
article.css("h3 > a::attr(title)").extract_first()  # Gets the book title
response.follow(next, self.parse)  # This is recursion. 


'''

import scrapy

# Need to define a Class that inherits from scrapy.Spider)
class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com/']

    # Next, need to define the parse method. Scrapy makes the request automatically, then call parse
    # over and over on every single response that it gets back that we want to scrape.
    # The parse() method usually parses the response, extracting the scraped data as dicts and 
    # also finding new URLs to follow and creating new requests (Request) from them.
    def parse(self, response):
        # response refers to what we get back from the HTTP request
        # response.css is kinda like soup.select()
        for article in response.css('article.product_pod'):  # all articles that have class = product_pod
            yield {
                'price': article.css(".price_color::text").extract_first(), # saves the printed object. We want to do equivalent to: soup.find.get_text()
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
        # Next, we need to crawl/swap to other pages
        next = response.css(".next > a::attr(href)").extract_first()  # returns the value of that href (which is some URL)
        if next:
            yield response.follow(next, self.parse)  # This is called recursion calling parse within function parse.
            # Going to go through everything, what to do next, where to go. Goes until it can't find a next button then done. 
