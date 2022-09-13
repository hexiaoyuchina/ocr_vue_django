# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from api.views import recognize_img

router = SimpleRouter()

router.register(r'reg_img', recognize_img.RegeViewSets, basename='reg_img')
