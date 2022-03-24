from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, ProfileForm


def register_view(request):
    user_form = SignUpForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if all([user_form.is_valid(), profile_form.is_valid()]):
        user = user_form.save(commit=False)
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        return redirect('/account/login/')
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/admin')
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/account/login/')
    return render(request, 'accounts/logout.html', {})
