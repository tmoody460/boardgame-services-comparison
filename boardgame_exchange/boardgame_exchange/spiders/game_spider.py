import scrapy

from boardgame_exchange.items import BoardGameExchangeItem

class GameSpider(scrapy.Spider):
    name = "game"
    count = 0
    allowed_domains = ["boardgameexchange.com"]
    start_urls = [
        "http://boardgameexchange.com/all-games.html?limit=all"
    ]

    def parse(self, response):
        # Parse all the games on this page
        for sel in response.css("form[id=product_addtocart_form] > div > ul > li > h2"):
            game = BoardGameExchangeItem()

            title = sel.xpath('a/text()').extract()

            # Check for empty td case on the last page of games
            if len(title) > 0:
                self.count += 1
                game['title'] = title[0]
                yield game

        print self.count
