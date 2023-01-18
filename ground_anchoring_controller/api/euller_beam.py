
from __future__ import division  #to enable normal floating division
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib import cm

class clWall():
	def __init__(self,xMax=10,yMax=10,angleFromVerticalGrad=0):
		# Beam parameters
		# Exact solution, E*Iy = const, y1 = y', y0 = y, 
		self.xMax=xMax
		self.yMax=yMax
		self.angleFromVerticalGrad=angleFromVerticalGrad
		# height (m)
		self.g = 9.8#m/sec^2  gravitation
		self.rho = 1000#kg/m^3  density of water
		
		wallWidth=0.2#m
		# w'''' = q(x)/(EI)
		#https://www.engineeringtoolbox.com/area-moment-inertia-d_1328.html
		#I_x = integral y^2 dA
		#I_y = integral x^2 dA
		#for 1 m * wallWidth: 
		#
		#wallWidth=0.1 m
		#(3): I_x=1 0.1^3/12=8*10^(-5) m^4
		#(3b): I_y=1^3 0.1/12=8*10^(-3) m^4
		#
		#wallWidth=0.5 m
		#(3): I_x=1 0.5^3/12=10^(-2) m^4
		#
		#wallWidth=1 m
		#(3): I_x=1 1^3/12=0.08 m^4
		#
		#https://www.linkedin.com/pulse/elastic-modulus-concrete-manilal-vasavan#:~:text=The%20elastic%20modulus%20of%20hardened,between%2030%20to%2050%20GPa.
		#E=20*10^9 (Pa=N/m^2)
		E=20*10**9
		#
		#for constant q without anchors: 
		#y_max=q*L^4/(8 E I_x)=q*L^4/(8 E b^3 /12)
		#=> b^3=q*L^4 *12/(8 E y_max), q=9.8*10^3=10^4, L=10 m, E=20^10^9, y_max =1 m
		#=> b^3=10^8 *12/(8 20 10^9)=12/1600=0.0075
		#=> wallWidth=b=0.0075^(1/3)=0.2 m
		beamWidth=1 #m for consistence between wall and beam: Force per 1 m of beam length = Force per 1 m^2 of wall square
		I=beamWidth*float(wallWidth**3)/12#m^4, =8^10^(-5) for wallWidth=0.1, =6.4^10^(-4) for wallWidth=0.2
		#
		#was:
		#I = 104   #cross sec moment of inertia (mm^4)
		#E = 30   #steel elast modul (N/mm^2)
		#self.E_Ic = (I * E*(1000**2) =30*10^9
		#
		#self.E_Ic = 8*20*(10**(9-5))#=16*10^5  => noAnchors yMax=17.5 m, with one anchor yMax=0.8 m
		self.E_Ic=E*I
		
		# w_xxxx(iv)+2w_xxyy(iv)+w_yyyy(iv)=q(x,y)/D
		# D=(2h^3 E)/(3(1-v^2)) where h is the width of the wall and v is the Poisson's Ratio defined by wall structure and material.
		#For design of concrete structures, the most common value of concrete Poisson’s ratio is taken as 0.2. (see https://theconstructor.org/concrete/properties/poissons-ratio-concrete/36030/#:~:text=The%20concrete%20Poisson's%20ratio%20under,ratio%20is%20taken%20as%200.2.)
		#I=1m wallWidth^3 /12, D=(2 wallWidth^3 E)/(3(1-v^2))
		#D=IE => 1/12 = 2/(3(1-v^2)) => (1-v^2)=8 ?!
		self.v=0.2#(1-v^2)=0.94 => ~8 times difference with beam model
		self.dd=float(2)*(wallWidth**3)*E/(3*(1-self.v**2))
		self.dd*=0.1
		
		self.start()
		#q(x,y)=rho*g*(h-h(y))
	def start(self):
		self.angleFromVerticalRad=float(self.angleFromVerticalGrad)*2*math.pi/360
		self.cos=math.cos(self.angleFromVerticalRad)
		self.h=self.h_y_get(self.yMax)
	def h_y_get(self,y):
		return y*self.cos
	def MomentBeam_get(self,w2):
		#M(x)=-EI w’’(x) #
		return -self.E_Ic*w2
	def q_get(self,y,index=0):
		# w'''' = (pg(h-y))/(EI)
		h_y=self.h_y_get(y)
		F=self.rho*self.g #rho*g=kg/m^3 * m/sec^2=N/m^3
		if index==0:
			return F*(self.h-h_y) #pressure N/m^3 * m = N/m^2 = Pa
		if index==1:#independent on y
			return F*self.h
		if index==2:#linear on y
			return -F*h_y

		# Old
	class clBeamAnalytical():
		#x is coordinate on beam (not on the wall)
		#w'''' = q(x)/(EI)
		#q(x,y)=rho*g*(h-h(y))
		#for beam:
		#x instead of y
		#q(x)=rho*g*(h-h(x))=rho*g*(h-x*cos(A))
		def __init__(self,Wall):
			self.Wall=Wall
			self.xMax=self.Wall.yMax
		def w(self, x, c_1, c_2, c_3, c_4):#not in use
			return self.bb(x) + c_1*x**3 + c_2*x**2 + c_3*x + c_4
		def bb(self,x):
			return (self.Wall.q_get(x,2)*(x**4))/(2*3*4*5*self.Wall.E_Ic) + (self.Wall.q_get(x,1)*(x**4))/(2*3*4*self.Wall.E_Ic)
		def bb1(self,x):
			return (self.Wall.q_get(x,2)*(x**3))/(2*3*4*self.Wall.E_Ic) + (self.Wall.q_get(x,1)*(x**3))/(2*3*self.Wall.E_Ic)
		def bb2(self,x):
			return (self.Wall.q_get(x,2)*(x**2))/(2*3*self.Wall.E_Ic) + (self.Wall.q_get(x,1)*(x**2))/(2*self.Wall.E_Ic)
		def bb3(self,x):
			return self.Wall.q_get(x,2)*(x**1)/(2*self.Wall.E_Ic) + (self.Wall.q_get(x,1)*x)/(self.Wall.E_Ic)
		def aa(self,x,k):
			if k==0:
				return 1
			if k==1:
				return x
			if k==2:
				return x**2
			if k==3:
				return x**3
			return 1/0
		def aa1(self,x,k):
			if k==0:
				return 0
			if k==1:
				return 1
			if k==2:
				return 2*x
			if k==3:
				return 3*(x**2)
			return 1/0
		def aa2(self,x,k):
			if k==0:
				return 0
			if k==1:
				return 0
			if k==2:
				return 2
			if k==3:
				return 6*x
			return 1/0
		def aa3(self,x,k):
			if k==0:
				return 0
			if k==1:
				return 0
			if k==2:
				return 0
			if k==3:
				return 6
			return 1/0
		def wSingleInterval_get(self,x,vc):
			w=self.bb(x)
			for k in range(4):
				w+=vc[k]*self.aa(x,k)
			return w
		def w2SingleInterval_get(self,x,vc):
			w2=self.bb2(x)
			for k in range(4):
				w2+=vc[k]*self.aa2(x,k)
			return w2
		def vc_get(self,x,vvc,v_x_anchor):
			iInterval=self.iInterval_get(x,v_x_anchor)
			vc = vvc[iInterval*4:iInterval*4 + 4]
			return vc
		def w_get(self,x,vvc,v_x_anchor):
			vc=self.vc_get(x,vvc,v_x_anchor)
			return self.wSingleInterval_get(x,vc)
		def w2_get(self,x,vvc,v_x_anchor):
			vc=self.vc_get(x,vvc,v_x_anchor)
			return self.w2SingleInterval_get(x,vc)
		# A * x = b
		# size of x is 4 * (כמות אנכורים +1)
		# size of b is 4 * (כמות אנכורים +1)
		# size of A is (4 * (כמות אנכורים +1))^2

		# list pf the anchor places - v_x_anchor

		def vvc_get(self,v_x_anchor):#vc=
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
					x=self.xMax
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
					# w'''(xMax)=0
					# -(F*cos(A)*xMax**2)/(2*E*I) + xMax*h/(E*I) + c_1*6 = 0
					x=self.xMax
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
				self.bTheLastAnchor_h=(abs(self.xMax-v_x_anchor[n-1])<0.01)
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
		def vw_get(self,vx,vvc,v_x_anchor):#vy=
			vw = []
			for x in vx:
				w=self.w_get(x,vvc,v_x_anchor)
				vw.append(w)
			return vw
		def vw2_get(self,vx,vvc,v_x_anchor):#vy2=
			vw2 = []
			for x in vx:
				w2=self.w2_get(x,vvc,v_x_anchor)
				vw2.append(w2)
			return vw2
		def xy_get(self,v_x_anchor,nPoints=300,bGraph=True):
			
			vvc = self.vvc_get(v_x_anchor)
			
			x_data = np.linspace(0,self.xMax,nPoints+1)
			vx=x_data.tolist()
			
			vy=self.vw_get(vx,vvc,v_x_anchor)
			y_data = np.array(vy)
			
			if bGraph:
				#accurate graph for w'''' only, more accurate calculation than by points only
				MyMath=clMyMath()
				nPoints=10000
				x_data0 = np.linspace(0,self.xMax,nPoints+1)
				vx=x_data0.tolist()
				def ff(x):
					return self.w_get(x,vvc,v_x_anchor)

				#vx=[0,1,2,3]
				vxNoNeedHighestDiff=v_x_anchor
				MyMath.graphDir(vx,f=ff,vy=[],kMin=4,kMax=4,dx=0.005,bMoreMax=True,sf="W",sTitle="Analytic solution: accurate w, numerical w''''' good for dx>0.005",vxNoNeedHighestDiff=vxNoNeedHighestDiff)#for smaller dx (0.001 and less) it is not enough accuracy: dx^4 is 10^(-12) 
			
			MomentMax, xArgMax = self.MomentMax_get(0.1,vvc,v_x_anchor)
			
			
			return x_data, y_data, MomentMax

		def MomentMax_get(self,dx,vvc,v_x_anchor):#MomentMax,xArgMax=
			def MomentBeam_get():
				w2=self.w2_get(x,vvc,v_x_anchor)
				return self.Wall.MomentBeam_get(w2)
				
			x=0
			MomentMax=MomentBeam_get()
			xArgMax=x
			while x<=self.xMax:
				M=MomentBeam_get()
				if abs(M)>abs(MomentMax):
					MomentMax=M
					xArgMax=x
				x+=dx
			return MomentMax,xArgMax

	class clBeamNumerical():
		def __init__(self,Wall,n=300):
			self.Wall=Wall
			self.xMax=self.Wall.yMax
			
			self.vx = []
			for ix in range(n+1):
				self.vx.append(float(ix)*self.xMax/n)
			
			self.vvIndex= []
			self.vw = [0] * (n + 1)
			self.dx=float(self.xMax)/n
		def ix_get(self,x):
			if x<=0:
				return 0
			if x>=self.xMax:
				return len(self.vx)-1
			return int((float(x)/self.xMax)*(len(self.vx)-1))
		def vvIndex_make(self,v_x_anchor):
			#v_x_anchor - ordered by increasing, dist at least 0.1, 0.1<x_anchor<=h, 
			self.vvIndex= []
			for x in self.vx:
				self.vvIndex.append([])
			
			ix=0
			nx=len(self.vx)
			for x in self.vx:
				if ix>1 and ix<nx-2:
					self.vvIndex[ix].append(4)
				ix+=1
			#print("vvIndex="+str(self.vvIndex))
			
			#w=0, w'=0
			self.vvIndex[0].append(0)
			self.vvIndex[0].append(1)
			#print("vvIndex="+str(self.vvIndex))
			
			#w''=0, w'''=0
			self.vvIndex[nx-2].append(2)
			self.vvIndex[nx-3].append(3)
			#print("vvIndex="+str(self.vvIndex))
			
			for x in v_x_anchor:
				ix=self.ix_get(x)
				self.vvIndex[ix].append(0)#w=0, may be no w''''
				if ix<nx-2:
					self.vvIndex[ix].append(-1)
				else:
					self.vvIndex[nx-2-1].append(-1)#(to have correct number of equations)
			#print("vvIndex="+str(self.vvIndex))
		def w(self,x):
			#use after vw_make()
			ix=self.ix_get(x)
			return self.vw[ix]
		def w2_get(self,x):
			# ix=self.ix_get(x)
			# if ix>=len(self.vx)-3:
			# ix=len(self.vx)-3
			# w_1=self.vw[ix]
			# w_2=self.vw[ix+1]
			# w_3=self.vw[ix+2]
			# x_1=vx[ix]
			# x_2=vx[ix+1]
			# x_3=vx[ix+2]
			MyMath=clMyMath()
			MyMath.y_start(self.vx,self.vw)
			df=vx[1]-vx[0]
			w2=MyMath.fk(x,MyMath.y_get,dx,2)
		def MomentMax_get(self):#MomentMax,xArgMax=
			MyMath=clMyMath()
			MyMath.y_start(self.vx,self.vw)
			dx=self.vx[1]-self.vx[0]
			def MomentBeam_get():
				w2=MyMath.fk(x,MyMath.y_get,dx,2)
				#print(str(x)+" "+str(w2))
				return self.Wall.MomentBeam_get(w2)

			x=self.vx[0]
			MomentMax=MomentBeam_get()
			xArgMax=x
			ix=0
			for x in self.vx:
				if ix<len(self.vx)-2:#for others impossible to calculate w''
					M=MomentBeam_get()
					if abs(M)>abs(MomentMax):
						MomentMax=M
						xArgMax=x
				x+=dx
				ix+=1
			# print("MomentMax="+str(MomentMax)+", xArgMax="+str(xArgMax))
			return MomentMax,xArgMax
		def vw_make(self, print_to_file=True):
			# print("clBeamNumerical.vw_make...")
			n = len(self.vx)
			v_b=[]
			v_b = [0] * n
			vv_A = [[0 for col in range(n)] for row in range(n)]
			#vix=[]
			u=0
			MyMath=clMyMath()
			
			
			for ix in range(n):

				x=self.vx[ix]
				if (4 in self.vvIndex[ix]) and not (-1 in self.vvIndex[ix]):
					# w'''' = q(x)/(EI)
					vcf=MyMath.vcf_get(4)
					c=float(1)/self.dx**4
					for i in range(4+1):
						vv_A[u][ix-2+i]=c*vcf[i]
					v_b[u] = float(self.Wall.q_get(x))/self.Wall.E_Ic
					u+=1
				if 0 in self.vvIndex[ix]:
					#w=0
					vv_A[u][ix]=1
					v_b[u]=0
					u+=1
				if 1 in self.vvIndex[ix]:
					#w'=0
					vcf=MyMath.vcf_get(1)
					c=float(1)/self.dx
					for i in range(1+1):
						v=c*vcf[i]
						#print("u="+str(u))
						#print("ix+i="+str(ix+i))
						#print("n="+str(n))
						
						vv_A[u][ix+i]=v
					v_b[u]=0
					u+=1
				if 2 in self.vvIndex[ix]:
					#w''=0
					vcf=MyMath.vcf_get(2)
					c=float(1)/self.dx**2
					for i in range(2+1):
						vv_A[u][ix-1+i]=c*vcf[i]
					v_b[u]=0
					u+=1
				if 3 in self.vvIndex[ix]:
					#w'''=0
					vcf=MyMath.vcf_get(3)
					c=float(1)/self.dx**3
					for i in range(3+1):
						vv_A[u][ix-1+i]=c*vcf[i]
					v_b[u]=0
					u+=1

			if print_to_file:
				MyMath.printMatrixToFile(vv_A,"A.txt")
				MyMath.printVectorToFile(v_b,"b.txt")
	
			self.vw = np.linalg.solve(vv_A, v_b)
		
			x_data = np.array(self.vx)
			y_data = np.array(self.vw)

			return x_data,y_data
	def vx_anchors_get(self,index):
		vx_anchors = []
		if index==0:# 2m, MomentMax=1.4*10^6
			pass
		if index==10:#15 cm, MomentMax=0.57*10^6
			vx_anchors = [self.yMax]
		if index==5:#8 cm, MomentMax=0.17*10^6
			vx_anchors = [0.5*self.yMax]
		if index==5.5:#0.3 mm, MomentMax=0.027*10^6
			vx_anchors = [2,4,6,8,10]
		return vx_anchors
	def testBeam(self, anchors, analytical=True, drew_graph=True):
		self.start()

		MyMath=clMyMath()

		if analytical:
			BeamAnalytical=self.clBeamAnalytical(self)
			x_data, y_data, max_moment=BeamAnalytical.xy_get(anchors, 100, bGraph=drew_graph)
			MyMath.testSol(x_data, y_data, kMin=0, kMax=4,sf="w", drew_graph=drew_graph, sTitle="Analytic solution: for selected points only (no w''''in anchors and in the end)", vxNoNeedHighestDiff=anchors)

		# else:
		# 	BeamNumerical=self.clBeamNumerical(self,1000)#,4)#10000)
		# 	BeamNumerical.vvIndex_make(anchors)
		# 	x_data,y_data=BeamNumerical.vw_make(print_to_file=drew_graph)
		# 	max_moment, x_place = BeamNumerical.MomentMax_get()
		# 	MyMath.testSol(x_data,y_data,kMin=0,kMax=4,sf="w", drew_graph=drew_graph, sTitle="Numerical solution: for selected points only (no w''''in anchors and in the end)",vxNoNeedHighestDiff=anchors)

		return max_moment

	def v_xy_anchor_get(self,index):
		v_xy_anchor=[]
		if index==0:
			v_xy_anchor=[]
		if index==1:
			v_xy_anchor=[[5,5]]
		if index==1.1:
			v_xy_anchor=[[5,1]]
		if index==5.2:
			v_xy_anchor=[[5,5],[5,10]]
		if index==5.5:
			v_xy_anchor=[[3,5],[4,5],[5,5],[6,5],[7,5]]
		if index==10.1:
			v_xy_anchor=[[5,10]]
		if index==10.5:
			v_xy_anchor=[[3,10],[4,10],[5,10],[6,10],[7,10]]
		return v_xy_anchor
	def testWall(self, v_xy_anchor=[], bLoop=False, print_all=True):
		WallNumerical=self.clWallNumerical(self,nx=100,ny=100)#,nx=4,ny=4)#,nx=50,ny=50)#
		# vvcc=WallNumerical.vvcc_get()
		# v_xy_anchor=self.v_xy_anchor_get(0)

		# if the borders acts like ground - False
		# True -> the wall acts cycle
		
		WallNumerical.vvvIndex_make(v_xy_anchor,bLoop)
		WallNumerical.vvw_make(bLoop, print_all)
		if print_all:
			WallNumerical.drewGraphs(v_xy_anchor)
		
		#print(WallNumerical.MomentMax_wall_get())
	
		return WallNumerical.MomentMax_wall_get()
	class clWallNumerical():
		def __init__(self,Wall,nx=10,ny=10, print_all=True):
			self.Wall = Wall
			self.xMax = self.Wall.xMax
			self.yMax = self.Wall.yMax
			self.print_all = print_all

			self.vx = []
			for ix in range(nx+1):
				self.vx.append(float(ix)*self.xMax/nx)

			self.vy = []
			for iy in range(ny+1):
				self.vy.append(float(iy)*self.yMax/ny)
				
				
			self.bSym = True#with false it is working wrong
			
			self.vvw = [[0 for col in range(ny+1)] for row in range(nx+1)]
			self.dx=float(self.xMax)/nx
			self.dy=float(self.yMax)/ny
		def vvcc_get(self):
			#D (w_xxxx(iv)(x,y)+2w_xxyy(iv)(x,y)+w_yyyy(iv)(x,y))=q(x,y)
			#vvcc are coef for w_xxxx(iv)(x,y)+2w_xxyy(iv)(x,y)+w_yyyy(iv)(x,y)
			vvcc=[[0 for col in range(4+1)] for row in range(4+1)]
			MyMath=clMyMath()
			vcf=MyMath.vcf_get(4)
			vvcf=MyMath.vvcf_get(2,2)
			#print(str(vvcf))
			if self.bSym:
				for k in range(4+1):
					vvcc[k][2]+=float(vcf[k])/self.dx**4
					vvcc[2][k]+=float(vcf[k])/self.dy**4
				#print(str(vvcc))
				for kx in range(4+1-2):
					for ky in range(4+1-2):
						vvcc[kx+2-1][ky+2-1]+=2*float(vvcf[kx][ky])/((self.dx**2)*(self.dy**2))
				#print(str(vvcc))
			else:
				for k in range(4+1):
					vvcc[k][0]+=float(vcf[k])/self.dx**4
					vvcc[0][k]+=float(vcf[k])/self.dy**4
				#print(str(vvcc))
				for kx in range(4+1):
					for ky in range(4+1):
						vvcc[kx][ky]+=2*float(vvcf[kx][ky])/((self.dx**2)*(self.dy**2))
				#print(str(vvcc))
			return vvcc
		def ix_get(self,x):
			if x<=0:
				return 0
			if x>=self.xMax:
				return len(self.vx)-1
			return int((float(x)/self.xMax)*(len(self.vx)-1))
		def iy_get(self,y):
			if y<=0:
				return 0
			if y>=self.yMax:
				return len(self.vy)-1
			return int((float(y)/self.yMax)*(len(self.vy)-1))
		def vvvIndex_make(self,v_xy_anchor,bLoop):
			#v_xy_anchor - dist at least 0.1, 0.1<x_anchor<=xMax-0.1, 0.1<y_anchor
			#y=0, y'=0 => y(x+dx)=0
			nx=len(self.vx)-1
			ny=len(self.vy)-1
			self.vvvIndex= [[[] for col in range(ny+1)] for row in range(nx+1)]
			for ix in range(nx+1):
				for iy in range(ny+1):
					if self.bSym:
						if iy>=2 and iy<=ny-2 and (bLoop or (ix>=2 and ix<=nx-2)):
							self.vvvIndex[ix][iy].append(4)
					else:
						if iy<=ny-4 and (bLoop or ix<=nx-4):
							self.vvvIndex[ix][iy].append(4)
			#2*(nx+1)
			ix=0
			for x in self.vx:
				self.vvvIndex[ix][0].append(0)#w=0
				self.vvvIndex[ix][1].append(0)#w=0
				ix+=1

			if bLoop:
				#fourth derivatives => need four more on y => need (nx+1)*4 border coditions
				#(nx+1)*2
				ix=0
				for x in self.vx:
					#if ix>1 and ix<nx-1:
					if self.bSym:
						self.vvvIndex[ix][ny-1].append(2)#w''=0
						self.vvvIndex[ix][ny-2].append(3)#w'''=0
					else:
						self.vvvIndex[ix][ny-2].append(2)#w''=0
						self.vvvIndex[ix][ny-3].append(3)#w'''=0
					ix+=1
			else:
				#fourth derivatives => need four more on x, need four more on y => need (nx+1)*4+(ny+1)*4-16 border coditions
				#w=0 on x=0,y=0,x=xMax : 2*(ny+1)+(nx+1)-2 conditions
				#w'y=0 on y=0, w'x=0 on x=0, x=xMax: 2*ny+(nx-3) conditions, itogo 4*ny+2*nx-2, need (nx-3)*2 conditions
				#w''y=w'''y=0 for y=yMax
				
				#4*(ny-1)
				iy=0
				for y in self.vy:
					if iy>1:
						self.vvvIndex[0][iy].append(0)#w=0
						self.vvvIndex[1][iy].append(0)#w=0
						self.vvvIndex[nx-1][iy].append(0)#w=0
						self.vvvIndex[nx][iy].append(0)#w=0
					iy+=1
				
				#(nx-3)*2
				ix=0
				for x in self.vx:
					if ix>1 and ix<nx-1:
						if self.bSym:
							self.vvvIndex[ix][ny-1].append(2)#w''=0
							self.vvvIndex[ix][ny-2].append(3)#w'''=0
						else:
							self.vvvIndex[ix][ny-2].append(2)#w''=0
							self.vvvIndex[ix][ny-3].append(3)#w'''=0
					ix+=1
			
			#anchors
			for xy_anchor in v_xy_anchor:
				x=xy_anchor[0]
				y=xy_anchor[1]
				ix=self.ix_get(x)
				iy=self.iy_get(y)
				self.vvvIndex[ix][iy].append(0)
				if iy<=ny-2:
					self.vvvIndex[ix][iy].append(-1)#w=0, no need w''''
				else:
					self.vvvIndex[ix][ny-2].append(-1)#w=0, no need w'''' (to have correct number of equations)
		def w_get(self,x,y):
			#use after vw_make()
			ix=self.ix_get(x)
			iy=self.iy_get(y)
			return self.vvw[ix][iy]
		def w2_get(self,ix,iy,index):
			MyMath=clMyMath()
			if index==1:#w''xx
				vcf=MyMath.vcf_get(2)
				c=float(1)/self.dx**2
				i0=1
				if ix==0:
					i0=0
				if ix==len(self.vx)-1:
					i0=2
				w2=0
				for i in range(2+1):
					w2+=c*vcf[i]*self.vvw[ix+i-i0][iy]
				#if w2>0.01:
				#	print(str([self.vvw[ix+0-i0][iy],self.vvw[ix+1-i0][iy]],self.vvw[ix+2-i0][iy]))
					
				return w2
			if index==2:#w''xx
				vcf=MyMath.vcf_get(2)
				c=float(1)/self.dy**2
				i0=1
				if iy==0:
					i0=0
				if iy==len(self.vy)-1:
					i0=2
				w2=0
				for i in range(2+1):
					w2+=c*vcf[i]*self.vvw[ix][iy+i-i0]
				return w2
			#w''xy
			i0=0
			j0=0
			if ix==len(self.vx)-1:
				i0=1
			if iy==len(self.vy)-1:
				j0=1
			c=float(1)/(self.dx*self.dy)
			w2=0
			w2+=c*self.vvw[ix-i0+1][iy-j0+1]
			w2-=c*self.vvw[ix-i0][iy-j0+1]
			w2-=c*self.vvw[ix-i0+1][iy-j0]
			w2+=c*self.vvw[ix-i0][iy-j0]
			return w2

		def Moment_get(self,ix,iy,index):
			#Mxx(x,y)=-D(w’’xx(x,y)-v w’’yy(x,y))
			#Myy(x,y)=-D(w’’yy(x,y)-v w’’xx(x,y))
			#Mxy(x,y)=-D(1-v) w’’xy(x,y))
			if index==1:
				return -self.Wall.dd*(self.w2_get(ix,iy,1)-self.Wall.v*self.w2_get(ix,iy,2))
			if index==2:
				return -self.Wall.dd*(self.w2_get(ix,iy,2)-self.Wall.v*self.w2_get(ix,iy,1))
			return -self.Wall.dd*(1-self.Wall.v)*self.w2_get(ix,iy,3)

		def MomentMax_wall_get(self):
			m_max = 0
   
			for ix in range(len(self.vx)):
				for iy in range(len(self.vy)):
					m = self.Moment_get(ix,iy,1) + self.Moment_get(ix,iy,2) + self.Moment_get(ix,iy,3)
					if abs(m) > m_max:
						m_max = abs(m)
			return m_max

		def MomentMax_get(self):#MomentMax,xArgMax=
			MyMath=clMyMath()
			MyMath.y_start(self.vx,self.vw)
			dx=self.vx[1]-self.vx[0]
			def MomentBeam_get():
				w2=MyMath.fk(x,MyMath.y_get,dx,2)

				return self.Wall.MomentBeam_get(w2)
				
			x=self.vx[0]
			MomentMax=MomentBeam_get()
			xArgMax=x
			ix=0
			for x in self.vx:
				#if self.vIndex[ix]
				if ix<len(self.vx)-2:#for others impossible to calculate w''
					M=MomentBeam_get()
					if abs(M)>abs(MomentMax):
						MomentMax=M
						xArgMax=x
				x+=dx
				ix+=1
			# print("MomentMax="+str(MomentMax)+", xArgMax="+str(xArgMax))
			return MomentMax,xArgMax
		def vvw_make(self, bLoop, print_all):
			nx=len(self.vx)-1
			ny=len(self.vy)-1
			n = (nx+1)*(ny+1)
			v_b=[]
			v_b = [0] * n
			vv_A = [[0 for col in range(n)] for row in range(n)]
			vvcc=self.vvcc_get()
			MyMath=clMyMath()
			vc2=MyMath.vcf_get(2)
			vc3=MyMath.vcf_get(3)
			
			def iVar_get(ix,iy,nx,ny,bLoop):
				if ix>nx and bLoop:
					ix-=nx+1
				if ix<0:
					ix+=nx+1
				iVar=ix*(ny+1)+iy
				return iVar
			u=0
			for ix in range(nx+1):
				x=self.vx[ix]
				for iy in range(ny+1):
					y=self.vy[iy]
					
					if (4 in self.vvvIndex[ix][iy]) and not (-1 in self.vvvIndex[ix][iy]):#>=0 and (iy<=ny-4) and (ix<=nx-4 or bLoop):
						for i in range(4+1):
							for j in range(4+1):
								if self.bSym:
									iVar=iVar_get(ix+i-2,iy+j-2,nx,ny,bLoop)
								else:
									iVar=iVar_get(ix+i,iy+j,nx,ny,bLoop)
								vv_A[u][iVar]=vvcc[i][j]
						v_b[u] = float(self.Wall.q_get(y))/self.Wall.dd
						u+=1
					
					if 0 in self.vvvIndex[ix][iy]:#w=0
						iVar=iVar_get(ix,iy,nx,ny,bLoop)
						vv_A[u][iVar]=1
						v_b[u]=0
						u+=1
					
					if 2 in self.vvvIndex[ix][iy]:#w''=0
						for j in range(2+1):
							if self.bSym:
								iVar=iVar_get(ix,iy+j-1,nx,ny,bLoop)
							else:
								iVar=iVar_get(ix,iy+j,nx,ny,bLoop)
							vv_A[u][iVar]=float(vc2[j])/self.dy**2
						v_b[u]=0
						u+=1
					
					if 3 in self.vvvIndex[ix][iy]:#w'''=0
						for j in range(3+1):
							if self.bSym:
								iVar=iVar_get(ix,iy+j-1,nx,ny,bLoop)
							else:
								iVar=iVar_get(ix,iy+j,nx,ny,bLoop)
							vv_A[u][iVar]=float(vc3[j])/self.dy**3
						v_b[u]=0
						u+=1
			
			if print_all:
				MyMath.printMatrixToFile(self.vvvIndex,"vvvIndex.txt")
			
			vVar= np.linalg.solve(vv_A, v_b)
			
			iVar=0
			for ix in range(nx+1):
				for iy in range(ny+1):
					self.vvw[ix][iy]=vVar[iVar]
					iVar+=1
			
			if print_all:
				MyMath.printMatrixToFile(self.vvw,"ww.txt")
			
		def drewGraphs_XY_get(self):#X, Y =
			#N = 100
			#X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
			X, Y = np.mgrid[self.vx[0]:self.vx[len(self.vx)-1]:complex(0, len(self.vx)), self.vy[0]:self.vy[len(self.vy)-1]:complex(0, len(self.vy))]
			return X,Y
		def drewGraphs_Z_w_get(self):#Z=
			#Z=X+Y
			Z=[]
			for ix in range(len(self.vx)):
				vZ=[]
				for iy in range(len(self.vy)):
					vZ.append(self.vvw[ix][iy])
				Z.append(vZ)
			return Z
		def drewGraphs_Z_w2_get(self,index):#Z=
			#Z=X+Y
			vvZ=[]
			#print(str(index))
			for ix in range(len(self.vx)):
				vZ=[]
				for iy in range(len(self.vy)):
					if index<=3:
						z=self.w2_get(ix,iy,index)
					else:
						z=self.Moment_get(ix,iy,index-3)
					vZ.append(z)
				vvZ.append(vZ)
			return vvZ
		def drewGraphs_subraph(self,X,Y,Z,v_xy_anchor,sTitle,ax):
			cmap = cm.coolwarm
			MyMath=clMyMath()
			argMin,argMax=MyMath.vvz_argMin_argMax_get(Z)
			Zmin=Z[argMin[0]][argMin[1]]
			Zmax=Z[argMax[0]][argMax[1]]
			s1="argMin="+str(argMin)+"=("+str(self.vx[argMin[0]])+","+str(self.vx[argMin[1]])+")"
			s2="argMax="+str(argMax)+"=("+str(self.vx[argMax[0]])+","+str(self.vx[argMax[1]])+")"
			s=sTitle+": "+s1+", "+s2
			print(s+", "+sTitle+"_min="+str(Zmin)+", "+sTitle+"_max="+str(Zmax))
			if Zmin<Zmax:
				pc = ax.pcolormesh(X,Y,Z, cmap=cmap)
			
			ax.set_title(sTitle)
			if len(v_xy_anchor)>0:
				vx=[]
				vy=[]
				for xy_anchor in v_xy_anchor:
					x=xy_anchor[0]
					y=xy_anchor[1]
					vx.append(x)
					vy.append(y)
					#ix=self.ix_get(x)
					#iy=self.iy_get(y)
					
				x_data=np.array(vx)
				y_data=np.array(vy)
				ax.plot(x_data,y_data,"o", color = "black")
				#print(str(x_data))
				#print(str(y_data))
			return pc,Zmin<Zmax
		def drewGraphs(self,v_xy_anchor=[]):
			MyMath=clMyMath()
			
			
			
			X, Y =self.drewGraphs_XY_get()
			for i in range(1+3+3):
				fig, ax = plt.subplots()
				if i==0:
					Z=self.drewGraphs_Z_w_get()
					sTitle="W"
					MyMath.printMatrixToFile(Z,"ww.txt")
				if i==1:
					Z=self.drewGraphs_Z_w2_get(1)
					sTitle="Wxx"
					MyMath.printMatrixToFile(Z,"wwxx.txt")
				if i==2:
					Z=self.drewGraphs_Z_w2_get(2)
					MyMath.printMatrixToFile(Z,"wwyy.txt")
					sTitle="Wyy"
				if i==3:
					Z=self.drewGraphs_Z_w2_get(3)
					sTitle="Wxy"
				#if i==4:
				#	Z=self.drewGraphs_Z_w2_get(4)
				#	sTitle="Mxx-Myy"
				if i==4:
					Z=self.drewGraphs_Z_w2_get(4)
					sTitle="Mxx"
					MyMath.printMatrixToFile(Z,"mmxx.txt")
				if i==5:
					Z=self.drewGraphs_Z_w2_get(5)
					MyMath.printMatrixToFile(Z,"mmyy.txt")
					sTitle="Myy"
				if i==6:
					Z=self.drewGraphs_Z_w2_get(6)
					sTitle="Mxy"
				pc,b=self.drewGraphs_subraph(X,Y,Z,v_xy_anchor,sTitle,ax)
				if b:
					fig.colorbar(pc, ax=ax)
				fig.savefig(sTitle+'.jpg')

