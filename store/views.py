from pickle import FALSE
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse

# from flask import jsonify
from apis.models import *
from django.db.models import Count, Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
import json, sys
from datetime import date, datetime
from django.contrib.auth.models import User
# from django.contrib.admin.views.decorators import staff_member_required


# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    categories = len(Category.objects.all())
    products = len(Product.objects.all())
    transaction = len(Sale.objects.filter(
        date_added__year=current_year,
        date_added__month = current_month,
        date_added__day = current_day
    ))
    today_sales = Sale.objects.filter(
        date_added__year=current_year,
        date_added__month = current_month,
        date_added__day = current_day
    ).all()
    total_sales = sum(today_sales.values_list('grand_total',flat=True))
    context = {
        'page_title':'Home',
        'categories' : categories,
        'products' : products,
        'transaction' : transaction,
        'total_sales' : total_sales,
    }
    return render(request, 'store/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'store/about.html',context)


#User management

# @staff_member_required
def cashier(request):
    cashier_list = Cashier.objects.all() 
    context = {
        'page_title':'Cashier List',
        'cashiers':cashier_list,
    }
    
    return render(request, 'store/cashier.html', context)

# @staff_member_required
@csrf_exempt
def manage_cashier(request):
    # Handle GET request
    cashier = {}
    if request.method == 'GET':
        data = request.GET
        id = data.get('id', None)
        if id and id.isnumeric() and int(id) > 0:
            cashier = Cashier.objects.filter(id=id).first()

    context = {
        'cashier': cashier
    }
    return render(request, 'store/manage_cashier.html', context)

@csrf_exempt
def save_cashier(request):
    data = request.POST
    resp = {'status': 'failed'}
    try:
        # Extract data from POST
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password1', None)

        password1 = data.get('password1', None)
        password2 = data.get('password2', None)
        account_type = data.get('account_type', None)

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'msg': 'Passwords do not match.'})
        
         # Create or get the User instance
        user, user_created = User.objects.update_or_create(
            username=username,
            defaults={
                'email': email,
                'password': make_password(password)
            }
        )

         # Use update_or_create to either update an existing cashier or create a new one
        cashier, created = Cashier.objects.update_or_create(
            user=user, # Associate the Cashier with the User
            defaults={
                'account_type': account_type
            }
        )

        resp['status'] = 'success'
        messages.success(request, 'Cashier Successfully saved.')
    except Exception as e:
        resp['error'] = str(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")



# @staff_member_required

def delete_cashier(request):
    data =  request.POST
    resp = {'status':''}
    try:
        cashier=Cashier.objects.get(id=request.POST.get('id')).user
        cashier.delete()
        resp['status'] = 'success'
        messages.success(request, 'Cashier Successfully deleted.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


#Categories
@login_required
def category(request):
    category_list = Category.objects.all()
    context = {
        'page_title':'Category List',
        'category':category_list,
    }
    return render(request, 'store/category.html',context)
@login_required
def manage_category(request):
    category = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            category = Category.objects.filter(id=id).first()
    
    context = {
        'category' : category
    }
    return render(request, 'store/manage_category.html',context)

@login_required
def save_category(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_category = Category.objects.filter(id = data['id']).update(name=data['name'], description = data['description'])
        else:
            save_category = Category(name=data['name'], description = data['description'])
            save_category.save()
        resp['status'] = 'success'
        messages.success(request, 'Category Successfully saved.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_category(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Category.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Category Successfully deleted.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


#Categories
@login_required
def vendor(request):
    vendor_list = Vendor.objects.all()
    context = {
        'page_title':'Vendor List',
        'vendors':vendor_list,
    }
    return render(request, 'store/vendor.html',context)
@login_required
def manage_vendor(request):
    vendor = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            vendor = Vendor.objects.filter(id=id).first()
    
    context = {
        'vendor' : vendor
    }
    return render(request, 'store/manage_vendor.html',context)

@login_required
def save_vendor(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_vendor = Vendor.objects.filter(id = data['id']).update(name=data['name'], contact_info = data['contact_info'])
        else:
            save_vendor = Vendor(name=data['name'], contact_info = data['contact_info'])
            save_vendor.save()
        resp['status'] = 'success'
        messages.success(request, 'vendor Successfully saved.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_vendor(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Vendor.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'vendor Successfully deleted.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Products
@login_required
def products(request):
    product_list = Product.objects.all()
    context = {
        'page_title':'Product List',
        'products':product_list,
    }
    return render(request, 'store/products.html',context)
@login_required
def manage_products(request):
    product = {}
    categories = Category.objects.all()
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            product = Product.objects.filter(id=id).first()
    
    context = {
        'product' : product,
        'categories' : categories
    }
    return render(request, 'store/manage_product.html',context)

@login_required
def save_product(request):
    data =  request.POST
    resp = {'status':'failed'}
    id= ''
    if 'id' in data:
        id = data['id']
    if id.isnumeric() and int(id) > 0:
        check = Product.objects.exclude(id=id).filter(code=data['code']).all()
    else:
        check = Product.objects.filter(code=data['code']).all()
    if len(check) > 0 :
        resp['msg'] = "Product Code Already Exists in the database"
    else:
        category = Category.objects.filter(id = data['category_id']).first()
        try:
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_product = Product.objects.filter(id = data['id']).update(code=data['code'], category_id=category, name=data['name'], description = data['description'], price = float(data['price']), quantity = int(data['quantity']), status = data['status'])
            else:
                save_product = Product(code=data['code'], category_id=category, name=data['name'], description = data['description'], price = float(data['price']), quantity = int(data['quantity']), status = data['status'])
                save_product.save()
            resp['status'] = 'success'
            messages.success(request, 'Product Successfully saved.')
        except:
            resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_product(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Product.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Product Successfully deleted.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def purchase(request):
    purchase_list = PurchaseOrderItem.objects.all()
    context = {
        'page_title':'Purchase List',
        'purchases':purchase_list,
    }
    return render(request, 'store/purchase.html',context)

@login_required
def manage_purchase(request):
    product = {}
    vendor={}
    purchase = PurchaseOrderItem.objects.all()
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            product = Product.objects.filter(id=id).first()
            vendor =  Vendor.objects.filter(id=id).first()

    context = {
        'products' : product,
        'purchases' : purchase,
        'vendors' : vendor
    }
    return render(request, 'store/manage_purchase.html',context)

@login_required
def save_purchase(request):
    data = request.POST
    resp = {'status': 'failed'}
    try:
        # Assuming 'vendor_id' and 'product_id' are provided in the POST data
        vendor_id = data.get('vendor_id')
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 0))

        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_purchase = PurchaseOrderItem.objects.filter(id = data['id']).update(vendor_id=vendor_id, product_id=product_id, quantity=quantity)
        else:
            save_purchase = PurchaseOrderItem(vendor_id=vendor_id, product_id=product_id, quantity=quantity)
            save_purchase.save()

        # Update the product's quantity
        product = Product.objects.get(id=product_id)
        product.quantity += quantity
        product.save()

        resp['status'] = 'success'
        messages.success(request, 'Purchase order successfully saved.')

    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_purchase(request):
    data =  request.POST
    resp = {'status':''}
    try:
        PurchaseOrderItem.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
        messages.success(request, 'Purchase Order Item Successfully deleted.')
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def pos(request):
    products = Product.objects.filter(status = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.id, 'name':product.name, 'price':float(product.price)})
    context = {
        'page_title' : "Point of Sale",
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    # return HttpResponse('')
    return render(request, 'store/pos.html',context)

@login_required
def checkout_modal(request):
    grand_total = 0
    if 'grand_total' in request.GET:
        grand_total = request.GET['grand_total']
    context = {
        'grand_total' : grand_total,
    }
    return render(request, 'store/checkout.html',context)

@login_required
def save_pos(request):
    resp = {'status':'failed','msg':''}
    data = request.POST
    pref = datetime.now().year + datetime.now().year
    i = 1
    while True:
        code = '{:0>5}'.format(i)
        i += int(1)
        check = Sale.objects.filter(code = str(pref) + str(code)).all()
        if len(check) <= 0:
            break
    code = str(pref) + str(code)

    try:
        sales = Sale(code=code, sub_total = data['sub_total'], tax = data['tax'], tax_amount = data['tax_amount'], grand_total = data['grand_total'], tendered_amount = data['tendered_amount'], amount_change = data['amount_change']).save()
        sale_id = Sale.objects.last().pk
        i = 0
        for prod in data.getlist('product_id[]'):
            product_id = prod 
            sale = Sale.objects.filter(id=sale_id).first()
            product = Product.objects.filter(id=product_id).first()
            qty = data.getlist('qty[]')[i] 
            price = data.getlist('price[]')[i] 
            total = float(qty) * float(price)
            print({'sale_id' : sale, 'product_id' : product, 'qty' : qty, 'price' : price, 'total' : total})
            SalesItem(sale_id = sale, product_id = product, qty = qty, price = price, total = total).save()
            i += int(1)
        resp['status'] = 'success'
        resp['sale_id'] = sale_id
        messages.success(request, "Sale Record has been saved.")
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(resp),content_type="application/json")

@login_required
def salesList(request):
    sales = Sale.objects.all()
    sale_data = []
    for sale in sales:
        data = {}
        for field in sale._meta.get_fields(include_parents=False):
            if field.related_model is None:
                data[field.name] = getattr(sale,field.name)
        data['items'] = SalesItem.objects.filter(sale_id = sale).all()
        data['item_count'] = len(data['items'])
        if 'tax_amount' in data:
            data['tax_amount'] = format(float(data['tax_amount']),'.2f')
        # print(data)
        sale_data.append(data)
    # print(sale_data)
    context = {
        'page_title':'Sales Transactions',
        'sale_data':sale_data,
    }
    # return HttpResponse('')
    return render(request, 'store/sales.html',context)

@login_required
def receipt(request):
    id = request.GET.get('id')
    sales = Sale.objects.filter(id = id).first()
    transaction = {}
    for field in Sale._meta.get_fields():
        if field.related_model is None:
            transaction[field.name] = getattr(sales,field.name)
    if 'tax_amount' in transaction:
        transaction['tax_amount'] = format(float(transaction['tax_amount']))
    ItemList = SalesItem.objects.filter(sale_id = sales).all()
    context = {
        "transaction" : transaction,
        "salesItems" : ItemList
    }

    return render(request, 'store/receipt.html',context)
    # return HttpResponse('')

@login_required
def delete_sale(request):
    resp = {'status':'failed', 'msg':''}
    id = request.POST.get('id')
    try:
        delete = Sale.objects.filter(id = id).delete()
        resp['status'] = 'success'
        messages.success(request, 'Sale Record has been deleted.')
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(resp), content_type='application/json')