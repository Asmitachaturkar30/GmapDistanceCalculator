from django.shortcuts import render
from .models import City_model

from django.shortcuts import render

def calculate_distance(request):
    if request.method == 'POST':
        city1_name = request.POST.get('place_1')
        city2_name = request.POST.get('place_2')

        distance = City_model.calculate_distance(city1_name, city2_name)

        return render(request, 'distanceCalculator.html', {'distance': distance})
    else:
        return render(request, 'distanceCalculator.html')