class clMyMath():
	# נוסחה לנגזרת: 

	# def dirivative(func, x, dx):
	#	 return float(func(x+dx) - func(x))/dx

	# def double_dirivative(func, x, dx):
	#	 return (dirivative(func, x + dx, dx) - )
	def f1(self,x,f,dx):
		return float(f(x+dx)-f(x))/dx
	def f2(self,x,f,dx):
		return float(self.f1(x+dx,f,dx)-self.f1(x,f,dx))/dx#(f(x+2dx)-2f(x+dx)+f(x))/dx^2
	def f3(self,x,f,dx):
		return float(self.f2(x+dx,f,dx)-self.f2(x,f,dx))/dx#(f(x+3dx)-3f(x+2dx)+3f(x+dx)-f(x))/dx^3
	def f4(self,x,f,dx):
		return float(self.f3(x+dx,f,dx)-self.f3(x,f,dx))/dx#(f(x+4dx)-4f(x+3dx)+8f(x+2dx)-4f(x+dx)+f(x))/dx^4
	def fk(self,x,f,dx,k):#numerical derivative
		if k==0:
			return f(x)
		#if k==1:
		#	return self.f1(x,f,dx)
		#if k==2:
		#	return self.f2(x,f,dx)
		#if k==3:
		#	return self.f3(x,f,dx)
		#if k==4:
		#	return self.f4(x,f,dx)
		y1=self.fk(x+dx,f,dx,k-1)
		y=self.fk(x,f,dx,k-1)
		dyFracdx=float(y1-y)/dx
		#print("fk: x="+str(x)+", k="+str(k)+", y1="+str(y1)+", y="+str(y)+", y'="+str(dyFracdx))
		return dyFracdx
	def ffkk(self,x,y,ff,dx,dy,kx,ky):#partial numerical derivative
		if kx==0 and ky==0:
			return ff(x,y)
		if ky>0:
			fff1=self.ffkk(x,y+dy,ff,dx,dy,kx,ky-1)
			fff=self.ffkk(x,y,ff,dx,dy,kx,ky-1)
			dFdy=float(fff1-fff)/dy
			#print("fk: x="+str(x)+", k="+str(k)+", y1="+str(y1)+", y="+str(y)+", y'="+str(dyFracdx))
			return dFdy
		if kx>0:
			fff1=self.ffkk(x+dx,y,ff,dx,dy,kx-1,ky)
			fff=self.ffkk(x,y,ff,dx,dy,kx-1,ky)
			dFdx=float(fff1-fff)/dx
			return dFdx
	def y_start(self,vx,vy):
		self.vx=vx
		self.vy=vy
	def y_get(self,x):
		#dx=const>0
		n=len(self.vx)
		if x<=self.vx[0]:
			return self.vy[0]
		if x>=self.vx[n-1]:
			return self.vy[n-1]
		ix=self.ix_get(x,self.vx)
		dy=(x-self.vx[ix])*float(self.vy[ix+1]-self.vy[ix])/(self.vx[ix+1]-self.vx[ix])
		y=self.vy[ix]+dy
		return y
	def ix_get(self,x,vx):
		n=len(self.vx)
		ix=int((float(x-self.vx[0])/(self.vx[n-1]-self.vx[0]))*(n-1))#from 0 to n-2
		#print("x="+str(x)+" nx="+str(n)+" ny="+str(len(vy))+" ix="+str(ix))
		return ix
	def vvx_vvy_dk_get(self,f=None,vx=None,kMax=4,dx=None,bMoreMax=False):
		#vx is ordered, x[i+1]-x[i] is constant >0
		#self.y_get
		if vx is None:
			vx=self.vx
		if dx is None:
			dx=vx[1]-vx[0]
		if f is None:
			if dx<vx[1]-vx[0]:
				dx=vx[1]-vx[0]
			f=self.y_get
		#print("self.vx="+str(self.vx))
		#print("self.vy="+str(self.vy))
		vvy=[]
		vvx=[]
		n=len(vx)
		xMax=vx[n-1]
		for k in range(kMax+1):
			vxk=[]
			vyk=[]
			for x in vx:
				if bMoreMax or x+dx*k<=xMax:
					y=self.fk(x,f,dx,k)
					vxk.append(x)
					vyk.append(y)
					#print("x="+str(x))
			vvx.append(vxk)
			vvy.append(vyk)
		return vvx,vvy
	def graphDir(self,vx,f=None,vy=None,kMin=0,kMax=4,dx=None,bMoreMax=False,sf="f",sTitle="sTitle",vxNoNeedHighestDiff=[]):
		#print(str(locals()))
		#print(str(vx))
		n=len(vx)
		plt.close()
		plt.title(sTitle)
		
		#drew axis x
		x_data=np.array([vx[0],vx[n-1]])
		y_data=np.array([0,0])
		plt.plot(x_data,y_data, color="black")
		
		for x in vxNoNeedHighestDiff:
			plt.plot(x, 0, marker="o", markersize=7, markeredgecolor="red",markerfacecolor="black")

		f0=f
		if f is None:
			self.y_start(vx,vy)
			f0=self.y_get
		#print("vx="+str(vx))
		#print("vy="+str(vy))
		vvx,vvy=self.vvx_vvy_dk_get(f=f0,vx=vx,kMax=kMax,dx=dx,bMoreMax=bMoreMax)
		for k in range(kMin,kMax+1):
			vxk=vvx[k]
			vy=vvy[k]

			if len(vxk)>1:
				if k==kMax and len(vxNoNeedHighestDiff)>0:
					if dx is None:
						dx=vxk[1]-vxk[0]
					vxkPP=[]
					vyPP=[]
					for i in range(len(vxk)):
						x=vxk[i]
						y=vy[i]
						bOk=True
						for xN in vxNoNeedHighestDiff:
							if x<xN and x+kMax*dx>=xN:
								bOk=False
								break
						if bOk:
							vxkPP.append(x)
							vyPP.append(y)
					vxk=vxkPP
					vy=vyPP
		
			x_data = np.array(vxk)
			y_data = np.array(vy)
			#"bb''''"
			s=sf
			for i in range(k):
				s+="'"
			plt.plot(x_data,y_data, label = s)
		plt.legend()
		plt.savefig("plot.jpg")
		plt.close()


	def testSol(self,x_data,y_data,kMin=0,kMax=4,sf="f", drew_graph=True,sTitle="sTitle",vxNoNeedHighestDiff=[]):#x1_data,y1_data
		MyMath=clMyMath()
		vx=x_data.tolist()#ordered, equal dist
		n=len(vx)
		vy=y_data.tolist()

		if drew_graph:
			MyMath.graphDir(vx,f=None,vy=vy,kMin=kMin,kMax=kMax,dx=None,bMoreMax=False,sf=sf,sTitle=sTitle,vxNoNeedHighestDiff=vxNoNeedHighestDiff)
		
		return

	def vcf_get(self,k):#binomial coeffecients with sign (for numerical calculation of derivatives)
		#starting from x, x+dx, x+2*dx
		#k=0 -> [1]: f^{(0)}(x)=f(x)
		#k=1 -> [1,-1]: f^{(1)}(x)=(f(x+dx)-f(x))/dx
		#k=2 -> [1,-2,1]: f^{(2)}(x)=(f(x+2*dx)-2*f(x+dx)+f(x))/dx^2
		#
		#starting from f(x):
		#k=0 -> [1]: f^{(0)}(x)=f(x)
		#k=1 -> [-1,1]: f^{(1)}(x)=(f(x+dx)-f(x))/dx
		#k=2 -> [1,-2,1]: f^{(2)}(x)=(f(x+2*dx)-2*f(x+dx)+f(x))/dx^2
		
		vc=[1]
		for ik in range(k):
			vcPP=[1]
			h=-1
			for ic in range(len(vc)-1):
				vcPP.append(h*(abs(vc[ic])+abs(vc[ic+1])))
				h=-h
			vcPP.append(h)
			vc=vcPP
		#print("k="+str(k)+", vc="+str(vc))
		return self.vxRev_get(vc)
	def vxRev_get(self,vx):
		n=len(vx)
		vxRev=[]
		for i in range(n):
			vxRev.append(vx[n-i-1])
		return vxRev
	def vvcf_get(self,kx,ky):
		vcx=self.vcf_get(kx)
		vcy=self.vcf_get(ky)
		vvcf=[]
		k=kx+ky
		for i in range(k+1):
			vcf=[]
			for j in range(k+1):
				cf=0
				if i<=kx and j<=ky:
					cf=vcx[i]*vcy[j]
				vcf.append(cf)
			vvcf.append(vcf)
		return vvcf
	def test1(self):
		vx=[0]
		n=100
		xMax=1
		kMax=4
		dx=float(1)/n
		for ix in range(n):
			vx.append(xMax*dx*(ix+1))
		x_data = np.array(vx)
		
		vvy=[]
		vy_data=[]
		for k in range(kMax+1):
			vy=[]
			for x in vx:
				vy.append(x**k)
			vvy.append(vy)
			y_data = np.array(vy)
			vy_data.append(y_data)
		#for k in range(kMax+1):
		#	plt.plot(x_data,vy_data[k], label = "y"+str(k))

		dx=float(1)/n
		vvy_data=[]
		for k1 in range(kMax+1):
			vy_data=[]
			for k in range(kMax+1):
				vy=vvy[k]
				#print("vy="+str(vy))
				MyMath.y_start(vx,vy)
				vyk=[]
				for x in vx[:len(vx)-k1]:
					yk=MyMath.fk(x,MyMath.y_get,dx,k1)
					vyk.append(yk)
				#print("vyk="+str(vyk))
				y_data = np.array(vyk)
				x_data=np.array(vx[:len(vx)-k1])
				if k==kMax:
					plt.plot(x_data,y_data, label = "y"+str(k)+str(k1))
					print("vyk="+str(vyk))
				vy_data.append(y_data)
			vvy_data.append(vy_data)
		
		plt.legend()
		#plt.show()
		
			#x1_data,y1_data,x4_data,y4_data=
		
		#plt.plot(x_data,y_data, label = "w")
		#plt.plot(x_data,y2_data, label = "w''")
		#plt.plot([0,h],[0,0], label = "x")
		#lines:
		#https://www.w3schools.com/python/matplotlib_line.asp
		#points:
		#plt.plot(xpoints, ypoints, 'o')
		#line with markers
		#https://www.w3schools.com/python/matplotlib_markers.asp
		#plt.plot(ypoints, marker = 'o')
		#plt.plot(ypoints, marker = '*')
		
		
		#plt.plot(x1_data,y1_data, label = "w'")
		#plt.plot(x4_data,y4_data, label = "w''''")

		#x_data,y_data=BeamDef.vw_make()
		#plt.plot(x_data,y_data, label = "wDiff")

		#plt.legend()
		#plt.show()
		pass
	def ixGeneral_get(self,x,xMin,xMax,n):
		if x<=xMin:
			return xMin
		if x>=xMax:
			return n-1
		return int(float(x)/(xMax-xMin)*(n-1))
	def printMatrixToFile(self,vvA,sFileName):
		f=open(sFileName,'w')
		nx=len(vvA)
		ny=len(vvA[0])
		iRow=0
		for row in vvA:
			s=""
			iCol=0
			for col in row:
				if iCol>0:
					s+="\t"
				s+=str(col)
				iCol+=1
			f.write(s+"\n")
			iRow+=1
		f.close()
	def printVectorToFile(self,vb,sFileName):
		f=open(sFileName,'w')
		nx=len(vb)
		iRow=0
		for row in vb:
			f.write(str(row)+"\n")
			iRow+=1
		f.close()
	def vx_vy_vc_Graph__get(self,vvf):#vx,vy,vc=
		nx=len(vvf)
		ny=len(vvf[0])
		f_max=max(vvf[0])
		f_min=min(vvf[0])
		
		ix=0
		for x in range(nx):
			f_ma=max(vvf[ix])
			f_mi=min(vvf[ix])
			f_max=max(f_max,f_ma)
			f_min=min(f_min,f_mi)
			ix+=1
		bz=(f_max==f_min)
		vx=[]
		vy=[]
		vc=[]
		ix=0
		for x in range(nx):
			iy=0
			for y in range(ny):
				vx.append(x)
				vy.append(y)
				if bz:
					c=50
				else:
					f=vvf[ix][iy]
					#print(str(f)+", "+str(f_min)+", "+str(f_max))
					c=float(f-f_min)/(f_max-f_min)*100
				vc.append(c)
				iy+=1
			ix+=1
		return vx,vy,vc
	def vvz_argMin_argMax_get(self,vvz):#argMin,argMax=
		argMin=[0,0]
		argMax=[0,0]
		ix=0
		for vz in vvz:
			iy=0
			for z in vz:
				if vvz[argMin[0]][argMin[1]]>vvz[ix][iy]:
					argMin=[ix,iy]
				if vvz[argMax[0]][argMax[1]]<vvz[ix][iy]:
					argMax=[ix,iy]
				iy+=1
			ix+=1
		return argMin,argMax

def start_euller_beam(h, deg, anchors, save_plot=True):
	Wall=clWall(yMax=h, angleFromVerticalGrad=deg)

	return  round(abs(Wall.testBeam(anchors=anchors, drew_graph=save_plot)), 2) # max moment


def start_wall_test(width, height, anchors, bLoop, print_all):
	Wall=clWall(xMax=width, yMax=height)

	return round(abs(Wall.testWall(v_xy_anchor=anchors, bLoop=bLoop, print_all=print_all)),2)


# from equalDistance import createEqualDistance
# anchors = createEqualDistance(width=10, height=6, number_of_points_row=3, number_of_points_col=3)
# anchors_xy = []
# for anchor in anchors:
# 	anchors_xy.append([anchor["x"], anchor["y"]])

# print(anchors_xy)

# print(start_wall_test(width=10, height=6, anchors=anchors_xy, print_all=True))
