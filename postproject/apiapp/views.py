from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from apiapp.serialaizers import Nameseraializer

# Create your views here.
class testappiview(APIView):
    def get(self,request,format=None):
        return Response({'msg':'welcome in the vaibhav-nitin world '})
    def post(self,request):
        serializer=Nameseraializer(data==request.data)
        if serializer.is_valid():
            name=serializer.data.get("name")
            msg='Hello {} wish u very happy birth day !!'.format(name)
        return Response(serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'msg':'Response from put method'})
    def patch(self,request,pk=None):
        return Response({'msg':'Response from patch method'})
    def delete(self,request,pk=None):
        return Response({'msg':'Response from delete method'})