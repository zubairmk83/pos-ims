from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'store/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),

    path('cashier', views.cashier, name="cashier-page"),
    path('manage_cashier', views.manage_cashier, name="manage_cashier-page"),
    path('save_cashier', views.save_cashier, name="save-cashier-page"),
    path('delete_cashier', views.delete_cashier, name="delete-cashier"),


    path('category', views.category, name="category-page"),
    path('manage_category', views.manage_category, name="manage_category-page"),
    path('save_category', views.save_category, name="save-category-page"),
    path('delete_category', views.delete_category, name="delete-category"),

    path('vendor', views.vendor, name="vendor-page"),
    path('manage_vendor', views.manage_vendor, name="manage_vendor-page"),
    path('save_vendor', views.save_vendor, name="save-vendor-page"),
    path('delete_vendor', views.delete_vendor, name="delete-vendor"),

    path('products', views.products, name="product-page"),
    path('manage_products', views.manage_products, name="manage_products-page"),
    path('save_product', views.save_product, name="save-product-page"),
    path('delete_product', views.delete_product, name="delete-product"),

    path('purchase', views.purchase, name="purchase-page"),
    path('manage_purchase', views.manage_purchase, name="manage_purchase-page"),
    path('save_purchase', views.save_purchase, name="save_purchase-page"),
    path('delete_purchase', views.delete_purchase, name="delete-purchase"),
    
    
    path('pos', views.pos, name="pos-page"),
    path('checkout-modal', views.checkout_modal, name="checkout-modal"),
    path('save-pos', views.save_pos, name="save-pos"),
    path('sales', views.salesList, name="sales-page"),
    path('receipt', views.receipt, name="receipt-modal"),
    path('delete_sale', views.delete_sale, name="delete-sale"),

    path('return', views.return_request, name="return_request-page"),
    path('manage_return', views.manage_return_request, name="manage_return_request-page"),
    path('save_return', views.save_return_request, name="save_return_request-page"),
    path('delete_return', views.delete_return, name="delete-return_request"),


]