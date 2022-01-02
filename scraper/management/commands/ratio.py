from django.core.management.base import BaseCommand
from properties.models import YieldlyToAlgoRatio, Property
from django.utils import timezone

class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        last_algorand = Property.objects.filter(currency='Algorand').order_by('-date').first()
        last_yieldly = Property.objects.filter(currency='Yieldly').order_by('-date').first()
        datetimenow = timezone.now()
        diff_algo = datetimenow - last_algorand.date
        diff_yieldly = datetimenow - last_yieldly.date

        if (diff_algo.total_seconds() < 300 and diff_yieldly.total_seconds() < 300 \
            and last_algorand.data and last_yieldly.data):
            YieldlyToAlgoRatio.objects.create(ratio=float(last_algorand.data/last_yieldly.data))
        
        
