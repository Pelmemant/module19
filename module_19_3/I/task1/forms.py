from django import forms

class UserRegister(forms.Form):
    #lable='Ваш логин',
    name = forms.CharField(max_length=18)
    #lable='Пароль'
    password = forms.CharField(min_length=8)
    #lable='Повторите пароль'
    r_password = forms.CharField(min_length=8)
    #, lable='Ваш возраст'
    age = forms.CharField(max_length=3)