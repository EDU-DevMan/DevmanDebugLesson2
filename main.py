import os

from weather_sdk import get_new_event, SMSServer

token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

token = os.getenv('SMS_TOKEN')
server = SMSServer(token)

new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

print("new_event", new_event)

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
# Способ проверки: ...
# Код для проверки: ...
# Установленный факт: ...
# Вывод: ...

# Гипотеза 2.2: В town_title не название города
# Способ проверки: ...
# Код для проверки: ...
# Установленный факт: ...
# Вывод: ...
