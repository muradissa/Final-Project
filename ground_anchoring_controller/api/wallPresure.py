from numpy import * 
from copy import deepcopy


# presure formula=> P = phg
p= 997   # water mass density = 997 kg/m³
# h = height # height m
g = 9.8 # 9.8 m/sec^2 


# Done !
'''
# inputs  => height :number , width:number 
# output  => wall presure without anchors "floatMatrix"
# p1 matrix
'''
def create_mat_wall_presure(height , width ):
    wall_presure = []
    for w in range(1, width+1):
        row_presure = []
        for h in range(1,height+1):
            presure = p*g*h
            row_presure.append(presure)
        wall_presure.append(row_presure)
    return wall_presure
 
   
# Done !
'''
  inputs  => (height : number) , (width : number) , (wall_presure : floatMatrix) , (anchors : array of {id:number , x:number , y:number})
  output  => wall presure with the anchors "floatMatrix"
'''
def calculate_mat_wall_presure(height , width , wall_presure , anchors):
    
    wall_presure2 = wall_presure.copy()
    for anchor in anchors:
        x = anchor['x']
        y = anchor['y']
        
        if(x != 0):  
            x-=1
        
        # distance = 0
        wall_presure2[x][y] = 0
        
        # distance = 1
        if(0 < x-1 and y+1 < height ):
            wall_presure2[x-1][y+1] = wall_presure2[x-1][y+1] * 0.25 # 1
        if(y+1 < height):
            wall_presure2[x+0][y+1] = wall_presure2[x+0][y+1] * 0.25 # 2
        if(y+1 < height and x+1 < width):
            wall_presure2[x+1][y+1] = wall_presure2[x+1][y+1] * 0.25 # 3
        if(x+1 < width):
            wall_presure2[x+1][y+0] = wall_presure2[x+1][y+0] * 0.25 # 4
        if(x+1 < width and 0 < y-1):
            wall_presure2[x+1][y-1] = wall_presure2[x+1][y-1] * 0.25 # 5
        if(0 < y-1):
            wall_presure2[x+0][y-1] = wall_presure2[x+0][y-1] * 0.25 # 6
        if(0 < y-1 and 0 < x-1):
            wall_presure2[x-1][y-1] = wall_presure2[x-1][y-1] * 0.25 # 7
        if(0 < x-1):
            wall_presure2[x-1][y+0] = wall_presure2[x-1][y+0] * 0.25 # 8
        
        # distance = 2
        if(0 < x-2 and y+2 < height):
            wall_presure2[x-2][y+2] = wall_presure2[x-2][y+2] * 0.5 # 1
        if(0 < x-1 and y+2 < height):
            wall_presure2[x-1][y+2] = wall_presure2[x-1][y+2] * 0.5 # 2
        if(y+2 < height):
            wall_presure2[x+0][y+2] = wall_presure2[x+0][y+2] * 0.5 # 3
        if(x+1 < width and y+2 < height):
            wall_presure2[x+1][y+2] = wall_presure2[x+1][y+2] * 0.5 # 4
        if(x+2 < width and y+2 < height):
            wall_presure2[x+2][y+2] = wall_presure2[x+2][y+2] * 0.5 # 5
        if(x+2 < width and y+1 < height):
            wall_presure2[x+2][y+1] = wall_presure2[x+2][y+1] * 0.5 # 6
        if(x+2 < width):
            wall_presure2[x+2][y+0] = wall_presure2[x+2][y+0] * 0.5 # 7
        if(x+2 < width and 0 < y-1):
            wall_presure2[x+2][y-1] = wall_presure2[x+2][y-1] * 0.5 # 8
        if(x+2 < width and 0 < y-2):
            wall_presure2[x+2][y-2] = wall_presure2[x+2][y-2] * 0.5 # 9
        if(x+1 < width and 0 < y-2):
            wall_presure2[x+1][y-2] = wall_presure2[x+1][y-2] * 0.5 # 10
        if( 0< y-2):
            wall_presure2[x+0][y-2] = wall_presure2[x+0][y-2] * 0.5 # 11
        if(0< x-1 and 0 < y-2):
            wall_presure2[x-1][y-2] = wall_presure2[x-1][y-2] * 0.5 # 12
        if(0< x-2 and 0 < y-2):
            wall_presure2[x-2][y-2] = wall_presure2[x-2][y-2] * 0.5 # 13
        if(0< x-2 and 0 < y-1):
            wall_presure2[x-2][y-1] = wall_presure2[x-2][y-1] * 0.5 # 14
        if(0< x-2 ):
            wall_presure2[x-2][y+0] = wall_presure2[x-2][y+0] * 0.5 # 15
        if(0< x-2 and y+1 < height):
            wall_presure2[x-2][y+1] = wall_presure2[x-2][y+1] * 0.5 # 16
        
        # distance = 3
        if(0 < x-3 and y+3 < height):
            wall_presure2[x-3][y+3] = wall_presure2[x-3][y+3] * 0.75 # 1
        if(0 < x-2 and y+3 < height):
            wall_presure2[x-2][y+3] = wall_presure2[x-2][y+3] * 0.75 # 2
        if(0 < x-1 and y+3 < height):
            wall_presure2[x-1][y+3] = wall_presure2[x-1][y+3] * 0.75 # 3
        if(y+3 < height):
            wall_presure2[x+0][y+3] = wall_presure2[x+0][y+3] * 0.75 # 4
        if(x+1 < width and y+3 < height):
            wall_presure2[x+1][y+3] = wall_presure2[x+1][y+3] * 0.75 # 5
        if(x+2 < width and y+3 < height):
            wall_presure2[x+2][y+3] = wall_presure2[x+2][y+3] * 0.75 # 6
        if(x+3 < width and y+3 < height):
            wall_presure2[x+3][y+3] = wall_presure2[x+3][y+3] * 0.75 # 7
        if(x+3 < width and y+2 < height):
            wall_presure2[x+3][y+2] = wall_presure2[x+3][y+2] * 0.75 # 8
        if(x+3 < width and y+1 < height):
            wall_presure2[x+3][y+1] = wall_presure2[x+3][y+1] * 0.75 # 9
        if(x+3 < width):
            wall_presure2[x+3][y+0] = wall_presure2[x+3][y+0] * 0.75 # 10
        if(x+3 < width and  0 < y-1):
            wall_presure2[x+3][y-1] = wall_presure2[x+3][y-1] * 0.75 # 11
        if(x+3 < width and 0 < y-2):
            wall_presure2[x+3][y-2] = wall_presure2[x+3][y-2] * 0.75 # 12
        if(x+3 < width and 0 < y-3):
            wall_presure2[x+3][y-3] = wall_presure2[x+3][y-3] * 0.75 # 13     
        if(x+2 < width and 0 < y-3):
            wall_presure2[x+2][y-3] = wall_presure2[x+2][y-3] * 0.75 # 14
        if(x+1 < width and 0 < y-3):
            wall_presure2[x+1][y-3] = wall_presure2[x+1][y-3] * 0.75 # 15
        if( 0 < y-3):
            wall_presure2[x+0][y-3] = wall_presure2[x+0][y-3] * 0.75 # 16
        if( 0 < x-1 and 0 < y-3):
            wall_presure2[x-1][y-3] = wall_presure2[x-1][y-3] * 0.75 # 17
        if(0 < x-2 and 0 < y-3):
            wall_presure2[x-2][y-3] = wall_presure2[x-2][y-3] * 0.75 # 18
        if(0 < x-3 and 0 < y-3):
            wall_presure2[x-3][y-3] = wall_presure2[x-3][y-3] * 0.75 # 19   
        if(0 < x-3 and 0 < y-2):
            wall_presure2[x-3][y-2] = wall_presure2[x-3][y-2] * 0.75 # 20
        if(0 < x-3 and 0 < y-1):
            wall_presure2[x-3][y-1] = wall_presure2[x-3][y-1] * 0.75 # 21
        if(0 < x-3 ):
            wall_presure2[x-3][y+0] = wall_presure2[x-3][y+0] * 0.75 # 22
        if(0 < x-3 and y+1 < height):
            wall_presure2[x-3][y+1] = wall_presure2[x-3][y+1] * 0.75 # 23
        if(0 < x-3 and y+2 < height):
            wall_presure2[x-3][y+2] = wall_presure2[x-3][y+2] * 0.75 # 24  
    
    return wall_presure2


