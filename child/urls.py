from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard

urlpatterns = [
    path('base/', include("base.urls")),
    path('', dashboard, name="dashboard"),


  

]