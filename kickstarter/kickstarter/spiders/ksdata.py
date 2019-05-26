# -*- coding: utf-8 -*-
import csv
import scrapy

from ..parse_html import parser


class KsdataSpider(scrapy.Spider):
    name = 'ksdata'
    allowed_domains = ['kickstarter.com']
    start_urls = ['http://kickstarter.com/']

    def __init__(self, file=None, **kwargs):
        self.path = file
        super().__init__(**kwargs)

    def start_requests(self):
        with open(self.path) as csvinput:
            reader = csv.DictReader(csvinput)
            for row in reader:
                url = row['urls']
                # url = url.replace('ref=discovery_category_newest', 'ref=category_newest') # @XXX: re-use old cache
                yield scrapy.Request(url, meta={'item': row})

    def parse(self, response):
        data = {
                'description': parser.handle(response.css('.full-description').extract_first()),
                'comment_count': response.css('#comments-emoji .count data::attr("data-value")').extract_first(),
                'updates_count': response.css('#updates-emoji .count::text').extract_first(),
                'faq_count': response.css('#faq-emoji .count::text').extract_first(),
                }
        yield dict(response.meta['item'], **data)
