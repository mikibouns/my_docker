from flask import Flask, Response, request, render_template
import requests
import hashlib # импортируем библиотеку для хэширования даных
import redis # библиотека для кэширования данных


app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0) # настройка Redis
salt = "UNIQUE_SALT" # соль для хэш-функции
default_name = "Igor Matiek"


@app.route('/', methods=['GET', 'POST']) # указываем какие медоды будут обрабатываться
def main_page():
    name = default_name
    if request.method == 'POST': # если метод POST
        name = request.form['name'] # получаем значение поля формы
    salted_name = salt + name # добавляем соль к полученному значению из формы
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest() # получаем хэшированное значение
    return render_template('index.html', name=name, name_hash=name_hash)


@app.route('/monster/<name>')
def get_identicon(name):
    image = cache.get(name) # получаем name
    if image is None: # проверяем значение name
        print("Cash miss", flush=True) # выводится информация об отсутствии кэша
        r = requests.get('http://dnmonster:8080/monster/{}?size=80'.format(name))
        image = r.content
        cache.set(name, image) # сгенерированный образ добавляется в кэш и связывается с именем, как в БД (ключ: значение)
    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')