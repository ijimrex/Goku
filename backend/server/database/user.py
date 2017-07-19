# -*- coding: UTF-8 -*-

from peewee import *
from server.database.base_model import BaseModel
from server.database.school import School


class User(BaseModel):
    # id will generate by default
    username = CharField(unique=True)
    phone = CharField()
    student_id = CharField()
    # status：
    # status = IntegerField()
    # school id
    # school_id = ForeignKeyField(School, related_name="user_school")
    # vc_id
    # type
    # type = IntegerField()
    # wechat_id = CharField()
    # battery_id
    #start_date end_date ?meaning
    password = CharField()
    # email = CharField()
    # join_date = DateTimeField()

    class Meta:
        order_by = ('username',)


def initialize():
    from server.database.base_model import database
    database.connect()
    database.create_table(User, safe=True)
    database.close()
