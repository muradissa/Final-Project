'''
    #      =>  Monte Carlo simulation  <=
    # Our code run 1000 simulations and save the best one that give us a high quality
    # to imporve the solution we can increase number the simultion but it's not necessary to give us better quality 
'''
# Importing Packages
from numpy import * 
from .wallPresure import *
import random

# Creating Roll Anchor Function
def roll_dice (height , width,anchors_1 ):
    #print( height , width)
    
    x = random.randint(1, width-1)
    y = random.randint(1, height-1)

    # Determining if the anchor is exist
    if(len(anchors_1) > 0):
        for anchor in anchors_1:
            if(anchor['x'] == x and anchor['y'] == y):
                return False ,0,0
    return True ,x ,y


def createAncorsWithMonteCarlo(height , width,max_num_of_anchors):
    # Inputs & Tracking
    num_simulations = 1000
    anchors = []
    quality_1 = 0
    # For loop to run for the number of simulations desired
    for i in range(num_simulations):
        anchors_1 = []
        num_rolls = [0]
        num_anchor = 0
        # Run until the computer has rolled "max_num_of_anchors" times
        while num_rolls[-1] < max_num_of_anchors:
            
            new_anchor,x,y = roll_dice(height , width,anchors_1) 
            
            # Result if the anchors is not exist 
            if new_anchor:
                anchors_1.append({'id' : num_anchor+1 , 'x' : x , 'y' : y})
                num_anchor += 1
                    
            num_rolls.append(num_rolls[-1] + 1)

        # if this simulation give us better quality than take it
        quality_2 = quality(height , width,anchors_1)
        if (quality_2 > quality_1):
            quality_1 = quality_2 
            anchors = anchors_1.copy()
            
    return anchors , quality_1