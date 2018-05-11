# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import urllib.request

class JobbolePipeline(object):
    def open_spider(self, spider):
        print("爬虫开始")
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user="hujiaming", passwd="123456", db="hujiaming", charset="utf8")
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):
        sql_insert = "insert into jobbole(title,create_date,url) values('{0}','{1}','{2}');".format(item["title"], item["date"], item["url"])
        self.cur.execute(sql_insert)
        self.conn.commit()
        urllib.request.urlretrieve(url="", path="")
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

