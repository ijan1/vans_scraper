import scrapy
from scrapy.item import Item
import json
import re

class VansSpider(scrapy.Spider):
    name = "checkers"

    start_urls = [
            "https://www.vans.co.uk/webapp/wcs/stores/servlet/VFAjaxProductAvailabilityView?requestype=ajax&storeId=10158&langId=-11&productId=4166906&requesttype=ajax"
            ]

    def parse(self, response):
        stock = response.xpath('//body').get()
        stock = re.sub("<body><p>|</p></body>", "", stock)
        stock = re.sub(",\"attr.*", "}", stock)
       # with open('shoes.json', 'w') as f:
       #     f.write(stock)
        stock = json.loads(stock)
        yield stock
