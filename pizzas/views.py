from django.shortcuts import render, redirect
from .models import Pizza, Topping
from pizzas import forms

# Create your views here.
def index(request):
    '''Home page for Pizzas.'''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context={'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html',context)

def piz(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
   # image = Pizza.objects.get()
    toppings=pizza.topping_set.order_by('-date_added')
    comments=pizza.comment_set.order_by('-date_added')
    context={'pizza':pizza, 'toppings':toppings,'comments':comments }
    return render(request, 'pizzas/piz.html',context)

def comment(request, pizza_id):
    if request.method != 'POST':
        form=forms.CommentForm()
    else:
        pizza = Pizza.objects.get(id = pizza_id)
        form=forms.CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.pizza=pizza
            comment.save()
            return redirect('pizzas:pizzas')
    context={'form':form, 'pizza_id': pizza_id}
    return render(request,'pizzas/comment.html',context)

# def homepage(request):
