from numpy import * 
from copy import deepcopy
from .euller_beam import *


def quality1d(wall: clWall, anchors):
    
    anchors_x =[]
    for anchor in anchors:
        anchors_x.append(anchor['y'])

    return round(abs(wall.testBeam(anchors=anchors_x, drew_graph=False)), 2)

# Done !
def quality(wall: clWall, anchors):
     
    anchors_xy =[]
    for anchor in anchors:
        anchors_xy.append([anchor['x'], anchor['y']])
    aaa =round(abs(wall.testWall(v_xy_anchor=anchors_xy, print_all=False)), 2)
    print(aaa)
    return aaa