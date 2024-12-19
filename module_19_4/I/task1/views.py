from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
# Create your views here.

def shop(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'shop.html', context)

class Cart(TemplateView):
    template_name = 'cart.html'

class Page(TemplateView):
    template_name = 'page.html'

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        r_password = request.POST.get('r_password')
        age = request.POST.get('age')
        try:
            tom = Buyer.objects.get(name=name)
            info["error"] = 'Логин уже зарегистрирован'
        except Buyer.DoesNotExist:
            if password == r_password:
                if age > 18:
                    tom = Buyer.objects.create(name= name, balance=0, age=age)
                    info["ok"] = f'Приветствуем, {name}'
                else:
                    info["error"] = 'Вам должно быть больше 18 для регистрации'
            else:
                info["error"] = 'Пароли не совпадают'
    error_type = 'error'
    return render(request, 'registration_page.html')#, HttpResponse(f"{info[error_type]}")

# def sign_up_by_django(request):
    user = ['max', 'pol', 'saha']
    info = {}

    if request.mathod == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            r_password = form.cleaned_data['r_password']
            age = form.cleaned_data['age']
            try:
                tom = Buyer.objects.get(name=name)
                info["error"] = 'Логин уже зарегистрирован'
            except Buyer.DoesNotExist:
                if password == r_password:
                    if age > 18:
                        tom = Buyer.objects.create(name= name, balance=0, age=age)
                        info["error"] = f'Приветствуем, {name}'
                        info['form'] = form

                    else:
                        info["error"] = 'Вам должно быть больше 18 для регистрации'

                else:
                    info["error"] = 'Пароли не совпадают'

    error_type = 'error'
    return render(request, 'registration_page.html', {"info": info}), HttpResponse(f"{info[error_type]}")
