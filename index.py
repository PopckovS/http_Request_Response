#! /usr/bin/python3

import requests
import os

"""

Expires
Заголовок содержит дату/время, по истечении которой ответ с сервера считается устаревшим.
Прошедшая или невалидная дата, например 0, обозначает, что ресурс уже устарел.Если в ответе с
сервера установлен заголовок Cache-Control с директивами "max-age" или "s-maxage",
заголовок Expires игнорируется.

Свойства:
    Тип заголовка : Response header
    Запрещенное имя заголовка : нет
    CORS безопасный заголовок : да

Пример:
    Expires: Wed, 21 Oct 2015 07:28:00 GMT
"""

adress = 'http://example.org'

def request_options(adress):
    response = requests.options(adress)
    print("Отправка запроса OPTIONS при помощи модуля requests")
    print(response.status_code)
    print(response)

    for header in response.headers:
        print(header, response.headers[header])

    print(response.text)
    print('======= Конец вывода =======')

def os_options(adress):
    """curl -X OPTIONS http://example.org -i"""
    response = os.system('curl -X OPTIONS {adress} -i'.format(adress=adress))
    print("Отправка запроса OPTIONS при помощи curl самой системы Linux")
    print(response)
    print('======= Конец вывода =======')


request_options(adress)
os_options(adress)