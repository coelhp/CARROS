from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    
    print(request.GET.get('search'))
    cars = Car.objects.all()
    

    return render(
        request,
        'cars.html',
        {'cars': cars}
        )
