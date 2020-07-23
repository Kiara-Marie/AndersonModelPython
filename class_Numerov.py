# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:18:38 2019

@author: Ruoxi
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter 


class Numerov:
    
    def __init__(self, spec='NO'):
        self.spec=spec

    def E(self,n,l): #This is for NO
        Ry=0.5 #in a.u
                
        if self.spec !='NO':
            delt=0        
        elif l==0:
            delt=1.2
        elif l==1:
            delt=0.7
        elif l==2:
            delt=-0.05
        elif l==3:
            delt=0.01
        elif l==4:
            delt=0.003
        else:
            delt=0     
        return -Ry/(n-delt)**2
            
            
    def V(self, r, Z=1, alpha_1=1, alpha_d=0, rc=1):
        """ Computes the potential.
        r = distance from e to core,
        Z = net charge of the core,
        alpha_1 = special coefficients related to decay of potential field specific to NO
        alpha_d = core dipole polarizability 
        rc = effective core size
        """ 

         # Coulomb potential
         Vc=-(1+(Z-1)*np.exp(-alpha_1*r))/r

         # Core polarization potential 
         Vp=-alpha_d/2/r**4*(1-np.exp(-(r/rc)**6))
         
         return Vc+Vp
    
    
    def g(self, n,l,r):
    #    return 2*np.exp(2*x)*(V(x)-E(n,l))+(l+0.5)**2
         return (2*l+1/2)*(2*l+3/2)/r+8*r*(self.V(r)-self.E(n,l)) 
    
    
    def X(self, n,l, h=0.1):
        
        r_max=2*n*(n+15)
        r_min=n**2-n*(n**2-(l-1)**2)**0.5
        #r_min=0.05
        
        x_max=r_max**0.5
        x_min=r_min**0.5
        
        x=np.arange(x_max,x_min,-h) # array has to start from max
        N=len(x)
        r=x**2
        
        eps=1e-6    
        
        G=self.g(n,l,r) #here must use unscaled r 
           
        y=np.zeros(N)
        y[0]=0
        y[1]=eps
        
        for j in range(2,N):
            y[j]=((2+5*h**2/6*G[j-1])*y[j-1]-(1-h**2/12*G[j-2])*y[j-2])/(1-h**2/12*G[j])
    #        if np.isnan(y[j]):
    #            y[j]=0    
        y=y*(2*h*np.sum(y**2*r))**-0.5 #normalization
        
        return [r, y, h]   
    
    def Wavefun(self,n,l):
        
         XX=self.X(n,l)
         plt.plot(XX[0],(XX[0]**0.25*XX[1])**2)
    
    def Rad_int(self, n1,l1,n2,l2,p=1):
        h=self.X(n1,l1)[2]
        r_i=min(max(self.X(n1,l1)[0]),max(self.X(n2,l2)[0])) #outer end
        r_f=max(min(self.X(n1,l1)[0]),min(self.X(n2,l2)[0])) #innner end
        
        x_i=r_i**0.5
        x_f=r_f**0.5
        
        x=np.arange(x_f,x_i,h)
        r=x**2
    #    print(r)
    #    print(x)  
        
        r1=self.X(n1,l1)[0]
        y1=self.X(n1,l1)[1]
        
        r2=self.X(n2,l2)[0]
        y2=self.X(n2,l2)[1]
        
        f1=inter.interp1d(r1,y1) 
        f2=inter.interp1d(r2,y2)
        
        X1=f1(r)
        X2=f2(r)
        
    #    plt.plot(r,r**0.25*X1)
    #    plt.plot(r,r**0.25*X2)
            
        
        result=2*h*np.sum(X1*X2*r**(p+1))
    
        return result
    
def get_rad(state1,state2,p=1):
    return Numerov().Rad_int(state1.n,state1.l, state2.n,state2.l,p)
    
    
    
    
class State:
    
    def __init__(self, n,l,rot,m,spec='NO'):
        self.n=n
        self.l=l
        self.rot=rot
        self.spec=spec
        self.m=m
        
    def getE(self): #This is for NO
        Ry=109735 #in cm^-1
        B0=1.98781
        
        n=self.n
        l=self.l    
        rot=self.rot
        
        
        if self.spec !='NO':
            delt=0        
        elif l==0:
            delt=1.2
        elif l==1:
            delt=0.7
        elif l==2:
            delt=-0.05
        elif l==3:
            delt=0.01
        elif l==4:
            delt=0.003
        else:
            delt=0     
        return -Ry/(n-delt)**2+B0*rot*(rot+1)       
    
   
    


    
           

    
    
    



 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
