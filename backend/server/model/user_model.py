# encoding: utf-8

"""

@author:LeiJin

@file: user_model.py

@time: 7/24/17 7:12 PM

@desc:

"""
from server.model.base_model import *
from server.model.school_model import School
from server.model.virtual_card_model import VirtualCard

class User(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    password = CharField()
    phone = IntegerField(null=True)
    school_id = ForeignKeyField(db_column='school_id', rel_model=School, to_field='id')
    status = CharField()
    student_id = CharField(db_column='student_id')
    username = CharField(unique=True)
    vc_id = ForeignKeyField(db_column='vc_id', null=True, rel_model=VirtualCard, to_field='id')

    class Meta:
        db_table = 'user'

    def get_user(self,id):
        '''
        获取用户在user表中的全部信息
        :param id:用户的id
        :return:info object
        '''
        if id!=None:
            return User.get(User.id==id)
        else:
            return None

    def get_user_list(self,page,limit):
        '''
        显示用户列表，for admin
        :param page: 分几页
        :param limit: 每页多少条
        :return:diclist 显示用户基本信息
        '''
        None

    def add_user(self,username,name,password,phone,status,vc_id,student_id,school_id,id):
        temp=User(username=username, name=name,password=password,phone=phone,status=status,vc_id=vc_id,student_id=student_id,id=id,school_id=school_id)
        temp.save()







m=User()
# m.add_user('a','b','123',917,'1','001','001','02','002')
print(m.get_user('001'))