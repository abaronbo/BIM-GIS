# myproject/ifcupload/urls.py

from django.urls import path
from . import views

urlpatterns = [
       path('upload-form/', views.upload_form, name='upload_form'),
       path('upload-ifc/', views.upload_ifc, name='upload_ifc'),
       path('get-ifc-url/', views.get_ifc_url, name='get_ifc_url'),
       path('upload-dataset/', views.upload_dataset, name='upload_dataset'),
]
