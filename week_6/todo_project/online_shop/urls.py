from online_shop import views
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'products', views.ProductsViewSet, basename='products')

urlpatterns = [
    path('categories/<int:pk>/products/', views.CategoryProductsAPIView.as_view())
]

urlpatterns += router.urls

