import translators as ts

# Название птицы: 'Eurasian Wren'
# Всю фразу переводит неверно, надо скармливать по одному
#

birds_name_en = 'Eurasian Wren'
birds_name_en_1 = 'Eurasian'
birds_name_en_2 = 'Wren'
translate_1= ts.google(birds_name_en, from_language='en', to_language='ru', if_use_cn_host=True)
translate_2= ts.google(birds_name_en_1, from_language='en', to_language='ru', if_use_cn_host=True)
translate_3= ts.google(birds_name_en_2, from_language='en', to_language='ru', if_use_cn_host=True)
print(translate_1)
print(translate_2 + ' ' + translate_3)
