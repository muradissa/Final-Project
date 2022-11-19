from rest_framework import serializers
from .models import Anchor
from .models import Wall

# code = models.IntegerField(null=False,default=0,unique=True)
#anchor_is_help = models.BooleanField(null=False , default=False)
#x = models.IntegerField(null=False,default=0)
#y = models.IntegerField(null=False,default=0)
class AnchorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ('id', 'code', 'anchor_is_help', 'x', 'y')

class CreateAnchorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields =('code','x','y')
        
class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ('height','width','angle','number_of_anchors')    
        

class CreateWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ('height','width','angle','number_of_anchors')       
        
   