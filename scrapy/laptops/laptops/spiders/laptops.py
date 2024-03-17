#To create the project : scrapy startproject ecommerce
# To create spider: scrapy genspider https://www.johnlewis.com/browse/electricals/laptops-macbooks/view-all-laptops-macbooks/_/N-a8f
#To run Spider: scrapy crawl laptops


import math
import re
from typing import Iterable
import scrapy
from selenium import webdriver
from scrapy.selector import Selector


class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["www.johnlewis.com"]
    start_urls = ["https://www.johnlewis.com/browse/electricals/laptops-macbooks/view-all-laptops-macbooks/_/N-a8f"]
    
    # def __init__(self):
    #     chrome_options = webdriver()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parsePage)

    def parsePage(self, response):
        hxs = Selector(text=response.text)
        products_per_page = 192
        products_per_chunk = 24
        total_products = int(re.findall(r'\d+', ''.join(hxs.xpath('//*[@id="screen-reader-updates"]//text()').extract()))[0])
        total_pages = math.ceil(total_products/products_per_page)
        remaining_products = total_products
        for page_number in range(1, total_pages+1):
            if remaining_products > products_per_page:
                this_page = products_per_page
                remaining_products -= products_per_page
            else:
                this_ipage = remaining_products
            chunks_count = math.ceil(this_page/ products_per_chunk)
            if remaining_products >= products_per_page:
                remaining_products -= products_per_page
            url = f'{self.start_urls[0]}?page={page_number}&chunk={chunks_count}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        hxs = Selector(text = response.text)
        links = hxs.xpath('//*[@class ="product-card_c-product-card__link__QeVVQ"]/@href').extract()
        for link in links:
            url_= 'https://'+ self.allowed_domains[0]+link
            yield scrapy.Request(url=url_,callback=self.parseProducts)

    def parseProducts(self, response):
        hxs = Selector(text = response.text)
        title = hxs.xpath('//*[@id="__next"]//h1//text()').extract()[0]
        price = hxs.xpath('//*[@class="ProductPrice_ProductPrice__Y8bXE"]//text()').extract()[0]
        yield {
            "title": title,
            "price": price
        }


# Command to output to json files ---> scrapy crawl laptops -o laptops.json
        
        
        
    