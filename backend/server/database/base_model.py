"""
db for base model

Author: Bingwei Chen
Date: 2017.07.20
"""
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


