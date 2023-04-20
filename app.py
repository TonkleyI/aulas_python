import html

from flask import Flask, render_template, request

from vsearch import search_for_letters

from calculo import alg, classificacao

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> html:
    return render_template(
        'entry.html',
        the_title='Bem vindo ao meu Site!'
    )


@app.route('/calcular_raiz')
def pag_raiz() -> html:
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

#Função classificação de idade

@app.route('/classificar_idade')#, methods=['POST'])
def classificacao_idade() -> html:
    return render_template(
        'classificacao.html',

    )

@app.route('/idade', methods=['POST'])
def resultado_idade() -> int:
    resultado = int(request.form['class_idade'])
    idade_classificada = classificacao(resultado)
    return render_template(
        'resultado_idade.html',
        idade_class = idade_classificada
    )
     
app.run(debug=True)