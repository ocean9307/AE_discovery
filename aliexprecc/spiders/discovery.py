# -*- coding: utf-8 -*-
import scrapy
import re
import json
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

class DiscoverySpider(scrapy.Spider):
    name = 'discovery'
    allowed_domains = ['aliexpress.com']
    def start_requests(self):
        start_urls = ['https://www.aliexpress.com/wholesale?catId=0&SearchText=swimsuit/']
        request = Request(start_urls[0], callback=self.parse)
        yield request

    def parse(self, response):
        urls = response.xpath('//*[@id="hs-below-list-items"]/li')
        for url in urls:
            print('*'*30)
            tar_a = url.xpath('.//a[contains(@class,"picRind")]/@href').get()   #tar_a是a标签里的href链接
            pid = re.findall('(\d*?).html', tar_a)[0]   #pid产品id
            a_url = 'https:'+ tar_a
            print('-'*20,a_url)   #a_url是过滤好的链接
            request = Request(a_url, callback=self.parse_detail)
            yield request
            break

    def parse_detail(self, response):
        print('+'*30)
        # res = response.xpath('')
        url_cus ='https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId=32823170125&type=default&page=1'
        request = Request(url_cus, callback=self.parse_customers)
        yield request

    def parse_customers(self, response):
        #https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?productId=32823170125&type=default&page=1
        print('$'*50)
        customers = json.loads(response.text)
        print(customers['page']['current'], customers['page']['total'], customers['records'][0]['id'])
        pass