#from pprint import pprint
from pickle import dump, load
from os.path import exists
from json import dump as json_dump
from requests import get
from collections import Counter
from bs4 import BeautifulSoup

from area import get_area_id
from skills import get_skills

def get_results(vacancy, my_city):
    url = 'https://api.hh.ru/vacancies'

    # загрузка текущих курсов валют ЦБ РФ
    data = get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rate = data['Valute']

    # загрузка файла с кодами городов
    area = load_cities()

    p = {'text': vacancy}
    r = get(url=url, params=p).json()
    count_pages = r['pages']
    all_count = len(r['items'])

    result = {
            'keywords': vacancy,
            'count': all_count,
            'city': my_city
             }

    sal = {'from': [], 'to': []}
    skills_all = []

    # определяем, сколько будет получено страниц, и проходим по каждой из страниц
    for page in range(count_pages):
        if page > 4:
            break

        p = {'text': vacancy,
             'page': page}
        ress = get(url=url, params=p).json()
        all_count = len(ress['items'])
        result['count'] += all_count

        for res in ress['items']:
            city_vac = res['area']['name']
            # добавление города из ответа на запроса, если его нет в файле
            if city_vac not in area:
                area[city_vac] = get_area_id(res['area']['id'])

            if my_city == 'all' or city_vac == my_city:
                res_full = get(res['url']).json()
                skills = get_skills(res_full['description'], res_full['key_skills'])
                skills_all += skills

                # обработка зарплаты
                if res_full['salary']:
                    code = res_full['salary']['currency']
                    k = 1 if code == 'RUR' else float(rate[code]['Value'])
                    sal['from'].append(k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
                    sal['to'].append(k * res_full['salary']['to'] if res['salary']['to'] else k*res_full['salary']['from'])

    # формирование результата
    result.update({
        'average_from': round(sum(sal['from']) / len(sal['from']), 2) if sal['from'] else 0,
        'average_to': round(sum(sal['to']) / len(sal['to']), 2) if sal['to'] else 0,
        'requirements': [{'name': name, 'count': count, 'percent': round((count / result['count'])*100, 2)}
                          for name, count in Counter(skills_all).most_common(5)]
    })

    # сохранение файла с результами работы
    with open('/app/data/result.json', mode='w') as f:
        json_dump([result], f)
    with open('area.pkl', mode='wb') as f:
        dump(area, f)
    return result


def load_cities():
    if exists('/app/data/area.pkl'):
        with open('/app/data/area.pkl', mode='rb') as f:
            cities = load(f)
        return cities
    else:
        return {}
