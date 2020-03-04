from django.db import models
from my_auth.models import MyUser
# Create your models here.


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True, editable=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    STATUSES = (
        (1, 'IN STOCK'),
        (2, 'SOLD'),
    )
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True, editable=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES)
    price = models.IntegerField(default=0, null=False)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
