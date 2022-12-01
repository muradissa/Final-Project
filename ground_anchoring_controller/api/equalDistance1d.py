

def createEqualDistance1d(height,numberOfAnchors):
    
    anchors =[]
    y1 = 0
    if(numberOfAnchors ==0):
        return anchors
    if (height > numberOfAnchors):
        y2 = (height/(numberOfAnchors+1))
    elif (height <= numberOfAnchors):
        y2=1  
    y1 = round(y2)
    id = 1  
    while (height >= y1 and numberOfAnchors >= id):  
        anchors.append({'id' :id ,'x' :0 , 'y' :y1})          
        id+=1
        y1=round(y2 * id)
      
    return anchors 
