import scrapy


TEST_URL = 'https://www2.hm.com/en_my/productpage.0684021184.html'


class HmproductpageSpider(scrapy.Spider):
    name = "HMSingleProductPage"

    def start_requests(self):
        yield scrapy.Request(TEST_URL)

    def parse(self, response):
        yield {
            # 'breadcrumbs': response.css('ol::span::text').get(),
            'breadcrumbs': '/'.join(item.css('span::text').get() for item in response.css('ol')),
            'url': response.url
        }
