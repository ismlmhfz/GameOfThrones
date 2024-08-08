from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cases/<int:case_id>/', views.case_view, name='case_view'),
]
