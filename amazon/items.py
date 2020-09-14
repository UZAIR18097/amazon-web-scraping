# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


# function to extract only price
def filter_price(value):
    if value.isdigit():
        return value


# function to extract values wihout \n
def remove_n(value):
    return value.replace("\n", '')


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_n)
    )
    author = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_tags,remove_n)
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )
    image_link = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_n)
    )
    stars = scrapy.Field()
