# encoding: utf-8

"""

@author:LeiJin

@file: bike_basic.py

@time: 8/1/17 2:29 PM

@desc:

"""
from server.model.bikemodel_model import BikeModel
from server.model.ebike_model import Ebike
from server.service.common_service import get_by_id


def get_ebike_models(category, page, offset, order, flag):
    '''
    获取某类ebike，并按照特定的关键词排序
    :param category:车的大分类 比如 小龟
    :param page:数据库分页
    :param offset:分页限制
    :param order:按什么排序
    :param flag: 0是正序，1是倒序
    :return:
    '''
    ebike_model = BikeModel()
    ebike_model_list = ebike_model.get_bikes_by_type(category, page, offset, order, flag)
    return ebike_model_list


def get_ebike_model_id_by_ebike_id(id):
    '''
    通过ebike的编号获取对应模型的编号
    :param id:ebike的id
    :return:ebike_model的编号
    '''
    ebike = Ebike()
    ebike_result = get_by_id(id, ebike)
    return ebike_result.model_id.id


def get_ebike_model_detail(id):
    '''
    查看一个model的车的详情
    :param id:ebike_model 的id
    :return:ebike_model所有字段
    '''
    ebike_model = BikeModel()
    ebike_model_result = get_by_id(id, ebike_model)
    return ebike_model_result


def modify_ebike_model(keyword, id, operate, value):
    '''
    改变已有的一个字段
    :param keyword: 更新的字段
    :param id:ebike model的id
    :param operate:对操作类型
    :param value: 修改字段变化的值
    :return:
    '''
    ebike_model = BikeModel()
    query = {}
    ebike_model_result = get_ebike_model_detail(id)
    query['id'] = id
    query['introduction'] = ebike_model_result.introduction
    query['pics'] = ebike_model_result.pics
    query['color'] = ebike_model_result.color
    query['type'] = ebike_model_result.type
    query['price'] = ebike_model_result.price
    query['num_view'] = ebike_model_result.num_view
    query['num_sold'] = ebike_model_result.num_sold
    query['left'] = ebike_model_result.left
    query['category'] = ebike_model_result.category

    if ebike_model_result != 0:
        if operate == 'add':
            query[keyword] += value
            # print( query)
        if operate == 'minus':
            query[keyword] -= value
        if operate == 'replace':
            query[keyword] = value
        return ebike_model.update_record(query)
    else:
        return -1


def modify_ebike(id, keyword, value):
    '''
    修改ebike中的一个字段
    :param id:ebike的的id
    :param keyword:修改的字段名
    :param value:修改的字段的新值
    :return:
    '''
    ebike = Ebike()
    ebike_result = get_by_id(id, ebike)
    query = {}
    query['id'] = id
    query['model_id'] = ebike_result.model_id
    query['user_id'] = ebike_result.user_id
    query['date'] = ebike_result.date
    query['status'] = ebike_result.status
    query[keyword] = value
    if ebike_result != 0:
        return ebike.update_record(query)
    else:
        return 0
