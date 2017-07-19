from peewee import *

# db = MySQLDatabase('database_name', user='www-data', charset='utf8mb4')

# import os
# from playhouse.db_url import connect
# mysql://user:passwd@ip:port/my_db
# db = connect(os.environ.get('DATABASE') or 'sqlite:///default.db')



DATABASE = '/Users/chen/myPoject/gitRepo/Goku/backend/server/database/people.db'
database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database


# class User(BaseModel):
#     # id will generate by default
#     username = CharField(unique=True)
#     phone = CharField()
#     student_id = CharField()
#     # status：
#     status = IntegerField()
#     # school id
#     # school_id = ForeignKeyField(School, related_name="user_school")
#     # vc_id
#     # type
#     type = IntegerField()
#     wechat_id = CharField()
#     # battery_id
#     #start_date end_date ?meaning
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField()
#
#     # class Meta:
#     #     order_by = ('username',)
#
#
# database.connect()
# database.create_table(User)