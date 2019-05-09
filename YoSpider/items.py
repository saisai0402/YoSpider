# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class YospiderItem(Item):
    post_title = Field()
    post_keywords = Field()
    post_content = Field()
    post_status = Field()
    post_prefecture_1 = Field()
    post_prefecture_2 = Field()
    post_prefecture_3 = Field()