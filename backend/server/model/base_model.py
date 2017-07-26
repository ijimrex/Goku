# encoding: utf-8

"""

@author:LeiJin

@file: base_model.py

@time: 7/24/17 6:50 PM

@desc:

"""
from peewee import *

database = MySQLDatabase('Goku', **{'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '123456'})
class BaseModel(Model):
    class Meta:
        database = database


    def get_info(self,query):
        '''
        通用的get_info方法，获取表中的所有内容
        :param query:
        :return:
        '''
        if query!=None:
            try:
                return self.get(**query)
            except:
                return -1
        else:
            return 0

    def add_record(self,query):
        '''
        增加一条新的记录
        :param query:
        :return:
        '''
        try:
            self.create(**query)
            return 1
        except:
            return -1

    def delete_record(self,query):
        '''
        删除记录
        :param query:where所指向的字段
        :return:
        '''
        print()
        try:
            st = self.get(**query)
            st.delete_instance()
            return 1
        except:
            return 0





