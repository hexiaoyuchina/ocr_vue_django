# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from service.RegcongizeService import RegcongizeService

class RegeViewSets(viewsets.GenericViewSet):
    @action(methods=['POST'], detail=False, url_path='reg_image')
    def reg_image(self, request, *args, **kwargs):
        action = RegcongizeService()
        res = action.reg_imge(request)
        return Response(res)
