# encoding: utf-8

"""

@author:LeiJin

@file: base_model.py

@time: 7/24/17 6:50 PM

@desc:

"""
from peewee import *

database = MySQLDatabase('Goku', **{'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '123456'})
class BaseModel(Model):
    class Meta:
        database = database

class Model(BaseModel):
    color = CharField(null=True)
    id = CharField(primary_key=True)
    introduction = CharField(null=True)
    num_sold = IntegerField()
    num_view = IntegerField()
    pics = CharField(null=True)
    price = FloatField()
    type = CharField()

    class Meta:
        db_table = 'model'