from flask import Flask, request, render_template
from scrape.wiki import date_of_birth

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', form='form.html')


@app.route('/', methods=['POST'])
def post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template('index.html', date=date_of_birth(first_name, last_name))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
