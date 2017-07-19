from peewee import *

DATABASE = 'people.db'
database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database
