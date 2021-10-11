from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'Email or password is invalid.')
            return redirect('login')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')
