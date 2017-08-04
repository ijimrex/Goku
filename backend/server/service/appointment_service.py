# encoding: utf-8

"""

@author:LeiJin

@file: appointment_service.py

@time: 8/3/17 2:27 PM

@desc:

"""
import datetime
from server.model.appointment_model import Appointment
from server.model.bikemodel_model import BikeModel
from server.model.history_model import History
from server.model.make_appointment_model import MakeAppointment
from server.model.user_model import User
from server.service.common_service import create_id, get_by_id
from server.service.user.bike_basic import modify_ebike_model
from server.service.user.user_basic import modify_user_one


def create_appointment(ebike_model_id, user_id, note, appointment_type):
    '''
    增加预约信息
    修改user bikemodel ebike appointment makeappointment表
    :param ebike_model_id:模型
    :param user_id:
    :param note:预约的时候填的备注信息
    :param appointment_type:预约类型：租车？买车
    :return:
    '''

    appointment_id = create_id(1)
    time_now = datetime.datetime.now()
    query = {}  # appointment
    query['user_id'] = user_id
    query['model_id'] = ebike_model_id
    query['id'] = appointment_id
    query['note'] = note
    query['type'] = appointment_type
    query['date'] = time_now
    query['status'] = 0
    query3 = {}  # history
    query3['id'] = create_id(1)
    query3['bike_model_id'] = ebike_model_id
    query3['user_id'] = user_id
    query3['time'] = time_now
    query3['operation'] = 'make_appointment'
    query3['battery_id'] = '001'
    query3['ebike_id'] = '001'
    query3['fc_id'] = '001'
    user = User()
    appointment = Appointment()
    history = History()
    ebike_model = BikeModel()
    ebike_model_result = get_by_id(ebike_model_id, ebike_model)
    if get_by_id(user_id, user).status == '1':  # 是否可约
        if ebike_model_result.left == 0:  # 车辆是否数量大于0
            return 2
        else:
            modify_ebike_model('left', ebike_model_id, 'minus', 1)
            modify_user_one('status', user_id, '2')
            appointment.add_record(query)
            history.add_record(query3)
        return 1
    else:
        return 0


def change_appointment_status(model_id, user_id):
    '''
    把原本的预约状态未完成0改成已完成 1
    :param model_id:电动车模型id
    :param user_id:用户id
    :return:
    '''
    print( model_id)
    print(user_id)
    appointment = Appointment()
    appointment_result = Appointment.select().where(
        (Appointment.user_id == user_id) & (Appointment.model_id == model_id) & (Appointment.status == '0')).get()
    query = {'model_id': model_id, 'user_id': user_id, 'status': 1, 'id': appointment_result.id}
    return appointment.update_record(query)


# create_appointment('001', '4', 'ok', '2')
# print(change_appointment_status('001', '03'))


