# ПРИМЕР РАБОТЫ БИБЛИОТЕКИ kometAPI

# Импортируем API библиотеку
import KometAPI as api

# API ключ
token="YOUR API KEY HERE"
# Вызываем функцию получения информации об аккаунте по его API ключу
a = api.get.account(api_key=token)
# Выводим результат функции в консоль
print(a)

# {'ok': True, 'data': {'id': СКРЫЛ, 'balance': 'СКРЫЛ', 'bonuses': СКРЫЛ, 'deposits': 'СКРЫЛ', 'discount': СКРЫЛ, 'refer_balance': 'СКРЫЛ', 'refers': СКРЫЛ}, 'timezone': 'Europe/Moscow', 'time': СКРЫЛ}

# Если в начале 'ok': True , это значит, что запрос был успешно отправлен и получен
