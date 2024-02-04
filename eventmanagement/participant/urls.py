from django.urls import path
from . import views

urlpatterns = [
    path('participant',views.participant,name='participant'),
]