from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from my_auth import views

router = DefaultRouter()

router.register(r'register', views.MyUserAPIView)
urlpatterns = [
    path('login/', obtain_jwt_token),
] + router.urls
