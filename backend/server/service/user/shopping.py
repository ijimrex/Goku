# encoding: utf-8

"""

@author:LeiJin

@file: shopping.py

@time: 7/26/17 5:23 PM

@desc:
用户在商场中的操作

"""
from server.database.db_map import History
from server.model.appointment_model import Appointment
from server.model.bikemodel_model import *
from server.model.make_appointment_model import MakeAppointment
from server.service.user.user_basic import *
from server.service.common_service import *
from datetime import *



def get_ebikes(category,page,offset,order,flag):
    '''
    获取某类ebike，并按照特定的关键词排序
    :param type:
    :param page:
    :param offset:
    :param order:
    :param flag: 0是正序，1是倒序
    :return:
    '''
    ebike=BikeModel()
    ebike_list=ebike.get_bikes_by_type(category,page,offset,order,flag)
    return ebike_list

def get_ebike_detail(id):
    '''
    查看一个model的车的详情
    :param id:
    :return:
    '''
    ebike=BikeModel()
    ebike_result=get_by_id(id,ebike)
    return ebike_result



def change_appointment_number(id,operate,num):
    pass


def modify_ebike(keyword,id,operate,value):
    '''
    改变已有的一个字段
    :param keyword: 更新的字段
    :param id:
    :param operate:
    :param num:
    :return:
    '''
    ebike = BikeModel()
    query={}
    ebike_result=get_ebike_detail(id)
    query['id']=id
    query['introduction']=ebike_result.introduction
    query['pics'] = ebike_result.pics
    query['color'] = ebike_result.color
    query['type'] = ebike_result.type
    query['price'] = ebike_result.price
    query['num_view']=ebike_result.num_view
    query['num_sold'] = ebike_result.num_sold
    query['left'] = ebike_result.left
    query['category'] = ebike_result.category

    if ebike_result != 0:
        if operate=='add':
            query[keyword]+=value
            # print( query)
        if operate=='minus':
            query[keyword]+=value
        if operate=='replace':
            query[keyword]=value
        return ebike.update_record(query)
    else:
        return -1

def create_appointment(ebike_id,user_id,note,appointment_type):
    '''
    下单预约
    :param id:车辆model编号
    :return:
    '''
    # ebike = ForeignKeyField(db_column='ebike_id', null=True, rel_model=Ebike, to_field='id')
    # fc = ForeignKeyField(db_column='fc_id', null=True, rel_model=FlashCharge, to_field='id')
    # id = CharField(primary_key=True)
    # time = DateTimeField()
    # vc = ForeignKeyField(db_column='vc_id', null=True, rel_model=VirtualCard, to_field='id')
    # operation=CharField()
    # model_id = ForeignKeyField(db_column='model_id', null=True, rel_model=BikeModel, to_field='id')




    appointment_id=create_id(1)
    time_now=datetime.now()
    query={}#ebike
    query['user_id']=user_id
    query['model_id']=ebike_id
    query['id']=appointment_id
    query['note']=note
    query['type']=appointment_type
    query['date']=time_now
    query2={}#appointment
    query2['u']=user_id
    query2['a']=appointment_id
    query2['date']=time_now
    # query3={}#history
    # query3['id']=create_id()
    # query3['']
    user=User()
    appointment=Appointment()
    appointment_made=MakeAppointment()
    history=History()
    ebike=BikeModel()
    ebike_result=get_by_id(ebike_id,ebike)
    if get_by_id(user_id,user).status=='1':
        if ebike_result.left==0:
            return 2
        else:
            modify_ebike('left', ebike_id, 'minus', 1)
            modify_user_one('status',user_id,'2')
            appointment.add_record(query)
            appointment_made.add_record(query2)
        return 1
    else:
        return 0
# print(create_appointment('001','01','haha','1'))
# print(modify_ebike('color','001','replace','black'))
# print (get_ebike_detail('001'))
# print(g)
# for x in g:
#     print(type(x.num_view))
#     print(x.price)

# def reverse_sort(l):