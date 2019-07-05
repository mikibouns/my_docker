from flask import Flask, render_template, Response
import requests

app = Flask(__name__)
default_name = "Igor Matiek"


@app.route('/', methods=['GET', 'POST'])
def main_page():
    name = default_name
    r = requests.get('http://dnmonster:8000/monster/{}?size=80'.format(name))
    image = r.content
    data_html = '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Identidock</title>
    </head>
    <body>
        <form method="POST">
            Hello <input type="text" name="name" value="{}">
            <input type="submit" value="submit">
        </form>
        <p>
            You look like a:
            <img src={}>
        </p>
    </body>
    </html>
    '''.format(name, image)
    return data_html


@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8000/monster/{}?size=80'.format(name))
    image = r.content
    return Response(image, mimetype='img/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')