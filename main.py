import requests
LAT =34.158710
LON = -118.246582
API_Key = "5a816fce88a3ea9c49bc080da35f8233"

weather_params ={
    "lat": LAT,
    "lon":LON,
    "appid": API_Key,
    "exclude": "current,minutely,daily"

}


data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params).json()
for x in range(0,7):
    if data["hourly"][x]["weather"][0]["id"] < 700:
        print("Bring a umbrella")
    else:
        print("no umbrella needed")