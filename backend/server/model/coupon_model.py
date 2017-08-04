# encoding: utf-8

"""

@author:LeiJin

@file: coupon_model.py

@time: 7/24/17 7:15 PM

@desc:

"""

from server.model.base_model import *

class Coupon(BaseModel):
    date = DateTimeField()
    description = CharField(null=True)
    id = CharField(primary_key=True)
    money = FloatField(null=True)
    name = CharField()
    type = CharField()

    class Meta:
        db_table = 'coupon'

    def update_record(self,query):
        '''
        :param query:
        :return:
        '''
        try:
            temp = Coupon(**query)
            temp.save()
            return 1
        except:
            return -1
