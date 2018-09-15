from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')

Session(app)

db = SQLAlchemy(app)

from views import *


if __name__ == '__main__':
    app.run()
