import html

from flask import Flask, render_template, request

from vsearch import search_for_letters

from calculo import alg

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Ola Mundo do Flask"


@app.route('/calcular_raiz')#-- , methods=['POST'])
def pag_raiz() -> html:
   # a_raiz = request.form['a_raiz']
    return render_template(
    'raiz.html',
    the_title = 'Calcule o valor da raiz'
    )

@app.route('/resultado_raiz', methods=['POST'])
def projetar() -> str:
    resultado = request.form['a_raiz']
    print(resultado)
    x1 = int(resultado[1:2])
    x2 = int(resultado[3:4])
    y1 = int(resultado[7:8])
    y2 = int(resultado[9:10])
    p1 = (x1, x2)
    p2 = (y1, y2)
    raiz = alg(p1, p2)
    print(raiz)
    results = 'Resultado do calculo'
    return render_template(
        'raiz2.html',
        a_raiz = raiz
        
    )

@app.route('/busca_palavra', methods=['POST'])
def do_search() -> str:
    frase = request.form['frase']
    letras = request.form['letras']
    title = 'Aqui está o resultado'
    results = str(search_for_letters(frase, letras))
    return render_template(
        'results.html',
        the_title=title,
        the_results=results,
        a_frase=frase,
        as_letras=letras
    )


@app.route('/entry')
def entry_page() -> html:
    return render_template(
        'entry.html',
        the_title='Bem vindo ao meu Site!'
    )

app.run()