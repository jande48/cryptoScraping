from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
# from scraper.spiders import TheodoSpider
from scraper import settings as my_settings
from scraper.spiders.yieldly_spider import YieldlySpider

class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(YieldlySpider)
        process.start()
