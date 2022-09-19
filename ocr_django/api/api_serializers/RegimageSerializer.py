# -*- coding: utf-8 -*-

from rest_framework import serializers

class ShowImageSerializer(serializers.Serializer):
    file_uuid = serializers.CharField()
