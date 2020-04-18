from todo import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'lists', views.TodoListsViewSet, basename='lists')
router.register(r'todos', views.TodoViewSet, basename='todos')


urlpatterns = [
    path('lists/<int:pk>/todos/', views.TodoListTodosAPIView.as_view())
]

urlpatterns += router.urls

