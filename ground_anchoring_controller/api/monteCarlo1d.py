'''
    #      =>  Monte Carlo simulation  <=
    # Our code run 1000 simulations and save the best one that give us a high quality
    # to imporve the solution we can increase number the simultion but it's not necessary to give us better quality 
'''
# Importing Packages
from numpy import * 
from .wallPressure1d import *
import random
from .GradientDescent1d import cost_func

# Creating Roll Anchor Function
def roll_dice (height ,anchors_1 ):    
    x = 0
    # y = random.randint(1, height-1)
    y= round(random.uniform(0.1, height), 2)

    # Determining if the anchor is exist
    if(len(anchors_1) > 0):
        for anchor in anchors_1:
            if(anchor['x'] == 0 and anchor['y'] == y):
                return False ,0,0
    return True ,x ,y


def createAncorsWithMonteCarlo1d(height, deg, max_num_of_anchors):
    # Inputs & Tracking
    wall = clWall(yMax=height , angleFromVerticalGrad=0) # TODO need to add deg

    num_simulations = 1000
    anchors = []
    min_moment = 0
    # For loop to run for the number of simulations desired
    for i in range(num_simulations):
        anchors_1 = []
        num_anchor = 0

        # Run until the computer has rolled "max_num_of_anchors" times
        while len(anchors_1) < max_num_of_anchors:

            new_anchor,x,y = roll_dice(height ,anchors_1)         
            # Result if the anchors is not exist 
            if new_anchor:
                anchors_1.append({'id' : num_anchor+1 , 'x' : x , 'y' : y})
                num_anchor += 1

        # if this simulation give us better quality than take it
        moment = quality1d(wall, anchors_1 )

        if moment < min_moment or not len(anchors):
            print(moment, " new  old ", min_moment)
            min_moment = moment 
            anchors = anchors_1.copy()

    return anchors 