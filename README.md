# ИНФОРМАЦИЯ ПО API
## kometAPI v1.0
### kometAPI v1.0 - это API. Его основой является Web API сайта komet.space. И ниже вы можете прочитать и рассмотреть подробную документацию про него. Кстати, это API написано на ЯП Python...

# ДОКУМЕНТАЦИЯ ПО API

## Класс - get // Данный класс имеет 4 функции и нужен для получения какой-либо информации...
##### Функция - account(api_key)
Данная функция нужна для получения информации об аккаунте с помощью API ключа.
В переменную api_key вы должны передать API ключ, который выдает сам сайт komet.space.
Пример: get.account(2838291182)

##### Функция - keys_all(api_key)
Данная функция нужна для получения всех чит ключей с аккаунта с помощью API ключа.
В переменную api_key вы должны передать API ключ, который выдает сам сайт komet.space.
Пример: get.keys_all(2838291182)

##### Функция - keys_get(api_key, key_id)
Данная функция нужна для получения информации об ключе чита (по его ID) на аккаунте с помощью API ключа.
В переменную api_key вы должны передать API ключ, который выдает сам сайт komet.space.
В переменную key_id вы должны передать ID ключа от чита.
Пример: get.keys_get(2838291182, 66667)

##### Функция - keys_disconnect(api_key, key_id)
Данная функция нужна для отвязки устройства от ключа чита на аккаунте с помощью API ключа.
В переменную api_key вы должны передать API ключ, который выдает сам сайт komet.space.
В переменную key_id вы должны передать ID ключа от чита.
Пример: get.keys_disconnect(2838291182, 66667)
