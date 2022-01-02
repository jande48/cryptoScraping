from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import ScraperItem
import json
from properties.models import Property
from django.utils import timezone

class YieldlySpider(CrawlSpider):
    name = "properties"
    # domain = "finder.com"
    # start_urls=["https://www.finder.com/algorand-price-prediction",]
   
    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = "https://coinmarketcap.com/currencies/yieldly/"
        self.domain = "coinmarketcap.com"
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        YieldlySpider.rules = [
           Rule(callback='parse_item', follow=False),
        ]
    
        super(YieldlySpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # You can tweak each crawled page here
        # This is the RIGHT properties
        item = ScraperItem()
        item['data'] = response.css('div.priceValue ::text').extract()
        name = response.css('h1.priceHeading ::text').extract()
        print('The name is {}'.format(name))
        print('The data is {}'.format(item['data']))
        if (item and item['data'] and item['data'][0] and name and name[0]=='Yieldly Price'):
            without_money_sign = item['data'][0][1:len(item['data'][0])]
            last_algorand = Property.objects.filter(currency='Yieldly').order_by('-date').first()
            datetimenow = timezone.now()
            diff = datetimenow - last_algorand.date
            if without_money_sign.replace('.', '', 1).isdigit() and diff.total_seconds() > 180:
                Property.objects.create(data=float(without_money_sign),currency='Yieldly')
        return item