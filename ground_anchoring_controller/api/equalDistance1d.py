

def createEqualDistance1d(height, numberOfAnchors):
    anchors =[]
    y1 = 0

    if(numberOfAnchors ==0):
        return anchors

    gap = (height/(numberOfAnchors+1))
    y1 = round(gap, 2)
    id = 1  

    while (height >= y1 and numberOfAnchors >= id):  
        anchors.append({'id' :id ,'x' :0 , 'y' :y1})          
        id+=1
        y1=round(gap * id, 2)

    return anchors 
