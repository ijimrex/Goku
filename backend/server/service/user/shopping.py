# encoding: utf-8

"""

@author:LeiJin

@file: shopping.py

@time: 7/26/17 5:23 PM

@desc:
用户在商场中的操作

"""
from server.model.bikemodel_model import *
from server.service.common_service import *

def get_ebikes(type,page,offset,order,flag):
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
    ebike_list=ebike.get_bikes_by_type(type,page,offset,order,flag)
    return ebike_list

def get_ebike_detail(id):

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
    e_keys=query.keys()
    # print(e_keys)
    if ebike_result != 0:
        for e_key in e_keys:
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

def make_appointment(id):
    ebike=BikeModel()
    ebike_result=get_by_id(id,ebike)

print(modify_ebike('color','001','replace','white'))





# print (get_ebike_detail('001'))
# print(g)
# for x in g:
#     print(type(x.num_view))
#     print(x.price)

# def reverse_sort(l):