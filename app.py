from flask import Flask, request, render_template
from scrape.wiki import Person

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', form='form.html')


@app.route('/', methods=['POST'])
def post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    person = Person(first_name, last_name)
    return render_template('index.html',
        name=person.get_name(),
        date=person.get_date_of_birth(),
        img=person.get_image(),
    )


@app.errorhandler(404)
def internal_error(error):
    return render_template('index.html',
        error='Błąd aplikacji'
    )


@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html',
        error='Nie znaleziono osoby...'
    )


def main():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
