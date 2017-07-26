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
    return user.get_info(id)
# print (get_info('001'))

def get_user_list():
    '''
    获取所用用户列表
    :return:
    '''


def add_user(username, name, password, phone, status, vc_id, student_id, school_id, id):
    '''
    新增用户
    :param s:
    :return:
    '''
    user=User()
    user_result = user.get_info(username)
    if user_result!=0 and user_result!=-1:
        return -1
    try:
        query=create_query(username, name, password, phone, status, vc_id, student_id, school_id, id)
        user.add_record(query)
        return 1
    except:
        return 0


def login(username,password):
    '''
    登录
    :param username:
    :param password:
    :return:success1/no username 0,-1/no password -2
    '''
    user=User()
    user_result=user.get_info(username)
    if user_result==0 or user_result==-1:
        return user_result
    else:
        psw=user_result.password
        if psw==password:
            return 1
        else:
            return -2


def delete_user_permentally(id):
    '''
    按照id永久删除一个user
    :param id:
    :return:
    '''
    query={}
    query['id']=id
    user=User()
    user_result=user.get_info(query)
    if user_result==0 or user_result==-1:
        return user_result
    else:
        return user.delete_record(query)

# def modify_user_info()


def create_query(username, name, password, phone, status, vc_id, student_id, school_id, id):
    '''
    构建查询的字典
    :param username:
    :param name:
    :param password:
    :param phone:
    :param status:
    :param vc_id:
    :param student_id:
    :param school_id:
    :param id:
    :return:字典
    '''
    query = {}
    query['username'] = username
    query['name'] = name
    query['password'] = password
    query['phone'] = phone
    query['status'] = status
    query['vc_id'] = vc_id
    query['student_id'] = student_id
    query['school_id'] = school_id
    query['id'] = id
    return query


# print(delete_user_permentally('04'))
# def update_user()
# print(login({'username':'c'},'123'))
# add_quert={'username':'abc', 'name':'Test', 'password':'12345', 'phone':123, 'status':'1', 'vc_id':'001', 'student_id':'012', 'school_id':'001','id':1 }
# print(add_user('b','b','123',123,'001','001','04','001','04'))

