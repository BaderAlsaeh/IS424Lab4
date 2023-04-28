from django.urls import path 
from . import views 
urlpatterns=[
    path ("", views.index,name='index'),
    path ('<int:num>', views.anyNumber, name='anynumber'),
    path ('taxrate', views.taxrate,name= 'taxrate')
]

 