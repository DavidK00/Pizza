from django.shortcuts import render, redirect
from django.template import loader
from .models import Pizza
from .forms import CommentForm


# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.all()
    context = {'pizza':pizza, "toppings": toppings}
    return render(request, 'MainApp/pizza.html', context)
def new(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        form = CommentForm()
    context = {'form', form}
    return render(request, 'MainApp/pizza.html', context)






    

    