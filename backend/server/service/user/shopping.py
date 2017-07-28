# encoding: utf-8

"""

@author:LeiJin

@file: shopping.py

@time: 7/26/17 5:23 PM

@desc:
用户在商场中的操作

"""
from server.model.history_model import History
from server.model.appointment_model import Appointment
from server.model.bikemodel_model import *
from server.model.make_appointment_model import MakeAppointment
from server.service.user.user_basic import *
from server.service.common_service import *
from datetime import *



def get_ebike_models(category,page,offset,order,flag):
    '''
    获取某类ebike，并按照特定的关键词排序
    :param type:
    :param page:
    :param offset:
    :param order:
    :param flag: 0是正序，1是倒序
    :return:
    '''
    ebike_model=BikeModel()
    ebike_model_list=ebike_model.get_bikes_by_type(category,page,offset,order,flag)
    return ebike_model_list

def get_ebike_model_detail(id):
    '''
    查看一个model的车的详情
    :param id:
    :return:
    '''
    ebike_model=BikeModel()
    ebike_model_result=get_by_id(id,ebike_model)
    return ebike_model_result



def change_appointment_number(id,operate,num):
    pass


def modify_ebike_model(keyword,id,operate,value):
    '''
    改变已有的一个字段
    :param keyword: 更新的字段
    :param id:
    :param operate:
    :param num:
    :return:
    '''
    ebike_model = BikeModel()
    query={}
    ebike_model_result=get_ebike_model_detail(id)
    query['id']=id
    query['introduction']=ebike_model_result.introduction
    query['pics'] = ebike_model_result.pics
    query['color'] = ebike_model_result.color
    query['type'] = ebike_model_result.type
    query['price'] = ebike_model_result.price
    query['num_view']=ebike_model_result.num_view
    query['num_sold'] = ebike_model_result.num_sold
    query['left'] = ebike_model_result.left
    query['category'] = ebike_model_result.category

    if ebike_model_result != 0:
        if operate=='add':
            query[keyword]+=value
            # print( query)
        if operate=='minus':
            query[keyword]-=value
        if operate=='replace':
            query[keyword]=value
        return ebike_model.update_record(query)
    else:
        return -1

def create_appointment(ebike_model_id,user_id,note,appointment_type):
    '''

    :param ebike_model_id:模型
    :param user_id:
    :param note:
    :param appointment_type:
    :return:
    '''

    appointment_id=create_id(1)
    time_now=datetime.now()
    query={}#ebike
    query['user_id']=user_id
    query['model_id']=ebike_model_id
    query['id']=appointment_id
    query['note']=note
    query['type']=appointment_type
    query['date']=time_now
    query2={}#appointment
    query2['u']=user_id
    query2['a']=appointment_id
    query2['date']=time_now
    query3={}#history
    query3['id']=create_id(1)
    query3['bike_model_id']=ebike_model_id
    query3['user_id']=user_id
    query3['time']=time_now
    query3['operation']='make_appointment'
    query3['battery_id']=''
    query3['ebike_id']=''
    query3['fc_id']=''
    query3['fc_id_id']=''



    user=User()
    appointment=Appointment()
    appointment_made=MakeAppointment()
    history=History()
    ebike_model=BikeModel()
    ebike_model_result=get_by_id(ebike_model_id,ebike_model)
    if get_by_id(user_id,user).status=='1':
        if ebike_model_result.left==0:
            return 2
        else:
            modify_ebike_model('left', ebike_model_id, 'minus', 1)
            modify_user_one('status',user_id,'2')
            appointment.add_record(query)
            appointment_made.add_record(query2)
            print(history.add_record(query3))
        return 1
    else:
        return 0
print(create_appointment('001','03','yoyo','1'))
# print(modify_ebike_model('color','001','replace','black'))
# print (get_ebike_model_detail('001').color)
# print(g)
# for x in g:
#     print(type(x.num_view))
#     print(x.price)

# def reverse_sort(l):

# m=User()
# print(get_by_id('04',m).status)
# add_quert={'username':'abd', 'name':'Test', 'password':'12345', 'phone':1235, 'status':'1', 'vc_id':'001', 'student_id':'012', 'school_id':'001','id':'01' }
# print(m.add(add_quert))
# m.update_record(add_quert)
# m.add_user('c','b','123','1','001','001','07','001',915)
# g=m.get_info_several(1,10)
# print(g)
# for x in g:
#     print(x.name)