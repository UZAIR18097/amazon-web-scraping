# amazon-web-scraping
I have created amazon web scraping project using scrapy where I extracted important information from Amazon bookstore.
I scraped information like Name of the book, Author name,Price of the book,number of stars and imagelink of the book.The spider is placed in amazon/spiders/amazon.
I used User Agent as Middle ware as Amazon does not allow scraping their website easily.
Finally the extracted from website is exported into MongoDB.The code is placed in the Pipelines.py. I have used different concepts like Pagination,Object Orientated Concepts for coding
