from django.urls import path
from .views import login_view, register_view, logout_view, profile_update_view

urlpatterns = [
    path('login/', login_view, name='login-view'),
    path('register/', register_view, name='register-view'),
    path('logоut/', logout_view, name='logout-view'),
    path('update/<int:id>', profile_update_view, name='update-view'),
]
