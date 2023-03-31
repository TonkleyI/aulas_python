import html

from flask import Flask, render_template, request

from soma import somar_valor

aplication = Flask(__name__)

@aplication.route('/')
@aplication.route('/calculo_valor')
def pag_init() -> html:
    return render_template(
        'calculo_valor.html',
        the_title='Bem vindo ao meu Site!'
    )


@aplication.route('/resultado_valores', methods=['POST'])
def resultado() -> str:
    valor1 = int(request.form['valor1'])
    valor2 = int(request.form['valor2'])
    #opera = request.form['operação']
    title = 'O resultado da soma'
    results = somar_valor(valor1,valor2)
    return render_template(
        'resultado_soma.html',
        the_title=title,
        results=results,
        valor1=valor1,
        valor2=valor2
    )


aplication.run()