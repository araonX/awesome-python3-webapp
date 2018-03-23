#!/home/xiejg/awesome-python3-webapp/env/bin/python3.5

'''
JSON API definition
'''

import json,logging,inspect,functools

class APIError(Exception):
    '''
      the base APIError which contains error(required),data(optional) and message(optional)
    '''
    def __init__(self,field,message=''):
        super(APIValueError,self).__init__('value:invalid',field,message)
class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. the data specifies the resource name.
    '''
    def __init__(self,field,message=''):
        super(APIResourceNotFoundError,self).__init__('value:notfound',field,message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self,message=''):
        super(APIPermissionError,self).__init__('permission:forbidden','permission',message)
