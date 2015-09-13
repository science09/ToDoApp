# encoding:utf-8
__author__ = 'le'

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
#app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {'db': 'todo'}
app.config['SECRET_KEY'] = 'flasktodoapp'
app.config['WTF_CSRF_ENABLED'] = False
db = MongoEngine(app)


from app import views, models