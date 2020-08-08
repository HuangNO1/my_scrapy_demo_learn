import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬蟲名
    allowed_domains = ['itcast.cn'] # 允許抓取範圍
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最開始請求的 url 地址

    def parse(self, response):
        # 處理 start_urls 地址對應的響應
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)
        # pass

        # 分組
        li_list = response.xpath("//div[@class='tea_con']//li")

        for li in li_list:
            item = {}
            # extract_first 或取締一個值
            item['name'] = li.xpath(".//h3//text()").extract_first()
            item['title'] = li.xpath(".//h4//text()").extract()[0]
            # print(item)
            yield item

