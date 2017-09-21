# coding: utf-8

from sdk import UcloudApiClient
from config import *


class UCloudAPI(object):

    def __init__(self):

        self.api_client = UcloudApiClient(base_url, public_key,  private_key, project_id)

    def request(self, **kwargs):
        return self.api_client.get(kwargs)


if __name__ == '__main__':

    ucloud_api = UCloudAPI()

    # 范例 获取实例vnc信息
    data = {
        'Region': 'cn-bj2',
        'Zone': 'cn-bj2-04',
        'UHostId': 'uhost-r4oawd'
    }

    print ucloud_api.request(
        Action='GetUHostInstanceVncInfo',
        **data
    )
