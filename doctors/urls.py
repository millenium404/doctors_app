from django.urls import path
from .views import doctor_edit_view, doctor_list_view, doctor_detail_view, doctor_search_view, schedule_view


# app_name='doctors'
urlpatterns = [
    path('', doctor_search_view, name='search'),
    path('edit/<int:id>', doctor_edit_view, name='doctor-edit-view'),
    path('detail/<int:id>', doctor_detail_view, name='doctor-detail-view'),
    path('schedule/<int:id>', schedule_view, name='schedule-view'),
    path('list/', doctor_list_view, name='doctor-list-view'),
]
