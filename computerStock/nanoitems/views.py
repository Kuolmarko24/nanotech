from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ProductForm

from django.http import HttpResponse
from .models import *
from .forms import  ProductForm

# Create your views here.
def home(request):
    total_promotions = promotions.count()
    total_products = products.count()
    context = {'total_promotions': total_promotions,'total_products':total_products}
    return render(request,'nanoitems/dashboard.html',context)
def products(request):
    products = Product.objects.all()
    return render(request, 'nanoitems/dashboard.html',{'products': products})

def promotions(request):
    promotions = Promotion.objects.all()
    return render(request, 'nanoitems/promotions.html',{'promotions':promotions})
def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['kuolmarko47@gmail.com'])
        # return HttpResponse('Thanks for submitting! We shall be in touch soon')
    return render(request, 'nanoitems/contactus.html',{})
def addproduct(request):
    if request.method=="POST":
        if request.POST.get('item') and request.POST.get('type') and request.POST.get('qty') and request.POST.get('price') and request.POST.get('specs'):
            saveproduct = Product()
            saveproduct.item = request.POST.get('item')
            saveproduct.type = request.POST.get('type')
            saveproduct.quantity = request.POST.get('qty')
            saveproduct.price = request.POST.get('price')
            saveproduct.specs = request.POST.get('specs')
            saveproduct.save()
            messages.success(request,"The record "+saveproduct.item+" Is saved Successfully!")
        return render(request,"nanoitems/addproduct.html")
    else:
        return render(request,"nanoitems/addproduct.html")
# add promotion
def addpromotion(request):
    if request.method=="POST":
        if request.POST.get('promo_name') and request.POST.get('category') and request.POST.get('status'):
            saveproduct = Promotion()
            saveproduct.promo_name = request.POST.get('promo_name')
            saveproduct.category = request.POST.get('category')
            saveproduct.status = request.POST.get('status')
            saveproduct.save()
            messages.success(request,"The record is posted Successfully!")
        return render(request,"nanoitems/addpromotion.html")
    else:
        return render(request,"nanoitems/addpromotion.html")
# end of post promotion


def editproduct(request,id):
    
    produpdate = get_object_or_404(Product, id=id)

    if request.method == "POST":
        produpdate.item = request.POST["item"]
        produpdate.type = request.POST["type"]
        produpdate.quantity = request.POST["qty"]
        produpdate.price = request.POST["price"]
        produpdate.specs = request.POST["specs"]

        produpdate.save()
        messages.success(request,"The product record is updated successfully...")
        
        return render(request,"nanoitems/edit.html",{"Product":produpdate})


    return render(request,'nanoitems/edit.html',{"Product":produpdate})


def viewproduct(request,id):
    
    produpdate = get_object_or_404(Product, id=id)

    return render(request,'nanoitems/view.html',{"Product":produpdate})


def productUpdate(request,id):
    pupdate=Product.objects.get(id=id)

    form = ProductForm(request.POST, instance=pupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The product record is updated successfully...")
    return render(request,"nanoitems/edit.html",{"Product":pupdate})


def productdelete(request,id):
    delstudent = Product.objects.get(id=id)
    delstudent.delete()
    results = Product.objects.all()
    return render(request,"nanoitems/dashboard.html",{"Product":results})