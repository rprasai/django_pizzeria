#path needed to map urs to view
from django.urls import path
#dot tells the python to import the views.py models from the same directory as current urls.py
from . import views

app_name = 'pizzas'
urlpattern = [path ('',views.index, name='index'),]

