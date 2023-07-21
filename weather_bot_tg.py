import requests
from config import weather_api,bot_api
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot,types
bot = Bot(token = bot_api)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async  def start_command(message:types.Message):
    await message.reply('Привет! Напиши мне название города и я пришлю сводку погоды! (англ.):o')
@dp.message_handler()
async def get_weather(message: types.Message):


    try:
        r = requests.get( f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_api}&units=metric")
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
        await message.reply(f'Погода в городе {city_cur}\nТемпература : {cur_weatther}°C {wd}\n'
              f'Влажность : {humidity}%\nВетер : {wind}км/час\n'
              f'Отличного дня! :)')



    except Exception as ex:
        await message.reply('Проверьте название города')


if __name__ == '__main__':
    executor.start_polling(dp)