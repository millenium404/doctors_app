from django import forms
from .models import Doctor
from appointments.models import Appointment


cities = (('Пловдив', 'Пловдив'), ('София', 'София'), ('Варна', 'Варна'), )
departments = (('Ревматолог', 'Ревматолог'), ('Образна Диагностика', 'Образна Диагностика'), ('Обща Практика', 'Обща Практика'), )

reasons = (('Първичен преглед', 'Първичен преглед'), ('Вторичен преглед', 'Вторичен преглед'), ('Профилактичен преглед', 'Профилактичен преглед'), )

class DoctorEditForm(forms.ModelForm):
    city = forms.ChoiceField(choices=cities, required=False, label='Населено място')
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user', 'active', 'map_url']
        labels = {
            'hospital': 'Болнично заведение',
            'practice_name': 'Име на лекар / лекарска практика',
            'department': 'Специалност',
            'about': 'Описание',
            'phone_number': 'Трефон за връзка с пациенти',
            'address': 'Адрес',
            'nzok': 'Работя с НЗОК',
            'children': 'Работя с деца',
            'price': 'Цена за преглед',
            'image': 'Снимка',
        }


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])


class AppointmentForm(forms.ModelForm):
    reason = forms.ChoiceField(choices=reasons, required=True, label='Причина за посещението')
    class Meta:
        model = Appointment
        fields = ['reason']
