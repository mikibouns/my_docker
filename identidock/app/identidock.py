from flask import Flask, render_template


app = Flask(__name__)
default_name = 'Igor Matiek'


@app.route('/')
def get_identicon():
    name = default_name
    return render_template('index.html', data=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')