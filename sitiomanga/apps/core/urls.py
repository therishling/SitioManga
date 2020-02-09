from django.contrib import admin
from django.urls import path, re_path
from apps.core import views as vistas
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dashboard/', login_required(vistas.Dashboard.as_view()), name="dashboard"),
]
