from rest_framework import generics
from .models import Category, Product, StockMovement
from .serializers import CategorySerializer, ProductSerializer, StockMovementSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.select_related("category").filter(is_active=True)
        search = self.request.query_params.get("search")
        if search:
            qs = qs.filter(name__icontains=search)
        return qs


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer


class LowStockView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        from django.db.models import F
        return Product.objects.filter(current_stock__lte=F("min_stock_level"), is_active=True)


class StockMovementListView(generics.ListAPIView):
    serializer_class = StockMovementSerializer

    def get_queryset(self):
        qs = StockMovement.objects.select_related("product").order_by("-created_at")
        product_id = self.request.query_params.get("product")
        if product_id:
            qs = qs.filter(product_id=product_id)
        return qs