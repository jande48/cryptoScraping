from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import ScraperItem
import json
from properties.models import Property
from django.utils import timezone

class PropertiesSpider(CrawlSpider):
    name = "properties"
    # domain = "finder.com"
    # start_urls=["https://www.finder.com/algorand-price-prediction",]
   
    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = "https://www.finder.com/algorand-price-prediction"
        self.domain = "finder.com"
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        PropertiesSpider.rules = [
           Rule(LinkExtractor(unique=False), callback='parse_item'),
        ]
        super(PropertiesSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # You can tweak each crawled page here
        # This is the RIGHT properties
        item = ScraperItem()
        item['data'] = response.css('div.stockWidget__price.stockWidget_v2__price ::text').extract()
        name = response.css('div.stockWidget__name ::text').extract()
        print('The name is {}'.format(name))
        print('The data is {}'.format(item['data']))
        if (item and item['data'] and item['data'][0] and name and name[0]=='Algorand'):
            without_money_sign = item['data'][0][1:len(item['data'][0])]
            last_algorand = Property.objects.filter(currency='Algorand').order_by('-date').first()
            datetimenow = timezone.now()
            diff = datetimenow - last_algorand.date
            if without_money_sign.replace('.', '', 1).isdigit() and diff.total_seconds() > 180:
                Property.objects.create(data=float(without_money_sign),currency='Algorand')
        return item
        # yield(item)
        # i = {}
        # i['url'] = response.url
        # data = 
        # return i
    
    # start_urls = ["https://coinmarketcap.com/currencies/algorand/"]
    # # allowed_domains = ["realestatedatabase.net"]
    # # start_urls = [
    # #     "https://realestatedatabase.net/FindAHouse/houses-for-rent-in-kampala-uganda.aspx?Title=Houses+for+rent+in+kampala"
    # # ]
    # rules = (
    #     Rule(
    #         LinkExtractor(unique=True), 
    #         callback='parse',
    #         ),
    # )

    # # rules = (
    # #     Rule(
    # #         LinkExtractor(allow=("HouseDetails\.aspx")),
    # #         callback="parse_property",
    # #         follow=True,
    # #     ),
    # # )
    # def parse(self, response):
    #     data = response.css("div.st-about-employee-pop-up")

    #     url = response.url
    #     print('The url is ',url)
    #     property_loader = ItemLoader(item=ScraperItem(), response=response)
    #     property_loader.default_output_processor = TakeFirst()

    #     # property_loader.add_css(
    #     #     "name", "div.h3 h3::text"
    #     # )
    #     # property_loader.add_css(
    #     #     "fun_fact", "div.p-small p::text"
    #     # )
    #     # yield property_loader.load_item()
    #     for line in data:
    #         item = ScraperItem()
    #         # item["name"] = line.css("div.h3 h3::text").extract_first()
    #         # item["fun_fact"] = line.css("div.p-small p::text").extract().pop()
    #         property_loader.add_css(
    #         "name", "div.h3 h3::text"
    #         )
    #         property_loader.add_css(
    #             "fun_fact", "div.p-small p::text"
    #         )
    #         print('\n\n\n\n\n This is the item')
    #         print(item)
    #         yield property_loader.load_item()
    # def parse_property(self, response):
    #     property_loader = ItemLoader(item=ScraperItem(), response=response)
    #     property_loader.default_output_processor = TakeFirst()

    #     property_loader.add_css(
    #         "code", "span#ContentPlaceHolder1_DetailsFormView_CodeLabel::text"
    #     )
    #     property_loader.add_css(
    #         "price", "span#ContentPlaceHolder1_DetailsFormView_Shillings::text"
    #     )
    #     property_loader.add_css(
    #         "location", "span#ContentPlaceHolder1_DetailsFormView_LocationLabel::text"
    #     )
    #     property_loader.add_css(
    #         "bedrooms",
    #         "span#ContentPlaceHolder1_DetailsFormView_BedsInWordsLabel::text",
    #     )
    #     property_loader.add_css(
    #         "district", "span#ContentPlaceHolder1_DetailsFormView_DistrictLabel::text"
    #     )
    #     property_loader.add_css(
    #         "status", "span#ContentPlaceHolder1_DetailsFormView_StatusLabel::text"
    #     )
    #     property_loader.add_css(
    #         "bathrooms",
    #         "span#ContentPlaceHolder1_DetailsFormView_BathsInWordsLabel::text",
    #     )
    #     property_loader.add_css(
    #         "category", "span#ContentPlaceHolder1_DetailsFormView_CategoryLabel::text"
    #     )
    #     property_loader.add_css(
    #         "agent", "span#ContentPlaceHolder1_DetailsFormView_AgentLabel::text"
    #     )
    #     property_loader.add_css(
    #         "agent_contact", "span#ContentPlaceHolder1_FormView1_TelephoneLabel::text"
    #     )
    #     property_loader.add_css(
    #         "agent_email", "span#ContentPlaceHolder1_FormView1_ContactEmailLabel::text"
    #     )
    #     property_loader.add_css(
    #         "agent_company", "span#ContentPlaceHolder1_FormView1_CompanyLabel::text"
    #     )

    #     yield property_loader.load_item()