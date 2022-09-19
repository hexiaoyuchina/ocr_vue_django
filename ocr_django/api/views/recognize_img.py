# -*- coding: utf-8 -*-
import os
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from service.operation.RegcongizeService import RegcongizeService
from service.resource.RegcongizeResource import RegcongizeResource
from api.api_serializers import api_serializer_deco
from api.api_serializers.RegImage.RegimageSerializer import ShowImageSerializer
import uuid

class RegeViewSets(viewsets.GenericViewSet):
    @action(methods=['POST'], detail=False, url_path='reg_image')
    @api_serializer_deco('识别')
    def reg_image(self, request, *args, **kwargs):

        image_file = request.FILES.get("file", None)
        if image_file:
            _,ext = os.path.splitext(image_file.name)
            if not ext or ext not in ['.jpg', '.JPG', '.png', '.PNG']:
                return Response({"msg": "文件格式不支持"})
            uuids = str(uuid.uuid1())
            file_name = image_file.name
            if 'detect_reg' in file_name or 'detect' in file_name:
                file_name = 'index' + file_name

            file_dir = os.path.abspath('data/' + uuids)

            if not os.path.exists(file_dir):
                os.mkdir(file_dir)

            file_path = os.path.join(file_dir, file_name)

            save_path = open(file_path, 'wb+')
            for chunk in image_file.chunks():
                save_path.write(chunk)
            save_path.close()

            action = RegcongizeService(file_name=file_name, file_path=file_path, file_uuid=uuids)
            res = action.reg_imge(request)
            res.update({'file_uuid': uuids})
            # image_data = open(imagepath, "rb").read()
            # return HttpResponse(image_data, content_type="image/png")
        return res

    @action(methods=['POST'], detail=False, url_path='show_res', serializer_class=ShowImageSerializer )
    @api_serializer_deco('获取识别结果')
    def show_res(self, request,  serializer_data=None):
        resourece = RegcongizeResource(serializer_data.get('file_id'))
        return resourece.get_res_image()


