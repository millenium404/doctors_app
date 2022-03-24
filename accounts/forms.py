from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'city', 'phone', 'is_doctor')
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'email': 'Имейл адрес',
            'city': 'Населено място',
            'phone': 'Телефонен номер',
            'is_doctor': 'Аз съм лекар',
        }
