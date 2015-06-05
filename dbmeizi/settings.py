# -*- coding: utf-8 -*-

# Scrapy settings for dbmeizi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dbmeizi'

SPIDER_MODULES = ['dbmeizi.spiders']
NEWSPIDER_MODULE = 'dbmeizi.spiders'
ITEM_PIPELINES = ['dbmeizi.pipelines.MongoDBPipeline',]
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "dbmeizi"
MONGODB_COLLECTION = "meizi"
DOWNLOAD_DELAY = 5#2个请求间隔时间为5s

# log 配置
# LOG_LEVEL = "INFO"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dbmeizi (+http://www.yourdomain.com)'
