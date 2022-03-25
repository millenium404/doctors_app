from django.contrib import admin
from django.urls import include, path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('account/', include('accounts.urls')),
    path('doctor/', include('doctors.urls')),
    path('admin/', admin.site.urls),
]
