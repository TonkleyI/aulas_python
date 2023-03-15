import html

from flask import Flask, render_template, request

from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Ola Mundo do Flask"


@app.route('/busca_palavra', methods=['POST'])
def do_search() -> str:
    frase = request.form['frase']
    letras = request.form['letras']
    return str(search_for_letters(frase, letras))


@app.route('/entry')
def entry_page() -> html:
    return render_template(
        'entry.html',
        the_title='Bem vindo ao meu Site!'
    )

app.run()