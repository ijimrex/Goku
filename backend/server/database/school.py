# -*- coding: UTF-8 -*-

from peewee import *
from server.database.base_model import BaseModel


class School(BaseModel):
    name = CharField(unique=True)
    address = CharField()
    # store_id


def initialize():
    from server.database.base_model import database
    database.connect()
    database.create_table(School, safe=True)
    database.close()