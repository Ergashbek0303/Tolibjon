from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import auth
from users.forms import UserLoginForm,UserRegistrationForm
from django.urls import reverse
 
def Login(request):
    if request.method =='POST':
        form=UserLoginForm(data=request.POST)
        print('here')
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            
            user=auth.authenticate(username=username,password=password)
            
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('home'))
                
    else:
        form=UserLoginForm()  # Agar Hech narsa user tomonidan jonatilmasa prosta formani o'zini html filega jo'natadi
    context={'form':form}     
    return render(request,'users/login.html',context)


def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        print('form working')
        form=UserRegistrationForm()
    context={
        'form':form,
    }
    return render(request,'users/register.html',context)



def profile(request):
    user=request.user
    context={
        'cust':user
    }
    return render(request,'users/profile.html',context)