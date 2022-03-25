from django import forms
from .models import Doctor


class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('hospital', 'practice_name', 'department', 'about', 'phone_number', 'city', 'address', 'nzok', 'children', 'price', 'image')
        labels = {
            'hospital': 'Болнично заведение',
            'practice_name': 'Име на лекар / лекарска практика',
            'department': 'Специалност',
            'about': 'Описание',
            'phone_number': 'Трефон за връзка с пациенти',
            'city': 'Населено място',
            'address': 'Адрес',
            'nzok': 'Работя с НЗОК',
            'children': 'Работя с деца',
            'price': 'Цена за преглед',
            'image': 'Снимка',
        }
