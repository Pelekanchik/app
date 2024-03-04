from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
 
    username = forms.CharField()
    password = forms.CharField()
        

    # username = forms.CharField(
    #     label = 'Ім`я',
    #     widget=forms.TextInput(attrs={"autofocus": True ,
    #                                   'class': 'form-control',
    #                                   'placeholder' : 'Введіть ваше ім`я користувача'})
    # )
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введіть ваш пароль'})
    # )


