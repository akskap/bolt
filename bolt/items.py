# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Webpage(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()
    status = scrapy.Field()
    images = scrapy.Field()


class Image(scrapy.Item):
    src = scrapy.Field()
    name = scrapy.Field()
