import scrapy
from datetime import date


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/losers']
    today = date.today()
    i = 0

    # def start_requests(self):
    #     yield scrapy.Request(url='https://finance.yahoo.com/losers',
    #                          callback=self.parse,
    #                          headers={'Referer': '', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'})

    def parse(self, response):
        for row in response.xpath("//table[@class='W(100%)']/tbody/tr"):
            yield {
                'date': self.today.strftime("%m/%d/%Y"),
                'symbol': row.xpath(".//td[1]/a/text()").get(),
                'name': row.xpath("normalize-space(.//td[2]/text())").get(),
                'price': row.xpath(".//td[3]/span/text()").get(),
                'dollar_change': row.xpath(".//td[4]/span/text()").get(),
                'percentage_change': row.xpath(".//td[3]/span/text()").get(),
                'volume': row.xpath(".//td[6]/span/text()").get(),
                'market_capitalization': row.xpath('.//td[8]/span/text()').get(),
            }

        self.i = self.i + 25

        next_page = response.xpath(
            "//button[@class='Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(10px) O(n):f Fw(500) C($linkColor)']")

        if next_page:
            yield scrapy.Request(url=f'https://finance.yahoo.com/losers?count=25&offset={self.i}', callback=self.parse)
