from django.contrib import admin
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('admin/', admin.site.urls),
]
