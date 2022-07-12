# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    stars = scrapy.Field()
    rating = scrapy.Field()
    prices = scrapy.Field()
    quality_price = scrapy.Field()
    comments = scrapy.Field()
    popular_services = scrapy.Field()
    services = scrapy.Field()
    beaches = scrapy.Field()
    airports = scrapy.Field()
    url = scrapy.Field()
    pass
