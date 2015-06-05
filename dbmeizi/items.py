# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MeiziItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()#三秒变成一个酷姐yo
    titleurl = Field()#http://www.doubanmeizi.com/2015/05/710/
    updateday = Field()#27
    updatedate = Field()#2015-05
    dataid = Field()#p30478421[1]
    width = Field()#500
    height = Field()#572
    tags = Field()#三秒变成一个酷姐yo
    desc = Field()#突然发现单身久了，总是发现自己一个人。每天就像是机器一样
    imageurl = Field()#http://www.doubanmeizi.com/wp-content/uploads/2015/05/p304784211.jpg
    startcount = Field()#三秒变成一个酷姐yo
    pass

