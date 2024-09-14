# Clave de API obtenida de OpenWeatherMap
api_key = "a34f7cfb1bd2aef3f882d46f876efe07" #Actualizar con al clave de la API
import requests
import json
from datetime import datetime

# Clave de API obtenida de OpenWeatherMap
#api_key = "introduzca su clave" #Actualizar con al clave de la API

# Latitud y longitud
latitud = 4.85876
longitud = -74.05866

# Parámetros para la solicitud de la API
params = {
    "lat": latitud,
    "lon": longitud,
    "appid": api_key,
}

# Realizar la solicitud a la API
# Endpoint de la API de OpenWeatherMap
api_endpoint = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitud}&lon={longitud}&appid={api_key}"
print(api_endpoint)


response = requests.get(api_endpoint)
weather_data = response.json()

# Generar el nombre del archivo utilizando la fecha y hora actual
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"weather_{current_datetime}.json"

# Especificar las rutas de los archivos
folder_path = "openweathermap_data/raw_data/"
full_file_path = folder_path + filename


# Guardar los datos meteorológicos en un archivo JSON local
with open(full_file_path, "w") as file:
    json.dump(weather_data, file)

# Escribir también el archivo en `openweathermap_data/raw_data/weather.json`
common_file_path = folder_path + "weather.json"
with open(common_file_path, "w") as common_file:
    json.dump(weather_data, common_file)