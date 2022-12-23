from __future__ import division  #to enable normal floating division
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class clBeam():
	def __init__(self, h, deg):
		# Beam parameters
		# Exact solution, E*Iy = const, y1 = y', y0 = y, 
		#w = 10  #beam cross sec width (m) - not in use
		self.h = h   # height (m)
		self.deg = deg   # height (m)
		self.I = 104   #cross sec moment of inertia (mm^4)
		self.E = 30   #steel elast modul (N/mm^2)
		self.F = 9.8*1000*math.sin(math.radians(deg))  #point load (N)
		self.E_Ic = (self.I * self.E)*(1000**2)
#  kg*m^2/s^2

	def get_E_Ic(self):
		return self.E_Ic

	def w(self, x, c_1, c_2, c_3, c_4):
		return -(self.F*x**5)/(2*3*4*5*self.E_Ic) + (self.F*self.h*x**4)/(2*3*4*self.E_Ic) + c_1*x**3 + c_2*x**2 + c_3*x + c_4

	def bb(self,x):
		return -(self.F*(x**5))/(2*3*4*5*self.E_Ic) + (self.F*self.h*(x**4))/(2*3*4*self.E_Ic)

	def bb1(self,x):
		return -(self.F*(x**4))/(2*3*4*self.E_Ic) + (self.F*self.h*(x**3))/(2*3*self.E_Ic)

	def bb2(self,x):
		return -(self.F*(x**3))/(2*3*self.E_Ic) + (self.F*self.h*(x**2))/(2*self.E_Ic)

	def bb3(self,x):
		return -(self.F*(x**2))/(2*self.E_Ic) + (self.F*self.h*x)/(self.E_Ic)

	def aa(self,x,k):
		if k in [0, 1, 2 , 3]:
			return x**k
		raise ValueError

		# if k==0:
		# 	return 1
		# if k==1:
		# 	return x
		# if k==2:
		# 	return x**2
		# if k==3:
		# 	return x**3

	def aa1(self,x,k):
		if k == 0:
			return 0
		if k in [1, 2 , 3]:
			return k*x**(k - 1)
		raise ValueError

		# if k==0:
		# 	return 0
		# if k==1:
		# 	return 1
		# if k==2:
		# 	return 2*x
		# if k==3:
		# 	return 3*(x**2)
		# return 1/0

	def aa2(self,x,k):
		if k in [0, 1]:
			return 0
		if k in [2 , 3]:
			return (k-1)*k*x**(k - 2)
		raise ValueError
		# if k==0:
		# 	return 0
		# if k==1:
		# 	return 0
		# if k==2:
		# 	return 2
		# if k==3:
		# 	return 6*x
		# return 1/0
	def aa3(self,x,k):
		if k in [0, 1, 2]:
			return 0
		if k ==3:
			return 6
		raise ValueError
		
		# if k==0:
		# 	return 0
		# if k==1:
		# 	return 0
		# if k==2:
		# 	return 0
		# if k==3:
		# 	return 6
		# return 1/0

	def ww(self,x,vc):
		w=self.bb(x)
		for k in range(4):
			w+=vc[k]*self.aa(x,k)
		return w

	def ww2(self,x,vc):
		w=self.bb2(x)
		for k in range(4):
			w+=vc[k]*self.aa2(x,k)
		return w
	# A * x = b
	# size of x is 4 * (כמות אנכורים +1)
	# size of b is 4 * (כמות אנכורים +1)
	# size of A is (4 * (כמות אנכורים +1))^2
	# list pf the anchor places - v_x_anchor
	
	def vvc_get(self,v_x_anchor):
		#v_x_anchor - ordered by increasing, 0.1<x_anchor<=h
		n = len(v_x_anchor)
		self.nn_make(v_x_anchor)
		v_b=[]
		v_b = [0, 0, 0, 0] * (self.nn + 1) # list size of nn+1
		vv_A = [[0 for col in range(4*(self.nn + 1))] for row in range(4*(self.nn + 1))]

		for i_anchor in range(self.nn + 1):
			u=4*i_anchor
			if i_anchor == 0:
				# w(0) = 0
				k0=0
				for k in range(4):
					vv_A[u][k0+k] = self.aa(0,k)
				v_b[u] = -self.bb(0)
			else:
				# w(ai+) = 0
				x = v_x_anchor[i_anchor-1]
				k0=4*i_anchor
				for k in range(4):
					vv_A[u][k0+k] = self.aa(x,k)
				v_b[u] = -self.bb(x)
			
			u=4*i_anchor+1
			if i_anchor == 0:
				# w'(0) = 0
				k0=0
				for k in range(4):
					vv_A[u][k0+k] = self.aa1(0,k)
				v_b[u] = -self.bb1(0)
			else:
				# w'(ai-) = w'(ai+)
				# -(F*x**4)/(2*3*4*E_Ic) + (F*h*x**3)/(2*3*E_Ic) + c_11*3*x**2 + c_12*x*2 + c_13 = 
				# -(F*x**4)/(2*3*4*E_Ic) + (F*h*x**3)/(2*3*E_Ic) + c_21*3*x**2 + c_22*x*2 + c_23
				x = v_x_anchor[i_anchor-1]
				k0=4*i_anchor
				for k in range(4):
					vv_A[u][k0+k-4] = self.aa1(x,k)
					vv_A[u][k0+k] = -self.aa1(x,k)
				v_b[u] = 0
			
			u=4*i_anchor+2
			if i_anchor == n:
				# w''(h) = 0
				# -(F*h**3)/(2*3*E*I) + (h**3)/(2*E*I) + c_1*6*h + c_2*2
				x=self.h
				k0=4*n
				for k in range(4):
					vv_A[u][k0+k] = self.aa2(x,k)
				v_b[u] = -self.bb2(x)
			else:
				# w(ai-) = 0
				# -(F*x**5)/(2*3*4*5*E_Ic) + (h*x**4)/(2*3*4*E_Ic) + c_1*x**3 + c_2*x**2 + c_3*x + c_4 = 0 
				x = v_x_anchor[i_anchor]
				k0=4*i_anchor
				for k in range(4):
					vv_A[u][k0+k] = self.aa(x,k)
				v_b[u] = -self.bb(x)
				
			u=4*i_anchor+3
			if i_anchor == n:
				# w'''(h)=0
				# -(F*h**2)/(2*E*I) + (h**2)/(E*I) + c_1*6 = 0
				x=self.h
				k0=4*n
				for k in range(4):
					vv_A[u][k0+k] = self.aa3(x,k)
				v_b[u] = -self.bb3(x)
			else:
				x = v_x_anchor[i_anchor]
				k0=4*i_anchor
				if self.bTheLastAnchor_h and i_anchor==self.nn:
					#w''(ai-)=0
					for k in range(4):
						vv_A[u][k0+k] = self.aa2(x,k)
					v_b[u] = -self.bb2(x)
				else:
					# vv_A[4*( i_anchor - 1 ) + 1] = vv_A[4*( i_anchor ) + 1]
					# w''(ai+)=w''(ai-)
					# -(F*x**3)/(2*3*E_Ic) + (F*h*x**2)/(2*E_Ic) + c_11*6*x + c_12*2 = 
					# -(F*x**3)/(2*3*E_Ic) + (F*h*x**2)/(2*E_Ic) + c_21*6*x + c_22*2
					for k in range(4):
						vv_A[u][k0+k] = self.aa2(x,k)
						vv_A[u][k0+k+4] = -self.aa2(x,k)
					v_b[u] = 0
		

		vc = np.linalg.solve(vv_A, v_b)
		return vc

	def nn_make(self,v_x_anchor):
		self.bTheLastAnchor_h=False
		n = len(v_x_anchor)
		self.nn=n
		if n>0:
			self.bTheLastAnchor_h=(abs(self.h-v_x_anchor[n-1])<0.01)
		if self.bTheLastAnchor_h:
			self.nn-=1#no need the last interval

	def iInterval_get(self,x,v_x_anchor):
		#use after self.nn_make(v_x_anchor)
		i_anchor=0
		for x_anchor in v_x_anchor:
			if x<=x_anchor:
				return i_anchor
			i_anchor+=1
		if self.bTheLastAnchor_h:
			return i_anchor-1
		return i_anchor

	def xy_get(self,v_x_anchor,nPoints=300):
		vvc = self.vvc_get(v_x_anchor)
		x_data = np.linspace(0,self.h,nPoints)
		vy = []
		vy2 = []
		for x in x_data.tolist():
			iInterval=self.iInterval_get(x,v_x_anchor)
			vc = vvc[iInterval*4:iInterval*4 + 4]
			w=self.ww(x,vc)
			vy.append(w)
			w2=self.ww2(x,vc)
			vy2.append(w2)
		y_data = np.array(vy)
		y2_data = np.array(vy2)
		return x_data,y_data,y2_data

