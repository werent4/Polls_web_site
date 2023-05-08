from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .weather_get import get_temperature, api_key, evaluation
# Create your views here.

@login_required
def index(request):
    return render(request, 'API/index.html')

@login_required
def weather(request):
    if request.method == 'GET':
        city_name = request.GET.get('site', 'Kiev')
    else:
        city_name = 'Kiev'

    try:
        temperature, data_json = get_temperature(city_name=city_name, api_key=api_key)
        eval = evaluation(data_json)
    except Exception as e:
        temperature = 'Write the correct name of the city'
        data_json = "Write the correct name of the city"
        eval = 'Unknown'


    context = {
        'temperature': temperature,
        'data_text': data_json,
        'evaluation': eval
    }
    return render(request, 'API/weather.html', context)