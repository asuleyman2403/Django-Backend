from todo import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', views.TodoListsViewSet, basename='lists')
router.register(r'lists/<int:pk>', views.TodoListsTodosViewSet, 'list-todos')
router.register(r'todos', views.TodoViewSet, basename='todos')

urlpatterns = router.urls
