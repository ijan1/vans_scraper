# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

class VansPipeline:

    def open_spider(self,spider):
        self.file = open('shoes', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        shoes = ItemAdapter(item)
        if shoes.get('stock').get('4171073') != 0 or shoes.get('stock').get("4171074") != 0:
            self.file.write("has shoes")
        return shoes 
