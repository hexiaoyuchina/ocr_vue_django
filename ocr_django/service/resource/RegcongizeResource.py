# -*- coding: utf-8 -*-

class RegcongizeResource(object):
    def __init__(self, file_uuid='', file_name='', *args, **kwargs):
        self.file_uuid = file_uuid
        self.file_name = file_name
    def get_word_index(self):
        return {'message':'xxx'}