# w(0) = 0
# w'(0) = 0
# w''(h) = 0
# w'''(h)=0
# w(ai-) = w(ai+) ai = anchor i
# w'(ai-) = w'(ai+) 
# w''(ai+)=w''(ai-)
# w(ai-) = 0
# w(ai+) = 0
# w(ai) = 0



# h=10
# Beam=clBeam(h)
# anchors = [2,4,6,8,10]
# x_data,y_data,y2_data=Beam.xy_get(anchors)
# plt.plot(x_data,y_data, label = "w")
# plt.plot(x_data,y2_data, label = "w''")
# plt.plot([0,h],[0,0], label = "x")
# plt.legend()
# plt.show()


def start_euller_beam(h, deg, anchors, save_plot=True):
    anchors.sort()
    Beam=clBeam(h, deg)
    x_data,y_data,y2_data=Beam.xy_get(anchors)
    max1 = find_the_high_moment(y2_data, Beam.get_E_Ic())
    
    if save_plot:
        plt.close()
        plt.plot(y_data,x_data, label = "w")
        plt.plot(y2_data,x_data, label = "w''")
        plt.plot([0,0],[0,h], label = "x")
        plt.legend()
        
        #plt.show()
        plt.savefig("plot.jpg")

    return max1
    
def find_the_high_moment(y2_data, E_Ic):
    max1 = y2_data[0]

    for w2_x in y2_data:
        if abs(w2_x) > max1:
            max1 = abs(w2_x)

    return round(abs(-E_Ic*max1), 2)
    


# start_euller_beam(h=15 ,anchors = [2,4,6,9,14] )