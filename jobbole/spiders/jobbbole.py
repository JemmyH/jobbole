# -*- coding: utf-8 -*-
import scrapy
from jobbole.items import JobboleItem
from scrapy.http import Request


class JobbboleSpider(scrapy.Spider):
    name = 'jobbbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_urls = response.xpath("/html/body/div[1]/div[3]/div//div[2]/p[1]/a[1]/@href").extract()  # 获取每一页的阅读原文的链接
        for post_url in post_urls:
            yield Request(url=post_url, callback=self.parse_datail)  # 分别获取每一篇文章的详情页，并将获得的详情页传给parse_datail进行解析
        next_url = response.xpath("/html/body/div[1]/div[3]/div[21]/a/@href").extract()[-1]  # 获取下一页的链接
        if next_url:
            yield Request(url=next_url, callback=self.parse)  # 如果下一页的链接（相当于start_url）存在，则把获取的页面交给parse函数解析

    def parse_datail(self, response):
        title = response.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()").extract()[0]
        date = response.xpath("/html/body/div[1]/div[3]/div[1]/div[2]/p/text()").extract()[0].strip().replace(" ·", "")
        url = str(response.url)
        item = JobboleItem()
        item["title"] = title
        item["date"] = date
        item["url"] = url
        yield item

