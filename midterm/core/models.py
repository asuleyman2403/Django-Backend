from django.db import models
from my_auth.models import MyUser
# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=800, default='')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    GENRES = (
        (1, 'Fantasy'),
        (2, 'Classic'),
        (3, 'Poems')
    )
    num_pages = models.IntegerField()
    genre = models.IntegerField(choices=GENRES)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


TYPES = (
    (1, 'Bullet'),
    (2, 'Food'),
    (3, 'Travel'),
    (4, 'Sport')
)


class Journal(BookJournalBase):
    types = models.IntegerField(choices=TYPES, null=False)
    publisher = models.CharField(max_length=255, null=False)


