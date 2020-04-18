from django.urls import path
from .views import *

urlpatterns = [
    path('lists/', TodoListsAPIView.as_view()),
    path('lists/<int:pk>/', TodoListAPIView.as_view()),
    path('lists/<int:pk>/todos/', TodoListTodosAPIView.as_view()),
    path('todos/<int:pk>/', TodoAPIView.as_view())
]
