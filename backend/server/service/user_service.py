# -*- coding: UTF-8 -*-
"""
service for user

Author: Bingwei Chen
Date: 2017.07.20
"""
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from server.database.user import User


def add(username, password, kwargs):
    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password, **kwargs)
    return user.save()


def add_user(username, password, kwargs):
    user = User(username=username, password=password, **kwargs)
    return user.save()


def get_users_list():
    users = User.select()
    for user in users:
        print(user.username)

# def authenticate(user_ID, password):
#     user = user_business.get_by_user_ID(user_ID)
#     if user and check_password_hash(user.password, password):
#         user.id = str(user.id)
#         return user
#     return False

