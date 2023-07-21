from pprint import pprint
import requests
from config import weather_api

def get_weather(city,token):
    try:
        r = requests.get( f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric")
        data = r.json()
        # pprint(data)
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        city_cur = data['name']
        cur_weatther = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        print(f'Погода в городе {city_cur}\nТемпература : {cur_weatther}°C {wd}\n'
              f'Влажность : {humidity}%\nВетер : {wind}км/час\n'
              f'Отличного дня! :)')



    except Exception as ex:
        print(ex)
        print('Проверьте название города')
def main():
    city = input('Введите город: ')
    get_weather(city,weather_api)

if __name__ == '__main__':
    main()