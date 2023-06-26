import requests

def get_weather(api_key):
    # Obtener la ubicación actual basada en la dirección IP
    response = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/ipaddress?apikey={api_key}")
    location_data = response.json()
    location_key = location_data['Key']

    # Obtener el clima actual de la ubicación
    response = requests.get(f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}")
    weather_data = response.json()
    weather_text = weather_data[0]['WeatherText']
    temperature = weather_data[0]['Temperature']['Metric']['Value']

    return weather_text, temperature

# Ejemplo de uso
api_key = "TU_CLAVE_DE_API_DE_ACCUWEATHER"
weather, temperature = get_weather(api_key)
print("Clima:", weather)
print("Temperatura:", temperature, "grados Celsius")
