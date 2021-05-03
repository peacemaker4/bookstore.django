from django.shortcuts import render, redirect
from authentication.forms import UserForm, ProfileForm
from authentication.models import UserProfile
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    return redirect('/home/')
            else:
                return render(request, 'authentication/login.html', {
                    'error': 'Email or Password error'
                })
        else:
            return render(request, 'authentication/login.html')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user=form.save()
                UserProfile.objects.create(user=user, phone=request.POST.get('phone'))
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if user.is_authenticated:
                    return redirect('/home/')
            else: 
                profile = ProfileForm()
                return render(request, 'authentication/register.html', {
                'form': form,
                'profile': profile,
                'error': 'Incorrect login or password, try again...'
            })
        else:
            form = UserForm()
            profile = ProfileForm()
            return render(request, 'authentication/register.html', {
                'form': form,
                'profile': profile
            })

def logout_user(request):
    logout(request)
    return redirect('login')