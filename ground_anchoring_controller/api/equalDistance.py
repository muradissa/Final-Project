

def createEqualDistance(height,width,numberOfAnchors):
    
    anchors =[]
    y1 = height-3
    x1 = 3
    id = 1
    while (y1 > 2 and numberOfAnchors >= id):  
        anchors.append({'id' :id ,'x' :x1 , 'y' :y1})
        if (x1 > width-5):
            x1 = 3
            y1-=5
        else:
            x1 +=5
        id+=1
        
    return anchors
        
     