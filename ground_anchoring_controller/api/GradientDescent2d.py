# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from euller_beam import *
#import .euller_beam
def cost_func(wall: clWall, v_x_anchor):
    dx = 0.001
    beam = wall.clBeamAnalytical(wall)
    vvc = beam.vvc_get(v_x_anchor)

    ix = 0
    x = 0
    m = 0
    while x <= beam.Wall.h:

        iInterval=beam.iInterval_get(x,v_x_anchor)
        vc = vvc[iInterval*4:iInterval*4 + 4]
        
        moment=beam.w2_get(x=x, vvc=vvc, v_x_anchor=v_x_anchor)

        if ix == 0 or abs(moment) > m :
            m = abs(moment)
        x += dx
        ix += 1

    return m


def test_wall():
    vx = [[3,2],[3,5],[3,7]]
    f_min, vx_best = gradient_descent_2d(10, 10, vx, cost_func, True, 1)
    print(f"f_min = {f_min}")
    print(f"vx_best = {vx_best}")
    return


def init_solution(h,n):
    dx = h/n
    vx = []

    for i in range(n):
        vx.append(dx*(i + 1))

    return vx

def gradient_descent_2d(height,width, anchors, f, b_min, dx):
    
    #wall = clWall(yMax=h , angleFromVerticalGrad=deg) #need to add deg
    wall=clWall(xMax=width, yMax=height)
    f0 = round(abs(wall.testWall(v_xy_anchor=anchors, bLoop=False, print_all=True)),2)
    dx_min = 0.01
    n = len(anchors)
    while dx > dx_min:
        print(dx)
        b = True
        while b:
            vdf = []
            y = 0

            for i in range(n):
                vxi = []

                for j in range(n):
                    vxi.append(anchors[j])
                
                vxi[i][0] += dx
                vxi[i][1] += dx
                dy = (round(abs(wall.testWall(v_xy_anchor=vxi, bLoop=False, print_all=False)),2) - f0) / dx
                y += dy**2
                vdf.append(dy)
            
            y = y**0.5
            vx_new = []
            sign = -1 if b_min else 1
            
            for i in range(n):
                vx_new.append(anchors[i] + sign * dx * vdf[i] / y)
            print("before cost")
            f1 = f(wall, vx_new) 
            print("after cost")
            if b_min:
                b = f1 < f0
            else:
                b = f1 > f0

            if b:
                f0 = f1
                anchors = vx_new
           
        dx = dx / 2

    return anchors
            
test_wall()
