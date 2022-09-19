# -*- coding: utf-8 -*-

from rest_framework import serializers

class RegImageSerializer(serializers.Serializer):
    file = serializers.ImageField()

class ShowImageSerializer(serializers.Serializer):
    file_uuid = serializers.CharField()
