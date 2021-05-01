#path needed to map urs to view
from django.urls import path
#dot tells the python to import the views.py models from the same directory as current urls.py
from . import views

app_name = 'pizzas'
urlpatterns = [path ('',views.index, name='index'), 
path ('pizzas',views.pizzas, name='pizzas'),
path ('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),]

