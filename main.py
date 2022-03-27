from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class City(BaseModel): 
   name : str

@app.post('/getweather')
def get_weather(weather: City):
    r = requests.get(f' http://api.weatherapi.com/v1/current.json?key=d81be5aeb8c547118c375344222802&q={weather}')
    current_weather = r.json()['current']['temp_c']
    return current_weather 
