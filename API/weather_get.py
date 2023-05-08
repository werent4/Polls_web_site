import requests

api_key = "4d0777dCfbb60ac013fe14f132657074a"


def evaluation(data):
    degrees_Celsius = data['main']["temp"]

    if degrees_Celsius >= 20:
        return 'Hot'
    if degrees_Celsius <= 5:
        return 'Cold'
    else:
        return 'Normal'



def get_temperature(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    #data_text = response.text

    degrees_Celsius = data['main']["temp"]

    return f"In city {city_name} temperature is {degrees_Celsius} degrees by Celsium", data
