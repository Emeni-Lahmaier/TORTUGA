from django.contrib.auth import authenticate,login
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField,PasswordChangeForm
from .form import * 
from django.contrib import messages

# Create your views here.

def home(request):
 return render(request,'home.html')

def acceuil(request):
   return render(request,'acceuil.html')

class SignupView(View):
    def get(self, request):
        fm= SignUpForm()
        return render(request, 'signup.html',{'form':fm} )
    def post(self, request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Success !  ")
            return redirect('/signup')
        else:
            return render(request, 'signup.html',{'form':fm} )

class MyloginView(View):
   def get(self, request):
      fm=MyLoginForm()
      return render(request , 'login.html',{'form':fm})
   def post(self, request):
      fm=MyLoginForm(request,data= request.POST)
      if fm.is_valid():
         username=fm.cleaned_data['username']
         password=fm.cleaned_data['password']
         
         user = authenticate(request,username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('/acceuil')
      else:
        return render(request , 'login.html',{'form':fm})