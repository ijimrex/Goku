# encoding: utf-8

"""

@author:LeiJin

@file: user_basic.py

@time: 7/25/17 11:23 AM

@desc:用户基本信息操作：
查看个人信息
修改个人信息
注册

"""
from server.model.user_model import User

def get_user_info(id):
    '''
     查看用户的信息
    :return:
    '''
    user=User()
    return user.get_user(id)
# print (get_info('001'))

def get_user_list():
    '''
    获取所用用户列表
    :return:
    '''


# def add_user(s):



