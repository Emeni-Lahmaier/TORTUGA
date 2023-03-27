"""devproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import  landingpage
from myapp.views import  sharelandingpage
from myapp.views import * 
from django.contrib.auth.views import LogoutView ,PasswordChangeView

from django.urls import URLPattern
 
urlpatterns = [

    path('', home, name='home'),  
    path('acceuil/', acceuil, name='acceuil'),  
    path('index/', index, name='index'), 
    path('indexa/', indexa, name='indexa'),
    path('landingpage/', landingpage, name='landingpage'), 
    path('sharelandingpage/', sharelandingpage, name='sharelandingpage'),
    path('share/<int:id>', share, name='share'),
    path('addnew', addnew, name='addnew'), 
    path('addnewa', addnewa, name='addnewa'), 
    path('edit/<int:id>', edit, name='edit'),  
    path('edita/<int:id>', edita, name='edita'), 
    path('update/<int:id>', update, name='update'),  
    path('updatea/<int:id>', updatea, name='updatea'), 
    path('delete/<int:id>', destroy, name='destroy'),
    path('destroya/<int:id>', destroya, name='destroya'),   
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',MyloginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
 



]