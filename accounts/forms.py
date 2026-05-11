from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, DateInput, URLInput, Select

from accounts.models import Profile

UserModel = get_user_model()

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel



class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email...'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat your password...'



class AppUserLoginForm(AuthenticationForm):
    username = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your email...'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password...'




class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', ]
        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Enter your username'
            }),
            'first_name': TextInput(attrs={
                'placeholder': 'Enter your first name'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Enter your last name'
            }),
            'date_of_birth': DateInput(attrs={
                'type': 'date'
            }),
            'profile_picture': URLInput(attrs={
                'placeholder': 'Link to image'
            }),
            'gender': Select(attrs={
                'placeholder': 'Type your gender'
            })

        }



class ProfileEditForm(ProfileBaseForm):
    ...

