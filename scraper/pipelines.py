from word2number import w2n
from .items import ScraperItem
import json
from properties.models import Property

class ScraperPipeline(object):
    def __init__(self, items, *args, **kwargs):
        # self.unique_id = unique_id
        self.items = items

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        item = ScraperItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        print(' We are inside the pipeline')
        #print('The item is {}'.format(item))
        if (item and item['data'] and item['data'][0]):
            Property.objects.create(data=str(item['data'][0]))
        return item
        # adapter = ScraperItem(item)
        # if adapter.get('data'): # if scraped data has a price
        #    item.save() # save it to database 
        #    return item

        # self.items.append(item['url'])
        # return item
    # """
    # Saves Item to the database
    # """
    # def process_item(self, item, spider):
    #     item = ScraperItem()
    #     item.unique_id = self.unique_id
    #     item.data = json.dumps(self.items)
    #     item.save()
    #     return item


class PropertyStatusPipeline(object):
    """
    Replace text for item status i.e For Rent will be replaced with Rent.
    """
    def process_item(self, item, spider):
        if item.get('status'):
            item['status'] = item['status'].replace('For ', '')
            return item


class PropertyPricePipeline(object):
    """
    Removes signs from the price value. i.e replaces 10000/= with 10000
    """
    def process_item(self, item, spider):
        if item.get('price'):
            item['price'] = item['price'].replace('/=', '')
            return item


class ConvertNumPipeline(object):
    """
    Converts words to number values for bedrooms and bathrooms
    """
    def process_item(self, item, spider):
        if item.get('bathrooms'):
            item['bathrooms'] = w2n.word_to_num(item['bathrooms'])
        if item.get('bedrooms'):
            item['bedrooms'] = w2n.word_to_num(item['bedrooms'])
        return item

class TheodoTeamPipeline(object):
    def process_item(self, item, spider):
        print('This is the item in the model {}'.format(item))
        item.save()
        return item