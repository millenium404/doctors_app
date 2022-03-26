from django import forms
from .models import Doctor


cities = (('Пловдив', 'Пловдив'), ('София', 'София'), ('Варна', 'Варна'), )
departments = (('Ревматолог', 'Ревматолог'), ('Образна Диагностика', 'Образна Диагностика'), ('Обща Практика', 'Обща Практика'), )

class DoctorEditForm(forms.ModelForm):
    city = forms.ChoiceField(choices=cities, required=False, label='Населено място')
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['active', 'map_url']
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
