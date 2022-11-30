from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,status
from .serializers import AnchorSerializer,CreateAnchorSerializer,CreateWallSerializer, ParametersSerializer,WallSerializer
from .models import Anchor ,Wall
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .equalDistance import *
from .monteCarlo import *


anchors1 = []
wall1 = []
typeParameters =[]
optimizationType = ''
dimensionalType = ''
strategyType = ''
heigth1=0
width1=0
numberOfAnchors1=0

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
            global width1, heigth1 , numberOfAnchors1
            width1 =width 
            heigth1 = height
            numberOfAnchors1 = number_of_anchors
            
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
        anchors = json.loads(request.data['anchors'])
        global anchors1
        anchors1=[]
        
        for index in range(len(anchors)):
            anchors1.append({
                'id':anchors[str(1+index)]['code'],
                'x': anchors[str(1+index)]['x'],
                'y':anchors[str(1+index)]['y']})
            
        return Response("ok", status=status.HTTP_200_OK)


class EnterParametersView(APIView):   
    serializer_class = ParametersSerializer
    def post(self , request , format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        #typeParameters =json.loads(request.data)
        global strategyType , globaloptimizationType ,dimensionalType
        globaloptimizationType = request.data['optimizationType']
        strategyType = request.data['strategyType']
        dimensionalType = request.data['dimensionalType']
        return Response("ok", status=status.HTTP_200_OK)
    

class startSimulation(APIView):
    
    def post(self , request , format=None):
        
        global strategyType
        
        #Manually
        if(strategyType == '1'):
            result =anchors1
        
        #Equal Distance 
        if(strategyType == '2'): # number_of_anchors 
            result = createEqualDistance(heigth1,width1,numberOfAnchors1)
            print(result)
            
        
        #Monte carlo
        if(strategyType == '3'):
            result ,quality = createAncorsWithMonteCarlo(heigth1,width1,numberOfAnchors1)
            print(result ,quality)
        
        #optimization
        if(True):
            pass
        
        return Response(json.dumps(result), status=status.HTTP_200_OK)
    
        
    
            