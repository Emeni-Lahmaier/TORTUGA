from django import forms  
from myapp.models import *  
from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField ,PasswordChangeForm ,UserChangeForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            
        }

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = ['name', 'contact', 'email','categorie'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'categorie': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class AffilieForm(forms.ModelForm):
    class Meta:
        model = Affilie
        fields = ['nom_prenom','contact', 'email','contrat','pourcentage']
        widgets={'nom_prenom': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contrat': forms.Textarea(attrs={'rows': 5}),
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


class PopUpdateForm(forms.ModelForm):
    class Meta:
        model = FormPopUp
        fields = ['title', 'codeHtml', 'description', 'image']
        widgets = {
            'codeHtml': forms.Textarea(attrs={'rows': 5}),
        }

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')

class TemplatesCreateForm(forms.ModelForm):
    class Meta:
        model = TemplatesCommuns
        fields = ['title', 'codeHtml', 'type', 'image']
        widgets = {
            'codeHtml': forms.Textarea(attrs={'rows': 5}),
        }

class PopCreateForm(forms.ModelForm):
    class Meta:
        model = FormPopUp
        fields = ['title','description' ,'codeHtml','image']
        widgets = {
            'codeHtml': forms.Textarea(attrs={'rows': 5}),
        }


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['Address', 'City', 'Country', 'postal_code', 'about_me', 'phonenumber', 'date_naissance']
        widgets = {
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Country': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control'}),
        }


 
        
 



class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {'email': 'Email Address'}

class ShareForm(forms.ModelForm):
    class Meta:
        model = TemplatesUser
        fields = ['title','URL','description']
        widgets= {'title':forms.TextInput(attrs={ 'class': 'form-control' }),
                  'URL': forms.TextInput(attrs={ 'class': 'form-control' }),
                  'description':forms.TextInput(attrs={ 'class': 'form-control' }),}

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




class MyLoginForm(AuthenticationForm):
    username = UsernameField(label="Nom Utilisateur",
        widget=forms.TextInput(attrs={"autofocus": True , 'class':'form-control'}))
    password = forms.CharField(
        label="Mot de Passe",
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
        label= "Mot de Passe Actuel :",
        strip= False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'autofocus':True,'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label= "Nouveau Mot de Passe :",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'autofocus':True,'class':'form-control'}),
    )
    new_password2 = forms.CharField(
        label= "Confirmer le nouveau Mot de Passe :",
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

class GoogleDocs(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    def save(self):
        data = self.cleaned_data
        contact = ContactGoogle.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            content=data['content'],
            image=data.get('image')
        )
        return contact