# coding: utf-8

import hashlib, json
import urlparse
import urllib
import sys
from config import *
import requests


class UCLOUDException(Exception):
    def __str__(self):
        return "Error"


def _verfy_ac(private_key, params):
    items = params.items()
    items.sort()

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)

    params_data = params_data + private_key

    '''use sha1 to encode keys'''
    hash_new = hashlib.sha1()
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value


class UConnection(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, resouse, params):
        resouse += "?" + urllib.urlencode(params)

        url = "%s%s" % (self.base_url, resouse)
        print (url)
        response = requests.get(url=url).json()
        return response


class UcloudApiClient(object):
    # 初始化配置
    def __init__(self,  base_url, public_key, private_key, project_id):
        self.g_params = {}
        self.g_params['PublicKey'] = public_key
        self.private_key = private_key
        self.conn = UConnection(base_url)

    def get(self, uri, params):
        _params = dict(self.g_params, **params)

        if project_id:
            _params["ProjectId"] = project_id

        _params["Signature"] = _verfy_ac(self.private_key, _params)

        return self.conn.get(uri, _params)