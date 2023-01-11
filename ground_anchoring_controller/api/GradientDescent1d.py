# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from .euller_beam import *
# add h to global and import it

# def cost_func(h, v_x_anchor):
#     dx = 0.001
#     beam = clBeam(h , 90)
#     vvc = beam.vvc_get(v_x_anchor)
#     ix = 0
#     x = 0
#     m = 0
#     while x <= h:
#         iInterval=beam.iInterval_get(x,v_x_anchor)
#         vc = vvc[iInterval*4:iInterval*4 + 4]
#         w2=beam.ww2(x,vc)
#         if ix == 0 or abs(w2) > m :
#             m = abs(w2)
#         x += dx
#         ix += 1

#     return m*beam.E_Ic


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


def test_wall(n):
    vx = init_solution(10,n)
    f_min, vx_best = gradient_descent_1d(10, vx, cost_func, True, 1)
    print(f"f_min = {f_min}")
    print(f"vx_best = {vx_best}")
    return


def init_solution(h,n):
    dx = h/n
    vx = []

    for i in range(n):
        vx.append(dx*(i + 1))

    return vx

def gradient_descent_1d(h, vx, deg, f, b_min, dx):
    
    wall = clWall(yMax=h , angleFromVerticalGrad=deg) #need to add deg
    f0 = f(wall, vx)
    dx_min = 0.01
    n = len(vx)
    while dx > dx_min:
        print(dx)
        b = True
        while b:
            vdf = []
            y = 0

            for i in range(n):
                vxi = []

                for j in range(n):
                    vxi.append(vx[j])
                
                vxi[i] += dx
                dy = (f(wall, vxi) - f0) / dx
                y += dy**2
                vdf.append(dy)
            
            y = y**0.5
            vx_new = []
            sign = -1 if b_min else 1
            
            for i in range(n):
                vx_new.append(vx[i] + sign * dx * vdf[i] / y)
            
            f1 = f(wall, vx_new)
            if b_min:
                b = f1 < f0
            else:
                b = f1 > f0

            if b:
                f0 = f1
                vx = vx_new

        dx = dx / 2

    return vx
            

