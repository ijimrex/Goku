# encoding: utf-8

"""

@author:LeiJin

@file: user.py

@time: 7/24/17 7:12 PM

@desc:

"""
from server.model.base_model import *

class User(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    phone = IntegerField(null=True)
    school = ForeignKeyField(db_column='school_id', rel_model=School, to_field='id')
    status = CharField()
    student = CharField(db_column='student_id')
    vc = ForeignKeyField(db_column='vc_id', null=True, rel_model=VirtualCard, to_field='id')

    class Meta:
        db_table = 'user'