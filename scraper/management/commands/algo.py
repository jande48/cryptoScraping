from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
# from scraper.spiders import TheodoSpider
from scraper import settings as my_settings
from scraper.spiders.algorand_spider import AlgorandSpider

class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(AlgorandSpider)
        process.start()
        # crawler_settings = Settings()
        # crawler_settings.setmodule(my_settings)

        # process = CrawlerProcess(settings=crawler_settings)

        # process.crawl(PropertiesSpider)
        # process.start()
