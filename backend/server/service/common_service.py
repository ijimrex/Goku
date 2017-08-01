# encoding: utf-8

"""

@author:LeiJin

@file: common_service.py

@time: 7/27/17 1:43 PM

@desc:

"""
from server.model.base_model import *
def get_by_id(id,model):
    '''
    按照id查询一条记录的全部字段
    :param id:
    :param model:
    :return:
    '''

    query={}
    query['id']=id
    # print (model.get_info_one(query))
    return model.get_info_one(query)

def modify_all_by_id(id,para,model):
    '''
    通过id同时改变多个字段
    :param id:
    :param para:
    :return:
    '''
    query={}
    query['id']=id
    if not 'id' in para:
        query_send=dict(query,**para)
    else:
        query_send = para
    result=get_by_id(id,model)
    if result==0:
        return  -1
    else:
        return model.update_record(query_send)
def create_id(length):
    return '022'