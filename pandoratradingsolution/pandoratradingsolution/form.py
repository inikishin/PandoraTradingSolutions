from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, label='Имя', help_text='* Это поле обязательно')
    last_name = forms.CharField(max_length=254, label='Фамилия', help_text='* Это поле обязательно')
    email = forms.EmailField(max_length=254, label='e-mail', help_text='* Это поле обязательно')

class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')