from flask import Flask
from peewee import SqliteDatabase
from models import Link

app = Flask(__name__)
db = SqliteDatabase('links')

Link.create_table()
from .views import *
