from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Viewsets for each model

class CashierViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]  # Restrict access to authenticated users
  queryset = Cashier.objects.all()
  serializer_class = CashierSerializer

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class VendorViewSet(viewsets.ModelViewSet):
  queryset = Vendor.objects.all()
  serializer_class = VendorSerializer

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
  queryset = PurchaseOrderItem.objects.all()
  serializer_class = PurchaseOrderItemSerializer

class SaleViewSet(viewsets.ModelViewSet):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer

class SalesItemViewSet(viewsets.ModelViewSet):
  queryset = SalesItem.objects.all()
  serializer_class = SalesItemSerializer

class ReturnRequestViewSet(viewsets.ModelViewSet):
  queryset = ReturnRequest.objects.all()
  serializer_class = ReturnRequestSerializer
