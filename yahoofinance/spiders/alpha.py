# -*- coding: utf-8 -*-
import scrapy


class AlphaSpider(scrapy.Spider):
    name = 'alpha'
    allowed_domains = ['seekingalpha.com']
    # start_urls = ['https://seekingalpha.com/']

    def start_requests(self):
        yield scrapy.Request(url='https://seekingalpha.com',
                             callback=self.parse,
                             headers={
                                 #  'Accept': '*/*',
                                 #  'Accept-Encoding': 'gzip, deflate, br',
                                 #  'Accept-Language': 'en-US,en;q=0.9',
                                 #  'Cache-Control': 'max-age=0',
                                 #  'Connection': 'keep-alive',
                                 #  'Host': 'dt.adsafeprotected.com',
                                 #  'Referer': 'https://7cc26609924e82e5b93e2bbd7a046da6.safeframe.googlesyndication.com/',
                                 #  'sec-ch-ua': 'Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99',
                                 #  'sec-ch-ua-mobile': '?0',
                                 #  'Sec-Fetch-Dest': 'empty',
                                 #  'Sec-Fetch-Mode': 'no-cors',
                                 #  'Sec-Fetch-Site': 'cross-site',
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'})

    def parse(self, response):
        yield {
            'period': response.xpath("//button[@data-test-id='register-now-button']/text()").get()
        }
