
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


def createEqualDistance(height, width, number_of_points_row, number_of_points_col):
    anchors =[]
    id = 0

    if(number_of_points_row == 0 or number_of_points_col == 0):
        return anchors

    x_distance = width / (number_of_points_row + 1) 
    y_distance = height / (number_of_points_col + 1)
    
    for i in range(number_of_points_row):
        for j in range(number_of_points_col):
            anchors.append({'id' :id ,'x' : (i + 1)* x_distance , 'y' : (j + 1) * y_distance})          
            id +=1

    return anchors


