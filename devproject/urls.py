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
from myapp.views import  preview
from myapp.views import  profile
from myapp.views import * 
from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp.views import ResetPasswordView, ChangePasswordView
from django.urls import include
from django.urls import URLPattern
from myapp.views import save_image


urlpatterns = [

    path('', home, name='home'),  
    path('acceuil/', acceuil, name='acceuil'), 
    path('homeadmin/', homeadmin, name='homeadmin'), 
    path('template/', template, name='template'),
    path('save-image/', save_image, name='save_image'),
    path('imagedisplay/', imagedisplay, name='imagedisplay'),
    path('index/', index, name='index'), 
    path('indexa/', indexa, name='indexa'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('updatep/<int:id>', updatep, name='updatep'),
    path('landinguser/', landinguser, name='landinguser'),
    path('destroylanding/<int:id>', destroylanding, name='destroylanding'), 
    path('landingpage/', landingpage, name='landingpage'),
    path('destroypost/<int:id>', destroypost, name='destroypost'),
    path('formpop/', formpop, name='formpop'),
    path('reclamation/', reclamation, name='reclamation'),
    path('reclamationSucc/', reclamationSucc, name='reclamationSucc'),
    path('preview/', preview, name='preview'),
    path('preview2/', preview2, name='preview2'),   
    path('template1/<int:id>/',template1, name='template1'),
    path('template2/<int:id>/',template2, name='template2'),
    path('previewform/<int:id>', previewform, name='previewform'), 
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
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/',MyloginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('adminDashboard/', user_list, name='admin_dashboard'),
    path('user/<int:user_id>/delete/', user_delete, name='user_delete'),
    path('user/<int:user_id>/update/', update_user, name='update_user'),
    path('template_create/', template_create, name='template_create'),
    path('pop_template/', pop_create, name='pop_template'),
    path('contact_form/', contact_view, name='contact_form'),
    path('template_update/<int:id>/', template_update, name='template_update'),
    path('pop_update/<int:id>/', pop_update, name='pop_update'),
    path('template_delete/<int:id>/', template_delete, name='template_delete'),
    path('destroyadmin/<int:id>/', destroyadmin, name='destroyadmin'),
    path('pop_delete/<int:id>/', pop_delete, name='pop_delete'),
    path('user_templates/', templates_communs, name='user_templates'),
    path('pop_admin/', pop_admin, name='pop_admin'),
    path('rec_admin/', rec_admin, name='rec_admin'),
    path('previewtemplate/<int:id>/', previewtemplate, name='preview_template'),
    path('contact/', contact_view, name='contact'),
    path('profile/<int:user_id>/update/', update_profile, name='update_profile'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('profiladmin/<int:user_id>/update/', update_profiladmin, name='update_profiladmin'),
    path('profiladmin/<int:user_id>/', profiladmin, name='profiladmin'),
    path('link-generator/', generate_link, name='generate-link'),
    path('template/view/<int:id>/', template_view, name='template_view'),
    path('template/share/<int:id>/', share_template, name='share_template'),
    path('send_email/', send_email, name='send_email'),
    path('notebook/', notebook_view, name='notebook'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('change_passwordadmin/', ChangePasswordViewAdmin.as_view(), name='change_passwordadmin'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

