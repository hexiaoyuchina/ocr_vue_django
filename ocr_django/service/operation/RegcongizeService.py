# -*- coding:utf-8 -*-

from ctpn.detect import detect
from crnn.recoginze_image import recognition

class RegcongizeService(object):
    def __init__(self, file_name, file_path='', file_uuid='', *args, **kwargs):
        self.file_name = file_name
        self.file_path = file_path
        self.file_uuid = file_uuid

    def reg_imge(self, request):
        detect(self.file_path)
        recognition(self.file_path)
        return {"msg": "成功"}