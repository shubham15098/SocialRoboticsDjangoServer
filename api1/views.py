from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models
from django.http import HttpResponse

from rest_framework import status, viewsets
import pyrebase
import os
import requests
import time

config = {
                "apiKey": "AIzaSyDvYeT0HMa1j6ZqWeUYvyF9BZQNpYxFgFg",
                "authDomain": "otd-delhi-diagnostics.firebaseapp.com",
                "databaseURL": "https://otd-delhi-diagnostics.firebaseio.com",
                "storageBucket": "otd-delhi-diagnostics.appspot.com"
            }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create your views here.
class TokenizerViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    # we can use same serializer here as well
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        # same as get of apiview
        a_viewset = [
            'Social Robotics',
            'Web robot control',
            'Parser',
        ]

        return Response({'message': a_viewset})

        # with open('media/admin@gmail.com/myFirstProject/preprocessGraph1.png', 'rb') as fh:
        #     return HttpResponse(fh.read(), content_type='content/image')

    # same as post
    def create(self, request):
        """Create a new hello message."""

        # get data from request and pass it in serializer
        serializer = serializers.HelloSerializer(data=request.data)

        # if it is valid, print the string message
        if serializer.is_valid():

            myString = serializer.data.get('myString')
            print(myString)

            file1 = open("hindi.input.txt", "w")

            file1.write(myString)

            file1.close()

            dic = {}


            os.system("make hindi.output")

            file = open("hindi.output", "r")

            for i in file:
                i = i.strip("\n").split("\t")
                if (len(i) > 1):
                    if (i[3] in dic):
                        dic[i[3]].append(i[1])
                    else:
                        dic[i[3]] = [i[1]]

            print(dic)

            bulbNum = 0

            if ("QO" in dic.keys()):
                if (dic["QO"][0] == "एक" or dic["QO"][0] == "पहला" or dic["QO"][0] == "पहले"):
                    print("first bulb")
                    bulbNum = 1

            if ("QC" in dic.keys()):
                if (dic["QC"][0] == "एक" or dic["QC"][0] == "पहला" or dic["QC"][0] == "पहले"):
                    print("first bulb")
                    bulbNum = 1

            if ("NST" in dic.keys()):
                if (dic["NST"][0] == "पहले"):
                    print("first bulb 1")
                    bulbNum = 1

            if ("QO" in dic.keys()):
                if (dic["QO"][0] == "दो" or dic["QO"][0] == "दूसरा"):
                    print("seconnd bulb")
                    bulbNum = 2

            if ("QC" in dic.keys()):
                if (dic["QC"][0] == "दो" or dic["QC"][0] == "दूसरा"):
                    print("seconnd bulb")
                    bulbNum = 2

            if ("QO" in dic.keys()):
                if (dic["QO"][0] == "तीन" or dic["QO"][0] == "तीसरा"):
                    print("third bulb")
                    bulbNum = 3

            if ("QC" in dic.keys()):
                if (dic["QC"][0] == "तीन" or dic["QC"][0] == "तीसरा"):
                    print("third bulb")
                    bulbNum = 3

            if ("QO" in dic.keys()):
                if (dic["QO"][0] == "चार" or dic["QO"][0] == "चौथा"):
                    print("fourth bulb")
                    bulbNum = 4

            if ("QC" in dic.keys()):
                if (dic["QC"][0] == "चौथा" or dic["QC"][0] == "चार"):
                    print("fourth bulb")
                    bulbNum = 4

            to_do = -1

            if ("JJ" in dic.keys()):
                if (dic["JJ"][0] == "बंद"):
                    print("off")
                    to_do = 0

            if ("JJ" in dic.keys()):
                if (dic["JJ"][0] == "चालू"):
                    print("on")
                    to_do = 1

            if ("NN" in dic.keys()):
                if (dic["NN"][0] == "चालू"):
                    print("on")
                    to_do = 1
                if (len(dic["NN"]) > 1):
                    if (dic["NN"][1] == "चालू"):
                        print("off")
                        to_do = 1

            if ("NN" in dic.keys()):
                if (dic["NN"][0] == "बंद"):
                    print("off")
                    to_do = 0
                if(len(dic["NN"]) > 1):
                    if (dic["NN"][1] == "बंद"):
                        print("off")
                        to_do = 0


            if (to_do == 1):
                if (bulbNum == 1):
                    print("set1")
                    db.child("SR").set(1)
                elif (bulbNum == 2):
                    print("set2")
                    db.child("SR").set(2)
                elif (bulbNum == 3):
                    print("set3")
                    db.child("SR").set(3)
                elif (bulbNum == 4):
                    print("set4")
                    db.child("SR").set(4)

            if (to_do == 0):
                if (bulbNum == 1):
                    print("set5")
                    db.child("SR").set(5)
                elif (bulbNum == 2):
                    print("set6")
                    db.child("SR").set(6)
                elif (bulbNum == 3):
                    db.child("SR").set(7)
                elif (bulbNum == 4):
                    db.child("SR").set(8)

            # if(dic["QO"][0] == "एक" or dic["QO"][0] == "पहला" or dic["QO"][0] == "पहले" or  dic["NST"][0] == "पहले"):
            #     print("first bulb")
            #     bulbNum = 1
            #
            # if(myString == "पहला बल्ब बंद करें"):
            #     print("okay2")
            #     db.child("SR").set(1)
            # if (myString == "पहला बल्ब बंद करे"):
            #     db.child("SR").set(2)
            # if (myString == "three"):
            #     db.child("SR").set(3)
            # if (myString == "four"):
            #     db.child("SR").set(4)
            # if (myString == "zero"):
            #     db.child("SR").set(0)


            return Response({'message': myString})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)