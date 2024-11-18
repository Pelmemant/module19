from django import forms

class UserRegister(forms.Form):
    name = forms.CharField(max_length=18, lable = 'Ваш логин')
    password = forms.CharField(min_length=8, lable='Пароль')
    r_password = forms.CharField(min_length=8, lable='Повторите пароль')
    age = forms.CharField(max_length=3, lable='Ваш возраст')