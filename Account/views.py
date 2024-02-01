from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.

# def admin_profile(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             form = CustomUserCreationForm()   
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'register_form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                    login(request, user)
                    return redirect('/homepage')
            else:
                return render(request, 'login_form.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {'form': form})



def registration(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_employee = True
            user.save()
            return redirect ('/user_login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register_form.html', {'user_form': user_form})