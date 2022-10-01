# Получаем на входе название птицы на английском - переменная "query"
# Ищем в википедии статью про эту птицу
# Готовим материал: краткое содержание статьи, ссылка на полное содержание, фото (видимо достаточно взять превью)
#
# Через апи есть доступ к записям голосов в формате .ogg

import requests
import json

api_url = 'https://en.wikipedia.org/api/rest_v1/page/'
query = 'Eurasian Wren'

s = requests.get(api_url+'summary/'+query)
#print(s.url)

if s.status_code == 200:
#    print('Get wikipedia summary - OK')
    my_json = s.json()
#    print(s.json())
    print(my_json['title'])

#Тут мы получаем адрес превью, если надо то есть и оригинал
    thumb_url = my_json['thumbnail']['source']
    print(thumb_url)

# Тут выяснилось, что не у всех страниц есть версии на русском языке
# По описанию АПИ, есть тег доступности на разных языках
# Можно заморочиться, можно дать ссылку на англоверсию вики и если есть желание пусть дальше переключают вручную
# Иначе надо искать аналоги статьи через таксономию видов и это нам не нужно
    page_url = my_json['content_urls']['desktop']['page']
#    page_url_ru = page_url.replace('//en.w', '//ru.w')
#    print(page_url, '', page_url_ru)
    print(page_url)

# Краткое содержание статьи
    page_summary = my_json['extract']
    print(page_summary)



