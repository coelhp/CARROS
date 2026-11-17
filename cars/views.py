from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    return render(
        request,
        'cars.html',
        {'cars': {'model': 'Astra 2.0'}}
        )
