# encoding: utf-8

"""

@author:LeiJin

@file: history_model.py

@time: 7/24/17 7:24 PM

@desc:

"""
from datetime import *



from server.database.user import User
from server.model.base_model import *
from server.model.battery_model import Battery
from server.model.bikemodel_model import BikeModel
from server.model.ebike_model import Ebike



class History(BaseModel):
    battery_id = ForeignKeyField(db_column='battery_id', null=True, rel_model=Battery, to_field='id')
    bike_model_id = ForeignKeyField(db_column='bike_model_id', null=True, rel_model=Ebike, to_field='id')
    ebike_id = CharField(db_column='ebike_id', null=True)
    id = CharField(primary_key=True)
    operation = CharField()
    time = DateTimeField()
    user_id = ForeignKeyField(db_column='user_id', null=True, rel_model=User, related_name='user_user_set', to_field='id')

    class Meta:
        db_table = 'history'

time_now=datetime.now()
m=History()
# print( time_now)

query3={}#history
query3['id']='226'
query3['bike_model_id']='001'
query3['user_id']='03'
query3['time']=time_now
query3['operation']='make_appointment'
query3['battery_id']='001'
query3['ebike_id']='001'
# print( query3)
m.add_record(query3)
