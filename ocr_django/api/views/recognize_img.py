# -*- coding: utf-8 -*-
import os
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from service.operation.RegcongizeService import RegcongizeService
from service.resource.RegcongizeResource import RegcongizeResource
from api.api_serializers import api_serializer_deco
from api.api_serializers.RegimageSerializer import WordIndexSerializer,RegImageSerializer


class RegeViewSets(viewsets.GenericViewSet):
    @action(methods=['POST'], detail=False, url_path='reg_image', serializer_class=RegImageSerializer)
    @api_serializer_deco('识别')
    def reg_image(self, request, serializer_data=None):
        action = RegcongizeService()
        res = action.reg_imge(request)
        return res

    @action(methods=['POST'], detail=False, url_path='get_word_index', serializer_class=WordIndexSerializer)
    @api_serializer_deco('获取文字及坐标结果')
    def show_res(self, request, serializer_data=None):
        resourece = RegcongizeResource(file_uuid=serializer_data.get('file_uuid'))
        return resourece.get_word_index()
