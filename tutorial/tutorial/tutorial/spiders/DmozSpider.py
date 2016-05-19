# --*-- coding:UTF-8 --*--

# from scrapy.spider import BaseSpider
# class DmozSpider(BaseSpider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]
#     def parse(self, response):
#         filename = response.url.split("/")[-2]
#         open(filename, 'wb').write(response.body)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tutorial.items import TutorialItem
import scrapy
from scrapy import Spider,Selector,log

from scrapy.loader import ItemLoader

from scrapy.contrib.linkextractors import LinkExtractor

class DmozSpider(Spider):
    name = "mm131"
    allowed_domains = ["mm131.com"]
    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]
    # start_urls = ["http://www.mm131.com/xinggan","http://www.mm131.com/xiaohua","http://www.mm131.com/chemo","http://www.mm131.com/qipao","http://www.mm131.com/mingxing"]
    start_urls = ["http://www.mm131.com/xinggan"]
    # rules = (Rule(LinkExtractor(allow=('list_[0-9]_[0-9]{1,2}\.html')),callback='parse_item'),)
    def parse(self, response):
        # count = int(response.url[response.url.rfind('_')+1:response.url.rfind('.')])
        sel = Selector(response)
        count = []
        for link in sel.xpath('//dd/a/@href').extract():
            if link.startswith('list'):
                count.append(int(link[link.rfind('_')+1:link.rfind('.')]))

        for i in range(max(count)):
            request = scrapy.Request(self.start_urls[0]+"/list_6_"+str(i)+".html",callback=self.parse_list)
            yield request

        # request = scrapy.Request(self.start_urls[0]+"/list_6_"+"2"+".html",callback=self.parse_list)
        # yield request
        # for i in rang(count):
        #     scrapy.Request(start_urls[0]+)
        # str = 'jieer'
        # str.rfind('-')

        #filename = response.url.split("/")[-2]
        # hxs = HtmlXPathSelector(response)
        # sites = hxs.select('//ul/li')
        # file = open(filename, 'wt')
        # for site in sites:
        #     item = TutorialItem()
        #     item['title'] = site.select('a/text()').extract()
        #     item['link'] = site.select('a/@href').extract()
        #     item['desc'] = site.select('text()').extract()
        #     for t in title:
        #         file.write('-->'+t+'\n')
        # file.close()
        #     yield item
        # text = response.selector.xpath('//title/text()').extract()
        # text = response.xpath('//title/text()').extract()
        # sel = Selector(type="html")
        # text = response.css('title::text').extract()
        # #href = response.xpath('//base/@href').extract()
        # # img_href = response.xpath('//a[contains(@href,"image")]/@href').extract()
        # link = response.xpath('//a/@href').extract
        #
        # img_href = response.xpath('//img/@src').extract()
        # print '----->'+str(len(text))
        # print('--->'+text[0])
        # #print '--->'+href[0]
        # print '@@@-->'+str(len(img_href))
        # for img in img_href:
        #     print img
        #scrapy.Request()

    def parse_list(self,response):
        urls = Selector(response).xpath('//dd/a/@href').extract()
        split_idex = 0
        for i,u in enumerate(urls):
            if u == '/xinggan/':
                split_idex = i
                break

        urls = urls[0:split_idex]

        for u in urls:
            request = scrapy.Request(u,callback=self.parse_img)
            yield request

    def parse_img(self,response):
        pages = response.url[response.url.rfind('/')+1:response.url.rfind('.')]
        img_urls = "http://img1.mm131.com/pic/"+pages+"/"
        for p in Selector(response).xpath("//span/text()").extract():
            if p.startswith("共"):
                #self.log("###->>"+p)
                log.msg("###->>"+p)
                for i in range(int(filter(lambda x:x.isdigit(),p))):
                    #self.log(img_urls+str(i+1)+"jpg")
                    request = scrapy.Request(img_urls+str(i+1)+".jpg",callback=self.deal_img)
                    yield request

    def deal_img(self,response):
        # self.log("@@@=====>>>"+response.url)
        l = ItemLoader(item=TutorialItem())
        l.add_value('img_url',response.url)
        return l.load_item()