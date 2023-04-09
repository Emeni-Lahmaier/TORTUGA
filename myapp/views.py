from django.shortcuts import render, redirect  
from myapp.forms import ContactForm  
from myapp.forms import ShareForm 
from myapp.forms import UtilisateurForm
from myapp.models import Contact  
from myapp.forms import UserForm
from myapp.forms import *
from django.contrib.auth import authenticate,login
from django.forms import ValidationError
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField,PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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


def landingpage(request):
    landingpages = TemplatesCommuns.objects.all()  
    return render(request,"landingpage.html",{'landingpages':landingpages}) 

def preview(request, id):
    landingpages = TemplatesCommuns.objects.get(id=id)  
    return render(request,"preview.html",{'landingpages':landingpages}) 


def sharelandingpage(request):
   return render(request,'sharelandingpage.html')

def share(request, id):  
    tc = TemplatesCommuns.objects.get(id=id)  
    form = ShareForm(request.POST)  
    if form.is_valid():  
        form.save()  
        return redirect("/landingpage")  
    return render(request, 'sharelandingpage.html', {'tc':tc}) 



def profile(request, id):  
    utilisateur = Utilisateur.objects.get(id=id)  
    return render(request,'profile.html', {'utilisateur':utilisateur})  

def updatep(request, id):  
    utilisateur =Utilisateur.objects.get(id=id)  
    form = UtilisateurForm(request.POST, instance = utilisateur)  
    user =User.objects.get(id=id)  
    formm = UserForm(request.POST, instance = user) 
    if form.is_valid() and formm.is_valid():  
        form.save() 
        formm.save() 
        messages.success(request,"Donnees mis a jours avec Success !  ") 
        return redirect("/acceuil") 
    return render(request, 'profile.html', {'utilisateur':utilisateur}, {'user':user}) 

def landinguser(request):
    landingusers = TemplatesUser.objects.all()  
    return render(request,"landinguser.html",{'landingusers':landingusers}) 

def destroylanding(request, id):  
    landinguser = TemplatesUser.objects.get(id=id)  
    landinguser.delete()  
    return redirect("/landinguser")  

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('home')
    return render(request, 'delete_profile.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('acceuil')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('acceuil')