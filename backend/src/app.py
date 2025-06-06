from flask import Flask, render_template
from flask_cors import CORS
from config import config

app = Flask(__name__)

#@app.route('/')

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()

