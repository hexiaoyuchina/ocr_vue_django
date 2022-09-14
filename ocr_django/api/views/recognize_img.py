# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.response import Response
from service.RegcongizeService import RegcongizeService

class RegeViewSets(viewsets.GenericViewSet):
    @action(methods=['POST'], detail=False, url_path='reg_image')
    def reg_image(self, request, *args, **kwargs):
        action = RegcongizeService()
        res = action.reg_imge(request)
        # image_data = open(imagepath, "rb").read()
        # return HttpResponse(image_data, content_type="image/png")
        return Response(res)
