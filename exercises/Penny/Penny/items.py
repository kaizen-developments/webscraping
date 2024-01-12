# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#1. Start defining the items! < 10 minutes
class PennyItem(scrapy.Item):
    #Body of the class matches "(<item name> = scrapy.Field() \n)+.
    name = scrapy.Field()
    price = scrapy.Field()
    priceWithRespectToUnit = scrapy.Field()
    unit = scrapy.Field()
    sizeInUnits = scrapy.Field()