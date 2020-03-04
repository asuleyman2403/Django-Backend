from online_shop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'categories/<int:pk>', views.CategoryProductsViewSet, basename='category-products')
router.register(r'products', views.ProductsViewSet, basename='products')

urlpatterns = router.urls

