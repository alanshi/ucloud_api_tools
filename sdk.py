# coding: utf-8

import hashlib
import urlparse
import urllib
import requests


class UcloudApiClient(object):
    # 初始化配置
    def __init__(self,  base_url, public_key, private_key, project_id):
        self.g_params = {}
        self.g_params['ProjectId'] = project_id
        self.g_params['PublicKey'] = public_key
        self.private_key = private_key
        self.base_url = base_url

    def _verfy_ac(self, private_key, params):
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

    def _request(self, params):
        resouse = "?" + urllib.urlencode(params)
        url = "%s/%s" % (self.base_url, resouse)
        print (url)
        response = requests.get(url=url).json()
        return response

    def get(self, params):
        _params = dict(self.g_params, **params)
        _params["Signature"] = self._verfy_ac(self.private_key, _params)

        return self._request(_params)
