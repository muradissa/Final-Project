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
from .monteCarlo1d import *
from .euller_beam import *
# from .euller_beam2d import *
import base64
from .GradientDescent1d import *


anchors1 = []
manual_anchor = []
wall1 = []
typeParameters =[]
optimizationType = ''
dimensional_type = ''
strategy_type = ''
height1=0
angle1=90
width1=0
number_Of_Anchors1=0
quality1=0
high_moment = 0
anchors_1d =[]

anchorsInRow = 0 
anchorsInCol = 0
bloop_global = False


# Create your views here.

class AnchorView(generics.ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializer

class WallView(generics.ListAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer
    
class CreatWallView(APIView):  
    serializer_class = CreateWallSerializer


    def post(self , request , format=None):
        global width1, height1 , number_Of_Anchors1, angle1 ,anchorsInRow, anchorsInCol,bloop_global

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()   
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            
            height = serializer.data['height']  
            width = serializer.data['width']
            angle = serializer.data['angle']
            number_of_anchors = serializer.data['number_of_anchors']
            anchorsInRow = serializer.data['anchorsInRow']
            anchorsInCol = serializer.data['anchorsInCol']
            bloop = serializer.data['bloop']
            bloop_global = bloop
            
            width1 =width 
            height1 = height
            number_Of_Anchors1 = number_of_anchors
            angle1 = angle
            number_Of_Anchors1 = int(serializer.data['number_of_anchors'])
            print("Number of anchors creatwallview: " ,number_Of_Anchors1)
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
        global manual_anchor
        manual_anchor=[]
        
        for index in range(len(anchors)):
            manual_anchor.append({
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
        global strategy_type , optimization_type ,dimensional_type
        optimization_type = request.data['optimizationType']
        strategy_type = request.data['strategyType']
        dimensional_type = request.data['dimensionalType']
        return Response("ok", status=status.HTTP_200_OK)

class startSimulation(APIView):
    
    def post(self , request , format=None):
        
        global strategy_type , anchors1 ,anchorsInRow, anchorsInCol, manual_anchor, quality1
        anchors1 = []

###############################################################################################################################
########################################################## 2D #################################################################
###############################################################################################################################
        if(dimensional_type == '2'):
            #Manually
            if(strategy_type == '1'):
                result =anchors1
                quality1 = quality(height1 , width1 , anchors1)            
            #Equal Distance 
            if(strategy_type == '2'): # number_of_anchors 
                result = createEqualDistance(height1,width1, anchorsInRow, anchorsInCol)  
            #Monte carlo
            if(strategy_type == '3'):
                result = createAncorsWithMonteCarlo(height1,width1,number_Of_Anchors1)
            
            anchors1 = result

###############################################################################################################################
########################################################## 1D #################################################################
###############################################################################################################################
        if(dimensional_type == '1'):
            # input(f"number of anchors = {number_Of_Anchors1}")
            #Manually
            if(strategy_type == '1'):
                result = manual_anchor
            
            #Equal Distance 
            elif(strategy_type == '2'): # number_of_anchors 
                result  = createEqualDistance1d(height1,number_Of_Anchors1)
            
            #Monte carlo
            elif(strategy_type == '3'):
                result  = createAncorsWithMonteCarlo1d(height1, angle1, number_Of_Anchors1)

            print("result 1 = ",result)
            anchors2 =[]
            for anchor in result:
                anchors2.append(anchor['y'])

            if optimization_type == '1':
                anchors1 = result
            
            print("Number of anchors startSimulation : " ,number_Of_Anchors1)
            #optimization
            if(optimization_type == '2'):
                x_anchors = gradient_descent_1d(height1, anchors2, angle1, cost_func, True, 1)
                for index in range(len(x_anchors)):
                    anchors1.append({'id':index+1, 'x': 0, 'y':x_anchors[index]})
                result = anchors1
                print("result 2 = ",result)

        return Response(json.dumps(result), status=status.HTTP_200_OK)
    
class simulationQuality(APIView):
    def post(self , request , format=None):
        global quality1
        quality_str = str(quality1*100)
        quality_str = quality_str[0:4]
        return Response(quality_str, status=status.HTTP_200_OK)

class getHighMoment(APIView):
    def post(self , request , format=None):
        global high_moment ,anchors1     
        anchors2 =[]
        for acnhor in anchors1:
            anchors2.append(acnhor['y'])
        high_moment = start_euller_beam(h=height1, deg=angle1, anchors=anchors2, both=True) 
        return Response(high_moment, status=status.HTTP_200_OK)

class getImage(APIView):
    def post(self , request , format=None):
        with open('plot.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)

class getHighMoment2d(APIView):
    def post(self , request , format=None):
        global high_moment ,anchors1   ,height1 , width1 ,bloop_global
        anchors2 =[]
        print("get high moment , anchors : ", anchors1)
        for anchor in anchors1:
            abc=[anchor['x'],anchor['y']]
            anchors2.append(abc)
            
        high_moment = start_wall_test(width=width1, height=height1, bLoop=bloop_global, anchors=anchors2, print_all=True) # TODO add bloop to gui 
        return Response(high_moment, status=status.HTTP_200_OK)

class getImage1(APIView):
    def post(self , request , format=None):
        with open('W.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
        
class getImage2(APIView):
    def post(self , request , format=None):
        with open('Wxy.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    
class getImage3(APIView):
    def post(self , request , format=None):
        with open('Wxx.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    
class getImage4(APIView):
    def post(self , request , format=None):
        with open('Wyy.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    
class getImage5(APIView):
    def post(self , request , format=None):
        with open('Mxx.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    
class getImage6(APIView):
    def post(self , request , format=None):
        with open('Myy.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    
class getImage7(APIView):
    def post(self , request , format=None):
        with open('Mxy.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)
    

class getImageNumerical(APIView):
    def post(self , request , format=None):
        with open('numerical_plot.jpg', "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return Response(image_data, status=status.HTTP_200_OK)       
    
            