from django.urls import path
from . import views


urlpatterns = [
    path("",views.register),
    path("form-submitted/",views.form_submitted)   
]
