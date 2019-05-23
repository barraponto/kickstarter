# -*- coding: utf-8 -*-
import csv
import json
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
                urls = json.loads(row['urls'])
                project_url = urls['web']['project']
                yield scrapy.Request(project_url, meta={'item': row})

    def parse(self, response):
        description = parser.handle(response.css('.full-description').extract_first())
        yield dict(response.meta['item'], description=description)
