import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['yhdm.tv'] # 允許抓取範圍
    start_urls = ['http://www.yhdm.tv/']

    def parse(self, response):
        li_list = response.xpath("//div[@class='img']//ul//li")

        # print(li_list)

        for li in li_list:
            item = {}
            item['link'] = li.xpath(".//a/@href").get();
            item['image'] = li.xpath(".//a//img/@src").get();
            item['name'] = li.xpath(".//p[@class='tname']//a//text()").get();
            item['last'] = li.xpath(".//p[last()]//a//text()").get();
            item['last_url'] = li.xpath(".//p[last()]//a/@href").get();
            yield item

