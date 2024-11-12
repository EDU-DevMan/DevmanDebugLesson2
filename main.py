import os

from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer


load_dotenv()

forecast_token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

sms_token = os.getenv('SMS_TOKEN')
server = SMSServer(sms_token)

new_event = get_new_event(forecast_token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

print(event_time)

print(event_date)

print(event_area)

print(phenomenon_description)

sms_message = sms_template.format(
    phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: print("new_event: ", new_event) > new_event:
# Регион:  Погода:
# Вывод: Гипотеза подтвердилась, в переменной new_event отсутствуют данные,
# необходим следующий шаг

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: print("town_title: ", town_title) > town_title:  Курск
# Вывод: Гипотеза не подтвердилась переменная не пуста

# Гипотеза 2.2: В town_title не название города
# Способ проверки: ыведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: print("town_title: ", town_title) > town_title:  Курск
# Вывод: Гипотеза не подтвердилась, в переменной содержится город Курск

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: print(token) > token:  None
# Вывод: Гипотеза подтвердилась, в переменной token ничего не лежит

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: `token` не пуст
# Вывод: Гипотеза не подтвердилась, токен доступен из .env

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки:  Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: print(token) > token:  aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Гипотеза подтвердилась, в токен перзаписывается другая переменная

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Закомментировать # token = os.getenv('FORECAST_TOKEN')
# Код для проверки: print(token)
# Установленный факт: print(token) > token:  aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Гипотеза подтвердилась, токен 'FORECAST_TOKEN' перезаписвается токеном SMS_TOKE

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную event_time
# Код для проверки: print(event_time)
# Установленный факт: print(event_time) > утром
# Вывод: Гипотеза не подтвердилась, переменнная содержит корретное значение

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную event_date
# Код для проверки: print(event_date)
# Установленный факт: print(event_date) > 14 ноября
# Вывод: Гипотеза не подтвердилась, переменнная содержит корретное значение

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную event_area
# Код для проверки: print(event_area)
# Установленный факт: print(event_area) > ст. Елец
# Вывод: Гипотеза не подтвердилась, переменнная содержит корретное значение

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную phenomenon_description
# Код для проверки: print(phenomenon_description)
# Установленный факт: print(phenomenon_description) > заморозки до минус 33 градусов
# Вывод: Гипотеза не подтвердилась, переменнная содержит корретное значение
