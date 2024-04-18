from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ACCOUNT_TYPE = (
    ('Admin', 'Admin'),
    ('Cashier', 'Cashier'),
)
class Cashier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Cashier')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE, default='Cashier')
    verified = models.BooleanField(default=True)
    def __str__(self):
      return self.user.username


@receiver(post_save, sender=User)
def create_user_cashier(sender, instance, created, **kwargs):
    if created:
        Cashier.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_cashier(sender, instance, **kwargs):
    instance.Cashier.save()


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0)
    quantity = models.IntegerField()
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PurchaseOrderItem(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Foreign key to Vendor model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item for purchase order #{self.vendor.name}: {self.product.name} (x{self.quantity})"

class Sale(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class SalesItem(models.Model):
    sale_id = models.ForeignKey(Sale,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    total = models.FloatField(default=0)

class ReturnRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    sale_record = models.ForeignKey('Sale', on_delete=models.SET_NULL, blank=True, null=True)  # Link to sale record if applicable
    return_date = models.DateTimeField(default=timezone.now)
    reason = models.TextField()
    def __str__(self):
        return f"Return request for {self.product.name}"