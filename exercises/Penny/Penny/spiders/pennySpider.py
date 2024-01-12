
#1. Provide a list of start_urls and allowed_domains!

#2. Provide further instructions on which links to follow or ignore, in this case allow all URLS  that match the regular expression '.*'!

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PennyItem

class PennySpider(CrawlSpider):
    #1. Provide a list of start_urls and allowed_domains!
    name = 'pennySpider'
    allowed_domains = ['foodora.hu']
    start_urls = [
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/54575b19-1ec5-45cb-9086-c6997bf62711",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/e471d46d-38a2-4089-93b3-616c7bd2815b",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/2015f43e-c2a8-4b9e-a6d1-ec33b445d9a5",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/10f84d32-de1c-4da8-bd3b-70f5532f51ab",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/6797a726-4119-4aac-90f2-ed0a0e3531c0",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/85c056c9-d1d3-4ada-83b1-d0e79c5aeece",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/e1429552-b8cc-458b-9633-0fc8e46c99b1",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/f44a0e18-2f38-40ae-b25e-f8c9fe2503c2",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/9cacdcdf-58e8-438b-994e-83a27ab13e17",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/b410e482-de49-439f-b3e6-b064c5e72ea3",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/67e95196-4fb4-441f-bf74-24454f8d13f6",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/52b36a55-8b2f-49da-bfd3-486325fb2105",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/5986e6c7-f968-40a1-8679-116ae5e93089",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/cd4b01ac-06da-4529-a2be-43894677bcd6",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/category/5986e6c7-f968-40a1-8679-116ae5e93089",
        "https://www.foodora.hu/shop/bsav/penny-szolnok-szechenyi-istvan-krt/view-all/dce95910-fb1b-4946-807e-bba490d4cf43.374ea2a2-9fd3-4ae9-9d46-08e29e933d05.a376be6116048069f7d4fb02096f1b31"]
    #2. Provide further instructions on which links to follow or ignore, in this case allow all URLS  that match the regular expression '.*'!
    rules = [
        Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)
        ]
    #Extract the raw data, doing as little processing as possible, to pass it to the pipeline!
    #TODO:Find all the parameters of parse_items, all the methods of response, and find how to get the list of products on the Penny page!
    
    def parse_items(self, response):
        #TODO:
        productListPattern = {
            "tag" : "ul",
            "class" : "product-grid is-dlab"
        }
        
        productPattern = {
            "tag" : "li",
            "itemprop" : "itemListElement"
        }

        price_per_unitPattern = {
            "tag" : "li",
            "class" : "comparison-price-content", 
            "data-testid" : "comparison-price-content"
        }

        def getListOfProducts(response, productsPattern):
            pennyItem = PennyItem()
            pennyItem['name'] = 
            pennyItem['title'] = 
            pennyItem['text'] = 
            pennyItem['lastUpdated'] = 

        products = getListOfProducts(response, productListsPattern)
        for product in products:
            yield product