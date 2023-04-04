from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import CustomUser, ReferalTable
# Create your views here.

class RegistrationView(View):

    def get(self, request):
        html = 'Userregistration.html'
        return render(request, html)


    def post(self, request):
        data = request.POST
        name = data['name']
        phone = data['phone']
        password = data['password']
        referal = data['referal']
        referal_obj = CustomUser.objects.filter(referal=referal)
        try:
            if CustomUser.objects.get(phone=phone):
                return redirect('register')
        except:
            new_user = CustomUser(username=phone, name=name, phone=phone)
            new_user.set_password(password)
            new_user.save()

            while new_user.referal != 'default':
                new_user = CustomUser.objects.get(phone=new_user.referal)
                new_user.add_new_member()
            return redirect('login')

class LoginView(View):

    def get(self, request):
        html = 'Userlogin.html'
        return render(request, html)


    def post(self, request):
        data = request.POST
        user = authenticate(username = data['phone'], password = data['password'])
        if user:
            login(request, user)
            return redirect('catalog')
        else:
            return redirect('login')