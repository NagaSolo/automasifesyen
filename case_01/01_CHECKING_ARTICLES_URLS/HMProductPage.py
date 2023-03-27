import scrapy

from file_reader import articles_reader

BASE_URL = 'https://www2.hm.com/en_my/productpage.{}.html'

ARTICLES = articles_reader()

class HmproductpageSpider(scrapy.Spider):
    name = "HMProductPage"

    def start_requests(self):
        for article in ARTICLES:
            yield scrapy.Request(BASE_URL.format(article))

    def parse(self, response):
        ol = response.css('ol')
        name = ''.join(item.css('span::text').get() for item in ol)
        article_id = response.url.split('.')[-2]
        yield {
            'name': name,
            'url': response.url,
            'article_id': article_id if int(article_id) else '0'
        }
