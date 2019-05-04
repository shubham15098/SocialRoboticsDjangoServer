from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):

    # user will be able to post these field in our database
    # this can be any, abc, xyz, upto you
    # you will collect this in views.py ka post wala method



    myString = serializers.CharField()