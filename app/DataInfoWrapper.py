# -*- coding: utf-8 -*-
import ujson

from dss import Serializer
from django.core.paginator import Page
from django.db.models.query import QuerySet

#Info Code
ERROR_UNKNOWN = 0
INFO_SUCCESS = 1
ERROR_FAILED = 2
ERROR_PASSWORD = 3
ERROR_VERIFY = 4
INFO_NO_VERIFY = 5
ERROR_TIME_OUT = 6
INFO_EXISTED = 7
INFO_NO_EXIST = 8
ERROR_PERMISSION_DENIED = 10


def wrapper(status_code=INFO_SUCCESS, data_list=None, message='success', return_format='dict'):
    return_data = {}
    if data_list:
        if isinstance(data_list, str):
            try:
                data_list = ujson.loads(data_list)
            except ValueError, e:
                pass
            except Exception, e:
                print e
        elif isinstance(data_list, (QuerySet, Page)):
            data_list = Serializer.serializer(data_list, 'string', deep=True)
    return_data['status'] = status_code
    return_data['msg'] = message
    return_data['body'] = data_list
    if return_format == 'dict':
        return return_data
    elif return_format == 'json':
        return ujson.dumps(return_data)
    else:
        return return_data





