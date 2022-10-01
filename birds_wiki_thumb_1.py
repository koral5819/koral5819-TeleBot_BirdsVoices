# на примере https://xeno-canto.org/431256

import requests   # https://requests.readthedocs.io/en/latest/user/quickstart/

username = 'koral5819@yandex.ru'
password = 'D#-R723wLcV'
#birds_xeno_nr = '431256'
birds_xeno_nr = '624326'
xeno_api_url = 'https://www.xeno-canto.org/api/2/recordings?query=nr:'
bird = requests.get(xeno_api_url+birds_xeno_nr, auth=(username, password), allow_redirects=True)

if bird.status_code == 200:
    my_bird = bird.json()
    # тут я не знаю как сразу обратиться к элементу в списке словарей, поэтому сделал как сделал :(
    rec = my_bird['recordings']
    rec_dict = rec[0]
    qry = rec_dict['gen'] + ' ' + rec_dict['sp']

# wiki search section
wiki_api_ru_url = 'https://ru.wikipedia.org/api/rest_v1/page/'
s_ru = requests.get(wiki_api_ru_url + 'summary/' + qry)

if s_ru.status_code == 200:
    my_json_ru = s_ru.json()

    print(my_json_ru['title'])

    thumb_url = my_json_ru['thumbnail']['source']
    print(f'Ссылка на превью {thumb_url}')

    page_ru_url = my_json_ru['content_urls']['desktop']['page']
    print(f'Ссылка на страницу {page_ru_url}')

    page_ru_summary = my_json_ru['extract']
    print('\n------------- Краткое содержание статьи(summary) ----------------')
    print(page_ru_summary)
    print('\n')

    # for key,value in my_json_ru.items():
    #     print(key,' : ', value)

wiki_api_en_url = 'https://en.wikipedia.org/api/rest_v1/page/'
s = requests.get(wiki_api_en_url+'summary/'+qry)

if s.status_code == 200:
    my_json = s.json()
    print('\n-------------------- EN ----------------------\n')
    print(my_json['title'])

    thumb_url = my_json['thumbnail']['source']
    print(f'Thumbinail link: {thumb_url}')

    page_url = my_json['content_urls']['desktop']['page']
    print(f'Link to page {page_url}')

    page_summary = my_json['extract']
    print(page_summary)


