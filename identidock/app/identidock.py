from flask import Flask, Response, request, render_template
import requests
import hashlib # импортируем библиотеку для хэширования даных


app = Flask(__name__)
salt = "UNIQUE_SALT" # соль для хэш-функции
default_name = "Igor Matiek"


@app.route('/', methods=['GET', 'POST']) # указываем какие медоды будут обрабатываться
def main_page():
    name = default_name
    if request.method == 'POST': # если метод POST
        name = request.form['name'] # получаем значение поля формы
    salted_name = salt + name # добавляем соль к полученному значению из формы
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest() # получаем хэшированное значение
    # data_html = '''
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Identidock</title>
    # </head>
    # <body>
    #     <form method="POST">
    #         Hello <input type="text" name="name" value="{0}">
    #         <input type="submit" value="submit">
    #     </form>
    #     <p>
    #         You look like a:
    #         <img src="/monster/{1}"/>
    #     </p>
    # </body>
    # </html>
    # '''.format(name, name_hash) # изменяем значение парамеитра src для тега img
    return render_template('index.html', name=name, name_hash=name_hash)


@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/{}?size=80'.format(name))
    image = r.content
    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')