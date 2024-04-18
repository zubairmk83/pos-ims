from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cashier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(PurchaseOrderItem)
admin.site.register(Sale)
admin.site.register(SalesItem)
admin.site.register(ReturnRequest)

