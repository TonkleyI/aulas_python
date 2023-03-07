from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Ola Mundo do Flask"


app.run()