# encoding: utf-8

"""

@author:LeiJin

@file: shopping.py

@time: 7/26/17 5:23 PM

@desc:
用户在商场中的操作

"""
from server.service.user.bike_basic import *
from server.service.appointment_service import *
from server.service.common_service import *


def change_appointment_number(id, operate, num):
    pass


def pick_bike(bike_id, user_id):
    '''
    提车，输入ebike的id
    :param bike_id:输入的电动车id
    :param user_id: 用户id
    :return:
    '''
    try:
        modify_user_one('status', user_id, 1)
        model_id = get_ebike_model_id_by_ebike_id(bike_id)
        modify_ebike_model('num_sold', model_id, 'plus', 1)
        modify_ebike(bike_id, 'user_id', user_id)
        ebike_model=get_by_id(bike_id,Ebike())
        change_appointment_status(ebike_model.model_id.id,user_id)
        h=History()
        h.add_history(user_id,'ebike_id',bike_id,'1')
        return 1
    except:
        return 0



















    # print(create_appointment('001','01','yoyo','1'))
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
