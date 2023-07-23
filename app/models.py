from peewee import Model, CharField

from app import db
from .settings import DOMAIN


class Link(Model):
    short_url = CharField()
    long_url = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{DOMAIN}/{self.short_url}'
