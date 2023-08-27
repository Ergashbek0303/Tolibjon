from django.shortcuts import render,redirect
from .models import Product,Basket

from django.views.generic import DeleteView
from users.models import User

# Create your views here.

def index(request):
    return render(request,"home/index.html")

def index1(request):
    return render(request,"home/index1.html")
def index2(request):
    return render(request,"home/index2.html")
def index3(request):
    return render(request,"home/index3.html")
def index4(request):
    return render(request,"home/index4.html")







# def index5(request):
#     if request.method =='POST':
#         name=request.POST['name']
#         surname=request.POST['surname']
#         tel=request.POST['tel']
#         birth=request.POST['birth']
#         gender=request.POST['gender']
#         print(gender)

#         new_user=Customers(name=name,
#                             surname=surname,
#                            phone_number=tel,
#                            birthday=birth,
#                             gender=gender)
        
#         new_user.save()
#     return render(request,'home/index5.html')



# def login(request):
#     return render(request,'home/login.html')



def basket(request):
    if request.user.is_authenticated:
        obj=Basket.objects.filter(user=request.user)
        total_sum=sum(basket.sum() for basket in obj)
        total_quantity=sum(basket.quantity for basket in obj)
    else:
        obj=[]
        total_sum=float()
        total_quantity=int()   
    contex={
        'obj':obj,
        'ts':total_sum,
        'tq':total_quantity,
    }

    return render(request,'home/basket.html',contex)



def basket_add(request,product_id):
    product=Product.objects.get(product_id=product_id)
    basket=Basket.objects.filter(user=request.user,product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user,product=product,quantity=1)#customer=request.user
    else:
        basket=basket.first()
        basket.quantity+=1
        basket.save()


    return redirect(request.META['HTTP_REFERER'])

def basket_minus(request,product_id):
    product=Product.objects.get(product_id=product_id)
    basket=Basket.objects.filter(user=request.user,product=product)

    basket=basket.first()
    if basket.quantity!=1:
        basket.quantity-=1
        basket.save()
    else:
        basket_remove(request,basket.id)

    return redirect(request.META['HTTP_REFERER'])

def basket_remove(request,basket_id):
    basket=Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])