import scrapy

from spielbound.items import SpielboundItem

class GameSpider(scrapy.Spider):
    name = "game"
    count = 0
    allowed_domains = ["spielbound.com"]
    start_urls = [
        "http://spielbound.com/library"
    ]

    def parse(self, response):
        # Parse all the games on this page
        for sel in response.css("section[id=content]").xpath('.//td'):
            game = SpielboundItem()

            title = sel.xpath('div/span/div/h2/a/text()').extract()

            # Check for empty td case on the last page of games
            if len(title) > 0:
                self.count += 1
                game['title'] = title[0]
                yield game

        # Find the next page button and start scraping that page
        for href in response.css("section[id=content]").xpath('.//ul').css("li[class=pager-next] > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)

        print self.count
