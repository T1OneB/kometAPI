## ABOUT MODULE
# Created by Godp3rsTT
# TG - t.me/Godp3rsTT
# LOLZ - zelenka.guru/lztf
# Web API - https://komet.space/ru/cabinet/api



# RU: Подключаем библиотеки
# EN: Connecting libraries
import requests as r

# RU: Класс GET
# EN: Class get
class get:
    # RU: Функция получения информации об аккаунте по его API токену
    # EN: The function of obtaining information about an account by its API token
    def account(api_key):
	    response = r.get(f"https://komet.space/api/v1/{api_key}/account").json()
	    return response
    
    # RU: Функция получения всех ключей с API токена
    # EN: Function to get all keys from API token
    def keys_all(api_key):
        response = r.get(f"https://komet.space/api/v1/{api_key}/keys/all").json()
        return response
    
    # RU: Функция получения информации о одном ключе по его ID с помощью API токена
    # EN: The function of obtaining information about one key by its ID using the token API
    def keys_get(api_key, key_id):
    	response = r.get(f"https://komet.space/api/v1/{api_key}/keys/get?&key={key_id}").json()
    	return response
    
    # RU: Функция отвязки устройства от ключа по его ID с помощью API токена
    # EN: The function of unbinding a device from a key by its ID using the token API
    def keys_disconnect(api_key, key_id):
    	response = r.get(f"https://komet.space/api/v1/{api_key}/keys/disconnect?&key={key_id}").json()
    	return response