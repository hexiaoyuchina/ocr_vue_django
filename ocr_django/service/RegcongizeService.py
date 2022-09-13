# -*- coding:utf-8 -*-

from ctpn.detect import detect
from crnn.recoginze_image import recognition
class RegcongizeService(object):
    # def __init__(self, *args, **kwargs):
    def reg_imge(self, request):
        detect()
        recognition()
        return {"msg": "成功"}