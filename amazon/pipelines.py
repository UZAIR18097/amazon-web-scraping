# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class AmazonPipeline(object):
    def __init__(self):
        # creates connection
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        # creates data base
        db = self.conn['amazon']
        # creates table
        self.collection = db['amazon_tb']

    def process_item(self, item, spider):
        #store the table
        self.collection.insert(dict(item))
        return item
