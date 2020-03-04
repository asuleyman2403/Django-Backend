from django.db import models
from my_auth.models import MyUser
# Create your models here.


class TodoListManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class TodoList(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True, editable=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = TodoListManager()

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'


class TodoManager(models.Manager):
    pass


class Todo(models.Model):
    STATUSES = (
        (1, 'CREATED'),
        (2, 'IN PROGRESS'),
        (3, 'DONE'),
        (4, 'REJECTED')
    )
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True, editable=True)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES)
    objects = TodoManager()

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
