from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import BooksAPIView, JournalsAPIView


router = DefaultRouter()

router.register(r'books', BooksAPIView)
router.register(r'journals', JournalsAPIView)

urlpatterns = router.urls
# urlpatterns = [
#     path('books/', BooksAPIView.as_view()),
#     path('journals/', JournalsAPIView.as_view())
# ]
