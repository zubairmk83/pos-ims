from rest_framework import serializers
from .models import *

class CashierSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')

  class Meta:
    model = Cashier
    fields = ('user', 'account_type', 'verified')

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'description', 'date_added', 'date_updated')

class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True)

  class Meta:
    model = Product
    fields = ('id', 'code', 'category', 'name', 'description', 'price', 'quantity', 'status', 'date_added', 'date_updated')

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ('id', 'name', 'contact_info')

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseOrderItem
    fields = ('id', 'vendor', 'product', 'quantity', 'unit_price')

class SaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = ('id', 'code', 'grand_total', 'tendered_amount', 'amount_change', 'date_added', 'date_updated')

class SalesItemSerializer(serializers.ModelSerializer):
  sale = SaleSerializer(read_only=True)
  product = ProductSerializer(read_only=True)

  class Meta:
    model = SalesItem
    fields = ('id', 'sale', 'product', 'price', 'quantity', 'total')

class ReturnRequestSerializer(serializers.ModelSerializer):
  product = ProductSerializer(read_only=True)
  sale_record = SaleSerializer(read_only=True)

  class Meta:
    model = ReturnRequest
    fields = ('id', 'product', 'quantity', 'sale_record', 'return_date', 'reason')
