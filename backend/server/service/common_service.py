# encoding: utf-8

"""

@author:LeiJin

@file: common_service.py

@time: 7/27/17 1:43 PM

@desc:

"""
from server.model.base_model import *
def get_by_id(id,model):
    query={}
    query['id']=id
    return model.get_info_one(query)