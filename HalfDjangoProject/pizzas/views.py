from django.shortcuts import render

from .models import Pizza


def index(request):
	""" The home page for pizzeria."""
	return render(request, 'pizzas/index.html')

def pizzas(request):
	"""show all pizzas"""
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/pizza_names.html', context)

def pizza(request, pizza_id):
	"""Show a single pizza and all its toppings."""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.order_by('-date_added')
	context = {'pizza': pizza, 'toppings': toppings}
	return render(request, 'pizzas/pizza_name.html', context)