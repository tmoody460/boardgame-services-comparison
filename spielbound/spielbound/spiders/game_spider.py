import scrapy

class GameSpider(scrapy.Spider):
    name = "game"
    allowed_domains = ["spielbound.com"]
    start_urls = [
        "http://spielbound.com/library"
    ]

    def parse(self, response):
        i = 0
        for sel in response.css("section[id=content]").xpath('.//td'):
            title = sel.xpath('div/span/div/h2/a/text()').extract()[0]
            print "Title:", title
