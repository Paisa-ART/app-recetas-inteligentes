from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, ShoppingListViewSet

router = DefaultRouter()
router.register(r'', RecipeViewSet, basename='recipe')
router.register(r'shopping-lists', ShoppingListViewSet, basename='shopping-list')

urlpatterns = [
    path('', include(router.urls)),
]
