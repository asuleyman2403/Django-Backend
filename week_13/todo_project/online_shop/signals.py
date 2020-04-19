from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, Product


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        if category.product_amount is None:
            Category.objects.filter(id=category.id)\
                .update(product_amount=Category.objects.get(id=category.id).product_set.count())
        else:
            Category.objects.filter(id=category.id).update(product_amount=category.product_amount + 1)
