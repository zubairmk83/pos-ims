from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('cashier', CashierViewSet)
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('vendor', VendorViewSet)
router.register('purchase', PurchaseOrderItemViewSet)
router.register('sale', SaleViewSet)
router.register('salesItem', SalesItemViewSet)
router.register('return', ReturnRequestViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

