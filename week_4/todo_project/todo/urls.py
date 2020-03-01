from django.urls import path
from todo import views
urlpatterns = [
    path('lists/', views.TodoListsAPIView.as_view()),
    path('lists/<int:pk>/', views.TodoListAPIView.as_view()),
    path('lists/<int:pk>/todos/', views.TodoListTodosAPIView.as_view()),
    path('todos/<int:pk>/', views.TodoAPIView.as_view())
]
