from flask import Flask, render_template


app = Flask(__name__)
default_name = 'Igor Matiek'


@app.route('/')
def get_identicon():
    name = default_name
    data_html = '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Identidock</title>
    </head>
    <body>
        <form method="POST">
            Hello <input type="text" name="name" value={}>
            <input type="submit" value="submit">
        </form>
        <img src="/monster/monster.png"/>
    </body>
    </html>
    '''.format(name)
    return data_html


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')