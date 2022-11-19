from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,status
from .serializers import AnchorSerializer,CreateAnchorSerializer,CreateWallSerializer, ParametersSerializer,WallSerializer
from .models import Anchor ,Wall
from rest_framework.views import APIView
from rest_framework.response import Response
import json

anchors = []
wall = []
typeParameters =[]

# Create your views here.


def main(request):
    return HttpResponse("Hello")

class AnchorView(generics.ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializer

class WallView(generics.ListAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer
    
class CreatAnchorView(APIView):
    
    serializer_class = CreateAnchorSerializer
    def post(self,request,format=None):
        pass
    
class CreatWallView(APIView):
    
    serializer_class = CreateWallSerializer
    def post(self , request , format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
       
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            height = serializer.data['height']  
            width = serializer.data['width']
            angle = serializer.data['angle']
            number_of_anchors = serializer.data['number_of_anchors']
            host = self.request.session.session_key
            queryset = Wall.objects.filter(host =host)
            if queryset.exists():
                wall = queryset[0]
                wall.height = height
                wall.width = width
                wall.angle = angle
                wall.number_of_anchors = number_of_anchors
                wall.save(update_fields=['height','width','angle','number_of_anchors'])
            else:
                wall = Wall(host =host , height=height , width=width , angle=angle , number_of_anchors=number_of_anchors )
                wall.save()

            return Response(WallSerializer(wall).data, status=status.HTTP_201_CREATED)
        
        
        
class CreatAnchorsView(APIView):
    
    serializer_class = CreateAnchorSerializer
    def post(self , request , format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        anchors = json.loads(request.data)
        print(request.data)
        
        return Response("ok", status=status.HTTP_200_OK)


class EnterParametersView(APIView):
    
    serializer_class = ParametersSerializer
    def post(self , request , format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        typeParameters =json.loads(request.data)
        print(request.data)
        
        return Response("ok", status=status.HTTP_200_OK)
       
       
                
                
            
            
            