from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, create_task, add_money


urlpatterns = [
    path('', dashboard, name="dashboard" ),
    path('create_task/', create_task, name="create_task"),
    path('add_money', add_money, name="add_money" ),
    path('base/', include("base.urls")),

]