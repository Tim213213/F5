from django.shortcuts import render, redirect
from .forms import MainDishForm, SideDishForm
from .models import MainDish, SideDish


def home_page(request):
    main_dish_form = MainDishForm()
    side_dish_form = SideDishForm()
    main_dishes = MainDish.objects.all()
    side_dishes = SideDish.objects.all()
    return render(request, 'index.html',
                 {'main_dish_form': main_dish_form,
                  'side_dish_form': side_dish_form,
                  'main_dishes': main_dishes,
                  'side_dishes': side_dishes})


def add_main_dish(request):
    main_dish = MainDishForm(request.POST)
    if main_dish.is_valid():
        main_dish.save()
    return redirect('home')

def add_side_dish(request):
    side_dish = SideDishForm(request.POST)
    if side_dish.is_valid():
        side_dish.save()
    return redirect('home')

