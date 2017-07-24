# encoding: utf-8

"""

@author:LeiJin

@file: appointment.py

@time: 7/24/17 7:13 PM

@desc:

"""
from server.model.base_model import *

class Appointment(BaseModel):
    date = DateTimeField()
    id = CharField(primary_key=True)
    model = ForeignKeyField(db_column='model_id', null=True, rel_model=Model, to_field='id')
    note = CharField(null=True)
    type = CharField(null=True)
    user = ForeignKeyField(db_column='user_id', null=True, rel_model=User, to_field='id')

    class Meta:
        db_table = 'appointment'