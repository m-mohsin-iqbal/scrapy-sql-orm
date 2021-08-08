# -*- coding: utf-8 -*-
import scrapy

from items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('article.product_pod h3 a::attr(href)'):
            yield response.follow(href, self.parse_book)

        # follow pagination links
        for href in response.css('ul.pager li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_book(self, response):
        item = dict(
            title='Mohsin',
            description="Orm script",
            price='345',
            imageurl='image_url',
            image='image'
        )
        print(item)
        return item

        # def extract_with_css(query):
        #     return response.css(query).extract_first().strip()





#scrapy crawl books -o books.json -s CLOSESPIDER_PAGECOUNT=5
