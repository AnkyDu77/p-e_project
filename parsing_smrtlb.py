"""Парсит 'https://smart-lab.ru/q/shares/' при помощи библиотек
requests и BeautifulSoup. Из скаченного материала выбираются названия эмитентов,
очищаются от "мусора" и записываются в базу MySQL запросом UPDATE."""

import requests
from bs4 import BeautifulSoup as bs
import re
from updt_cmpn_names import update_names

"""Получаем данные с сайта 'https://smart-lab.ru/q/shares/' и формируем из них
bs-объект"""
url = 'https://smart-lab.ru/q/shares/'
req = requests.get(url)
soup = bs(req.text, features = 'lxml')
soup_str = str(soup)

"""Записываем bs-объект в файл для последующего писка нужной информации"""
with open('text_sl.txt', 'w') as file:
    file.write(soup_str)

"""Находим все ссылки, содержащие названия эмитентов"""
res_link_lst = []
with open('text_sl.txt', 'r') as file_prs:
    for line in file_prs:
        item = re.findall('/forum.+?\s', line)
        res_link_lst.append(item)

"""Очищаем список имен эмитентов от пустых значений"""
clean_lst = [value for value in res_link_lst if value != []]

"""Формируем список имен эмитентов для занесения в базу данных MySQL"""
name_lst = []
for item in clean_lst:
    name = re.findall('>[А-Яа-яa-zA-Z0-9-.+]+.<?', item[0])
    name_lst.append(name)
clean_name_lst0 = [value for value in name_lst if value != []]
clean_name_lst1 = []
for item in clean_name_lst0:
    name = item[0]
    clean_name = name[1:-1]
    clean_name_lst1.append(clean_name)
del clean_name_lst1[:2]
del clean_name_lst1[-3:]

"""При помощи функции 'update_names', содержащейся в файле 'updt_cmpn_names.py'
обновляем названия имен в таблице MySQL"""
update_names(clean_name_lst1)
