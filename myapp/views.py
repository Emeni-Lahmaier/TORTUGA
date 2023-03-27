from django.shortcuts import render, redirect  
from myapp.forms import ContactForm  
from myapp.forms import ShareForm 
from myapp.models import Contact  
from myapp.forms import *
from django.contrib.auth import authenticate,login
from django.forms import ValidationError
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField,PasswordChangeForm
from django.contrib import messages

# Create your views here.

class SignupView(View):
    def get(self, request):
        fm= SignUpForm()
        return render(request, 'signup.html',{'form':fm} )
    def post(self, request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Success !  ")
            return redirect('/login')
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

# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass
    else:  
        form = ContactForm()  
    return render(request,'index.html',{'form':form})  
 
def index(request):  
    contacts = Contact.objects.all()  
    return render(request,"show.html",{'contacts':contacts})  
 
def edit(request, id):  
    contact = Contact.objects.get(id=id)  
    return render(request,'edit.html', {'contact':contact})  
 
def update(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/index")  
    return render(request, 'edit.html', {'contact':contact})  
     
def destroy(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/index")  

def addnewa(request):  
    if request.method == "POST":  
        form = AffilieForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/indexa')  
            except:  
                pass
    else:  
        form = AffilieForm()  
    return render(request,'indexa.html',{'form':form}) 

def indexa(request):  
    affilies = Affilie.objects.all()  
    return render(request,"showaffilie.html",{'affilies':affilies}) 

 
def edita(request, id):  
    affilie = Affilie.objects.get(id=id)  
    return render(request,'edita.html', {'affilie':affilie})  
 
def updatea(request, id):  
    affilie = Affilie.objects.get(id=id)  
    form = AffilieForm(request.POST, instance = affilie)  
    if form.is_valid():  
        form.save()  
        return redirect("/indexa")  
    return render(request, 'edita.html', {'affilie':affilie}) 

def destroya(request, id):  
    affilie = Affilie.objects.get(id=id)  
    affilie.delete()  
    return redirect("/indexa")  

def home(request):
 return render(request,'home.html')


def acceuil(request):
   return render(request,'acceuil.html')

def email(request):
    emails = TemplatesCommuns.objects.all()  
    return render(request,"email.html",{'emails':emails}) 
def sharelandingpage(request):
   return render(request,'sharelandingpage.html')

def share(request, id):  
    tc = TemplatesCommuns.objects.get(id=id)  
    form = ShareForm(request.POST)  
    if form.is_valid():  
        form.save()  
        return redirect("/email")  
    return render(request, 'sharelandingpage.html', {'tc':tc}) 