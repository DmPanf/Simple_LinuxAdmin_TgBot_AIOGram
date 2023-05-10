# Импортируем необходимые модули и функции из библиотеки Flask и других модулей
from flask import Flask, render_template, request, redirect, url_for
from main import get_results, load_cities
from os.path import exists
import ast
import locale


# Создаем экземпляр приложения Flask
app = Flask(__name__)
#app.debug = True

# Определяем маршрут для главной страницы. При переходе на адрес "/", функция home() будет запущена
@app.route('/')
def home():
    # Функция возвращает index.html шаблон
    return render_template('index.html')

## Определяем маршрут для главной страницы с поддержкой методов GET и POST
#@app.route('/', methods=['GET', 'POST'])
#def home():
#    # Обрщаемся к функции для загрузки словаря из файла
#    cities = load_cities()
#    # Получаем список всех городов из словаря
#    cities = list(cities.keys())
#    print(cities)
#    # Возвращаем шаблон index.html с динамическим списком городов
#    return render_template('index.html', cities=cities)


# Определяем маршрут для страницы поиска вакансий, с поддержкой методов GET и POST
@app.route('/search', methods=['GET', 'POST'])
def search():
    # Если метод запроса - POST, мы получаем данные формы
    if request.method == 'POST':
        vacancy = request.form.get('vacancy')
        city = request.form.get('my_city')
        # Затем мы передаем данные формы в функцию get_results, которая возвращает результаты поиска
        results = get_results(vacancy, city)
        # Перенаправляем пользователя на страницу результатов поиска с полученными результатами
        return redirect(url_for('search_results', results=results))
    else:
        # Если метод запроса - GET, мы загружаем словарь со списком городов
        cities = load_cities()
        # Получаем список всех городов из словаря
        cities = sorted(list(cities.keys()))
        # Возвращаем шаблон search.html с динамическим списком городов
        return render_template('search.html', cities=cities)


# Определяем маршрут для страницы результатов поиска
@app.route('/search-results')
def search_results():
    """
    В Flask, request.args используется для доступа к параметрам запроса в строке URL. Это часть URL,
    которая идет после вопросительного знака ? и содержит параметры запроса, разделенные амперсандами &.
    Метод get() для словаря (и для request.args, который по сути является словарем) позволяет 
    получить значение элемента по его ключу. Синтаксис get(key, default) возвращает значение ключа, 
    если он есть в словаре, и возвращает значение по умолчанию, если ключа нет.
    Это полезно в случае, когда параметр 'results' не обязательный. 
    """
    # Получаем результаты поиска из аргументов запроса
    results = request.args.get('results', {})
    results = ast.literal_eval(results)  # для преобразования строки в словарь
    # Возвращаем шаблон search-results.html с полученными результатами
    return render_template('search-results.html', results=results)


# Определяем маршрут для страницы контактов
@app.route('/contacts')
def contacts():
    # Возвращаем шаблон contacts.html
    return render_template('contacts.html')


@app.template_filter('number_format')
def number_format(value, digits=0):
    return f"{value:,.{digits}f}"


# Проверяем, запущен ли скрипт напрямую, а не импортирован
if __name__ == "__main__":
    # Если скрипт запущен напрямую, мы запускаем наше приложение Flask
    app.run(host='0.0.0.0', port=5000)
