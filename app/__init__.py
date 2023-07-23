from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)

db = SqliteDatabase('links')

from .views import *
