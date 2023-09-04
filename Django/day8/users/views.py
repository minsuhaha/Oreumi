from django.shortcuts import render,redirect
from django.contrib.auth import logout

def social_login_view(request):
    return render(request, 'users/social_login.html')

def login_success(request):
    username = request.user

    return render(request, 'users/main.html', {'username':username})

def logout_view(request):
    logout(request)
    return redirect('social_login')