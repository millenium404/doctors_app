from .models import Doctor
import django_filters
from crispy_forms.helper import FormHelper
from .forms import cities, departments


class DoctorFilter(django_filters.FilterSet):

    city = django_filters.ChoiceFilter(choices=cities, label='Град:')
    department = django_filters.ChoiceFilter(choices=departments, label='Специалност:')

    class Meta():
        model = Doctor
        fields = ['city', 'department']
        labels = {
            'city': 'Град',
            'department': 'Специалност',
        }
