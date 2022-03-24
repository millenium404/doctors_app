from django.contrib import admin
from django.urls import include, path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
