from django import forms  
from myapp.models import *  
from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField ,PasswordChangeForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = ['name', 'contact', 'email'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class AffilieForm(forms.ModelForm):
    class Meta:
        model = Affilie
        fields = ['nom_prenom','contact', 'email','contrat','pourcentage']
        widgets={'nom_prenom': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contrat': forms.TextInput(attrs={ 'class': 'form-control' }),
            'pourcentage': forms.TextInput(attrs={ 'class': 'form-control' }),
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

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Utilisateur
        fields = ['avatar', 'bio']

class ProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = [
            'avatar',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'bio',
            'city',
            'state',
            'country',
            'favorite_animal',
            'hobby',
        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        bio = cleaned_data.get("bio")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )