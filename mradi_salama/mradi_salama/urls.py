from django.contrib import admin
from django.urls import path
from tovuti_yangu.views import nyumbani

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nyumbani, name='home'),
]


