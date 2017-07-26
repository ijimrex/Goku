# encoding: utf-8

"""

@author:LeiJin

@file: bikemodel_model.py

@time: 7/26/17 11:08 AM

@desc:

"""
from server.model.base_model import *


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
