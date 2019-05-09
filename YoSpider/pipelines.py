# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from openpyxl import Workbook
from YoSpider.spiders import yospider

class YospiderPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['post_title', 'post_keywords', 'post_content', 'post_status', 'post_prefecture_1', 'post_prefecture_2',
               'post_prefecture_3'])

    def process_item(self, item, spider):
        line = [item['post_title'], item['post_keywords'], item['post_content'], item['post_status'],
                item['post_prefecture_1'], item['post_prefecture_2'], item['post_prefecture_3']]
        self.ws.append(line)
        self.wb.save((r'D:\spider_data\{0}.xlsx').format(yospider.id))
        return item
