# encoding: utf-8

"""

@author:LeiJin

@file: ebike_model.py

@time: 7/24/17 7:23 PM

@desc:

"""
from server.model.base_model import *
from server.model.virtual_card_model import VirtualCard


class Ebike(BaseModel):
    id = CharField(primary_key=True)
    model = ForeignKeyField(db_column='model_id', rel_model=Model, to_field='id')
    state = CharField()
    vcid = ForeignKeyField(db_column='vcid', null=True, rel_model=VirtualCard, to_field='id')

    class Meta:
        db_table = 'ebike'