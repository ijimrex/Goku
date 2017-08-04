# encoding: utf-8

"""

@author:LeiJin

@file: store_model.py

@time: 7/24/17 6:52 PM

@desc:

"""
from server.model.base_model import *


class Store(BaseModel):
    address = CharField(unique=True)
    id = CharField(primary_key=True)
    name = CharField(unique=True)

    class Meta:
        db_table = 'store'

    def update_record(self, query):
        '''
        修改记录
        :param query:
        :return:
        '''
        try:
            temp = Store(**query)
            temp.save()
            return 1
        except:
            return -1
