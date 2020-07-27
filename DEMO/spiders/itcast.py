import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬蟲名
    allowed_domains = ['itcast.cn'] # 允許抓取範圍
    start_urls = ['http://itcast.cn/'] # 最開始請求的 url 地址

    def parse(self, response):
        pass