# Done !
'''
    this function should to put the anchors in good place 
    the distance between the anchors should be (x2-x1 = 7 , y2-y1 =7)
    inputs  => (height : number) , (width : number)
    output  => wall presure with the anchors "floatMatrix"
    p2 matrix
'''
def create_best_anchors_for_wall_presure(height , width):
    anchors =[]
    y1 = height-3
    x1 = 3
    id = 1
    while (y1 > 4 ):  
        anchors.append({'id' :id ,'x' :x1 , 'y' :y1})
        if (x1 > width-4):
            x1 = 3
            y1 -= 4
        else:
            x1 +=4
        id+=1
        
    return anchors
    

# Done !
def covert_matrix_presure_to_number(wall_presure):
    res1 = sum(wall_presure)
    #print(res1)
    return sum(wall_presure)
 
    
# Done !
'''
    This function take ( p1 =the maxinum presure ,p2 = the minumum presure ,p3 = the current presure) 
    and calculate the quality between them in this way =>
    quality = (p1-p3)/(p1-p2)
    Inputs  => (p1 : number) , (p2 : number) , (p3 : number)
    Output  => (quality : number)
'''
def calculate_quality(p1 , p2 , p3):
    #print("p1 :" ,p1)
    #print("p2 :" ,p2)
    #print("p3 :" ,p3)
    quality = 1- ((p3-p2)/(p1-p2))
    return quality
    

# Done !
def quality (height,width,anchors):
    # 1
    #print("1111")
    p1 = create_mat_wall_presure(height,width)   
    p1_sum = covert_matrix_presure_to_number(p1)
    p1_copy2 =[]
    p1_copy3=[]
    
    # 2
    #print("2222")
    best_places_for_anchors = create_best_anchors_for_wall_presure(height , width)
    p2 = calculate_mat_wall_presure(height , width, deepcopy(p1) ,best_places_for_anchors)
    p2_sum = covert_matrix_presure_to_number(p2)
    # 3
    #print("3333")
    p3 = calculate_mat_wall_presure(height , width, p1 ,anchors)
    p3_sum = covert_matrix_presure_to_number(p3)
    
    return calculate_quality(p1_sum ,p2_sum ,p3_sum)
    