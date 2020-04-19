from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Min, Sum
from online_shop.models import Product, Category


class Command(BaseCommand):
    help = 'Monitor existing products in DB'

    def handle(self, *args, **kwargs):
        data = [
            Product.objects.aggregate(Avg('price')),
            Product.objects.aggregate(Max('price')),
            Product.objects.aggregate(Min('price')),
            Product.objects.aggregate(Sum('price')),
        ]
        self.stdout.write(self.style.SUCCESS(data))

