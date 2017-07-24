# encoding: utf-8

"""

@author:LeiJin

@file: flashCharge.py

@time: 7/24/17 7:23 PM

@desc:

"""
from server.model.base_model import *
class FlashCharge(BaseModel):
    battery = ForeignKeyField(db_column='battery_id', null=True, rel_model=Battery, to_field='id')
    date = DateTimeField()
    id = CharField(primary_key=True)
    status = CharField()
    vc = ForeignKeyField(db_column='vc_id', null=True, rel_model=VirtualCard, to_field='id')

    class Meta:
        db_table = 'flash_charge'