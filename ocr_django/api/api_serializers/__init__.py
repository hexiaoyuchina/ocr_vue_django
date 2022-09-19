# -*- coding:utf-8 -*-
import logging
from django.utils import translation
from django.conf import settings

from rest_framework.response import Response
logger = logging.getLogger(__name__)

def api_serializer_deco(api_msg):

    def _wrapper(func):
        def deco(*args, **kwargs):
            try:
                obj = args[0]
                req = args[1]
                language = req.META.get("HTTP_ACCEPT_LANGUAGE")
                if language != 'en':
                    language = 'zh-hans'
                req.LANGUAGE_CODE = language
                logger.info("req.LANGUAGE_CODE: %s" % req.LANGUAGE_CODE)
                settings.LANGUAGE_CODE = req.LANGUAGE_CODE

                if req.META.get("HTTP_USER_IP", None):
                    user_ip = req.META.get("HTTP_USER_IP")
                else:
                    user_ip = req.META.get("HTTP_X_FORWARDED_FOR")
                    user_ip = user_ip.split(',')[0] if user_ip else ''

                settings.USER_REAL_IP = user_ip
                logger.info("user real ip: %s" % settings.USER_REAL_IP)
                settings.CURRENT_DEFAULT_LANGUAGE = req.LANGUAGE_CODE

                translation.activate(language)

                req_dict = {
                    "GET": req.GET.dict(),
                    "POST": req.data,
                    "PUT": req.data,
                    "DELETE": req.data
                }
                obj_serializer = None
                if obj.serializer_class:
                    obj_serializer = obj.get_serializer(data=req_dict.get(req.method))

                # if not obj_serializer.is_valid() and req.method.lower() == "get":
                #     obj_serializer = obj.get_serializer(data=req.GET)

                if obj_serializer.is_valid():
                    serializer_data = obj_serializer.data
                    kwargs['serializer_data'] = serializer_data
                res = func(*args, **kwargs)

            except Exception as ex:
                msg = u'%s异常：%s' % (api_msg, ex)
                logger.error(msg, exc_info=True)
                res = {
                    'code': '9000',
                    'code_msg': '失败',
                    'message': msg
                }
            logger.info(u'%s返回结果:%s' % (api_msg, res))
            return Response(res)
        return deco
    return _wrapper
