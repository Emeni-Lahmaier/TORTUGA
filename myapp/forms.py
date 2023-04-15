from django import forms  
from myapp.models import *  
from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField ,PasswordChangeForm ,UserChangeForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = ['name', 'contact', 'email'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class AffilieForm(forms.ModelForm):
    contrat = forms.CharField(widget=CKEditorWidget(),label="Contrat")

    class Meta:
        model = Affilie
        fields = ['nom_prenom','contact', 'email','contrat','pourcentage']
        widgets={'nom_prenom': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contrat': forms.TextInput(attrs={ 'class': 'form-control' }),
            'pourcentage': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
class UtilisateurUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TemplatesUpdateForm(forms.ModelForm):
    class Meta:
        model = TemplatesCommuns
        fields = ['title', 'codeHtml', 'type', 'image']
        widgets = {
            'codeHtml': forms.Textarea(attrs={'rows': 5}),
        }

class TemplatesCreateForm(forms.ModelForm):
    class Meta:
        model = TemplatesCommuns
        fields = ['title', 'codeHtml', 'type', 'image']
        widgets = {
            'codeHtml': forms.Textarea(attrs={'rows': 5}),
        }

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['num_tel','date_naissance']
        widgets={'user': forms.TextInput(attrs={ 'class': 'form-control' }), 

            'num_tel': forms.TextInput(attrs={ 'class': 'form-control' }),
            'date_naissance': forms.DateInput(attrs={ 'class': 'form-control' }),
        
        }
        
 



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets={'first_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
                 'last_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
        
        }

class ShareForm(forms.ModelForm):
    class Meta:
        model = TemplatesUser
        fields = ['title','URL','description']
        widgets= {'title':forms.TextInput(attrs={ 'class': 'form-control' }),
                  'URL': forms.TextInput(attrs={ 'class': 'form-control' }),
                  'description':forms.TextInput(attrs={ 'class': 'form-control' }),}

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Password Again ",widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True,label=" First Name ",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,label=" Last Name ",widget=forms.TextInput(attrs={'class':'form-control'}))


    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields =('first_name','last_name','username','email')
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'})}




class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True , 'class':'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )
class MyContactForm():
    label="Nom&Prenom",
    label="Numero Telephone",
    label="Email"

class MyAffForm():
    label="Nom&Prenom",
    label="Numero Telephone",
    label="Email",
    label="Contrat",
    label="Pourcentage"

class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label= "Old password",
        strip= False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'autofocus':True,'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label= "New password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'autofocus':True,'class':'form-control'}),
    )
    new_password2 = forms.CharField(
        label= "New password Again",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'autofocus':True,'class':'form-control'}),
    )

class EditProfileForm(UserChangeForm):

      class Meta:
        model = User
        fields = (
          'first_name',
          'username',
          'email',
        )
        exclude = ('password',)