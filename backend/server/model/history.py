# encoding: utf-8

"""

@author:LeiJin

@file: history.py

@time: 7/24/17 7:24 PM

@desc:

"""
from server.model.base_model import *
class History(BaseModel):
    ebike = ForeignKeyField(db_column='ebike_id', null=True, rel_model=Ebike, to_field='id')
    fc = ForeignKeyField(db_column='fc_id', null=True, rel_model=FlashCharge, to_field='id')
    id = CharField(primary_key=True)
    time = DateTimeField()
    vc = ForeignKeyField(db_column='vc_id', null=True, rel_model=VirtualCard, to_field='id')

    class Meta:
        db_table = 'history'