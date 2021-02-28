# -*- coding: utf-8 -*-
import scrapy


class CryptosSpider(scrapy.Spider):
    name = 'cryptos'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/cryptocurrencies']
    i = 0

    def parse(self, response):
        for row in response.xpath("//tr"):
            yield{
                'symbol': row.xpath('.//td[1]/a/text()').get(),
                'currency': row.xpath('.//td[2]/text()').get(),
                '($USD)price': row.xpath(".//td[3]/span/text()").get(),
                'dollar_price_change': row.xpath(".//td[4]/span/text()").get(),
                'percentage_change': row.xpath('.//td[5]/span/text()').get(),
                'market_capitalization': row.xpath(".//td[6]/span/text()").get(),
                'total_volume_in_all_currencies': row.xpath(".//td[9]/text()").get(),
            }

        self.i = self.i + 25

        next_page = response.xpath(
            "//button[@class='Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(10px) O(n):f Fw(500) C($linkColor)']")
        if next_page:
            yield scrapy.Request(url=f'https://finance.yahoo.com/cryptocurrencies?count=25&offset={self.i}', callback=self.parse)
