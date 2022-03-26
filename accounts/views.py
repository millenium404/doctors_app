from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import Profile
from django.http import Http404



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
        return redirect('home-view')
        messages.warning(request, 'Грешно потребителско име или парола!')
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'accounts/login.html', context)


@login_required
def profile_update_view(request, id=None):
    obj = get_object_or_404(Profile, user_id=id)
    profile_form = ProfileForm(request.POST or None, instance=obj)
    context = {'object': obj, 'profile_form': profile_form}
    if profile_form.is_valid():
        try:
            profile_form.save()
            messages.success(request, f'Профилът ви е обновен успешно.')
        except:
            messages.warning(request, f'Възникна грешка. Моля, опитайте отново.')
        return redirect('update-view', id=id)
    if id == request.user.id:
        return render(request, 'accounts/user-update.html', context)
    else:
        raise Http404


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login-view')
    return render(request, 'accounts/logout.html', {})
