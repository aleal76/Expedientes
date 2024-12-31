from django.urls import path
from . import views

urlpatterns = [
    path('', views.exptes_list),
]