# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PennyPipeline(object):
    #Define the mandatory "process_item" method for the pipeline class!
    #TODO: Create data from the PennyProducts that can be directly transformed into json format in a simple list!
    def process_item(self, item, spider):
        if isinstance(item, Article):
            article = item
            article['lastUpdated'] = article['lastUpdated'].replace('This page was last edited on', '')
            article['lastUpdated'] = article['lastUpdated'].strip()
            article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M.')
            article['text'] = [line for line in article['text'] if line not in whitespace]
            article['text'] = ''.join(article['text'])
            return article
