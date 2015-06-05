# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.http import Request

class MongoDBPipeline(object):

    def __init__(self):
        self.imageurls = []
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            dataid = item["dataid"]
            rslt = self.collection.find({'dataid':dataid}).count()

            if rslt <= 0:
                self.collection.insert(dict(item))
                log.msg("Meizi added to MongoDB database!",
                    level=log.INFO, spider=spider)
            else:
                log.msg("当前记录已经存在")
        return item