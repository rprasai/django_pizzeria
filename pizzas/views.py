from django.shortcuts import render

# Create your views here.
def index(request):
    '''Home page for Pizzas.'''
    return render(request, 'pizzas/index.html')
