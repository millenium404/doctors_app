from django.urls import path
from .views import doctor_edit_view

urlpatterns = [
    path('edit/<int:id>', doctor_edit_view, name='doctor-edit-view'),
]
