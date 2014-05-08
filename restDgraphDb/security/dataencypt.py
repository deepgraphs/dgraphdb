__author__ = 'mpetyx'

from itsdangerous import JSONWebSignatureSerializer
from django.conf import settings

class jsonEncoder():

    def __init__(self,jsonObject):

        s = JSONWebSignatureSerializer(settings.SECRET_KEY)
        self.jsonObject = s.dumps(jsonObject)