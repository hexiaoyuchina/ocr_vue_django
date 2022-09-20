# -*- coding:utf-8 -*-
import os
import uuid
from ctpn.detect import detect
from crnn.recoginze_image import recognition

class RegcongizeService(object):
    def __init__(self, file_name='', file_path='', file_uuid='', *args, **kwargs):
        self.file_name = file_name
        self.file_path = file_path
        self.file_uuid = file_uuid

    def reg_imge(self, request):
        # image_file = serializer_data.get('file',None)
        image_file = request.FILES.get("file", None)

        _, ext = os.path.splitext(image_file.name)
        if not ext or ext not in ['.jpg', '.JPG', '.png', '.PNG']:
            return Response({"msg": "文件格式不支持"})
        self.file_uuid = str(uuid.uuid1())
        self.file_name = image_file.name
        if 'detect_reg' in self.file_name or 'detect' in self.file_name:
            self.file_name = 'index' + self.file_name

        file_dir = os.path.abspath('static/' + self.file_uuid)

        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        self.file_path = os.path.join(file_dir, self.file_name)

        save_path = open(self.file_path, 'wb+')
        for chunk in image_file.chunks():
            save_path.write(chunk)
        save_path.close()

        detect(self.file_path)
        recognition(self.file_path)
        return {"msg": "识别成功", 'file_uuid': self.file_uuid, 'file_name': self.file_name}