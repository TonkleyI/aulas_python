import html

from flask import Flask, render_template, request

from soma import somar_valor

app = Flask(__name__)




@app.route('/')
def inicio() -> html:
    return render_template(
        'entry.html'
    )