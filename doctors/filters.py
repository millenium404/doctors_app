from .models import Doctor
import django_filters
from django import forms
from .forms import cities, departments


class DoctorFilter(django_filters.FilterSet):

    city = django_filters.ChoiceFilter(choices=cities)
    department = django_filters.ChoiceFilter(choices=departments)

    class Meta():
        model = Doctor
        fields = ['city', 'department']
        labels = {
            'city': 'Град',
            'department': 'Специалност',
        }
