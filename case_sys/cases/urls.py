from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cases', views.case_view, name='case_view'),
]
