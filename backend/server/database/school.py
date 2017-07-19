# -*- coding: UTF-8 -*-

from peewee import *
from server.database.base_model import BaseModel


class School(BaseModel):
    name = CharField(unique=True)
    address = CharField()
    # store_id
