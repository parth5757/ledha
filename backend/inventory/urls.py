from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    LowStockView, StockMovementListView
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view()), 
    path("categories/<int:pk>", CategoryDetailView.as_view()),
    path("products/", ProductListCreateView.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view()),
    path("products/low-stock",LowStockView.as_view()),
    path("stock-movements/", StockMovementListView.as_view()),
]
