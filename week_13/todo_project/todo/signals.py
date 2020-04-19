from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TodoList, Todo


@receiver(post_save, sender=Todo)
def todo_created(sender, instance, created, **kwargs):
    if created:
        task_list = instance.list
        if task_list.task_amount is None:
            TodoList.objects.filter(id=task_list.id)\
                .update(task_amount=TodoList.objects.get(id=task_list.id).todo_set.count())
        else:
            TodoList.objects.filter(id=task_list.id).update(task_amount=task_list.task_amount + 1)
