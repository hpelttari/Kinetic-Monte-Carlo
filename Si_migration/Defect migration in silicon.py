# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 07:37:34 2017

@author: hannu
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.constants as const
from constants import *
import functions as func

'''
Kinetic Monte Carlo simulation of migration of defects in silicon caused by a boron beam.
'''

    
  


seed		= None	
random.seed(seed)



jumpRatei = wi*const.e**(Eim/(kb*T))
jumpRatev = wv*const.e**(Evm/(kb*T))
rates=[jumpRatei for i in range(300)]+[jumpRatev for i in range(300)]  #list of jumprates



#Create the cumulative funciton for KMC:
R=func.cum(rates)


vacanciesx=np.random.normal(0,sigma_i,300)
vacanciesy=np.random.normal(0,sigma_i,300)
interstitialsx=np.random.normal(0,sigma_v,300)
interstitialsy=np.random.normal(0,sigma_v,300)



distvac=func.distances(vacanciesx,vacanciesy,N)
distint=func.distances(interstitialsx,interstitialsy,N)   

#plot the vacancies and interstitials the boron beam before recombination
plt.figure(1)
plt.plot(vacanciesx,vacanciesy,"o",color="b")
plt.plot(interstitialsx,interstitialsy,"o",color="r")
plt.title("Initial defect positions before recombination")
plt.xlabel("x")
plt.ylabel("y")


###                recombination at the beginning:
defects=600
distvac=func.distances(vacanciesx,vacanciesy,N)
distint=func.distances(interstitialsx,interstitialsy,N)
for i in range(N):
    for j in range(N):
        if(abs((distvac[i]-distint[j]))<=recomb):
            vacanciesx[i]=np.NaN
            vacanciesy[i]=np.NaN
            rates[i]=0
            defects=defects-2
            interstitialsx[j]=np.NaN
            interstitialsy[j]=np.NaN
            rates[j+299]=0
            distvac[i]=np.sqrt((vacanciesx[i]**2+vacanciesy[i]**2))
            distint[j]=np.sqrt((interstitialsx[j]**2+interstitialsy[j]**2))

#plot the vacancies and interstitials after recombination
plt.figure(2)
plt.plot(vacanciesx,vacanciesy,"o",color="b")
plt.plot(interstitialsx,interstitialsy,"o",color="r")
plt.title("Initial defect positions after recombination")
plt.xlabel("x")
plt.ylabel("y")


vx=0
vy=0
ix=0
iy=0
for i in range(N):
    if(np.isnan(vacanciesx[i])):
        vx=vx+1
    if(np.isnan(vacanciesy[i])):
        vy=vy+1
    if(np.isnan(interstitialsx[i])):
        ix=ix+1
    if(np.isnan(interstitialsy[i])):
        iy=iy+1
   
print("NaN LKM:",vx,vy,ix,iy) 

################# KMC begins #################
t=0
R=0
q=0
k=1
while(k<2000):
    #Cumulative function
    R=[0 for i in range(600)]
    for i in range(600):
        if(i<300):
            if(interstitialsx[i]==0):
                R[i]=0
            else:
                R[i]=sum(R)+rates[i]
        if(i>299):
            if(vacanciesx[i-300]==0):
                R[i]=0
            else:
                R[i]=sum(R)+rates[i]    
    u1=random.uniform(0,1)
    j=0
    #pick an event to carry out:
    for i in range(len(rates)):
        if(i>0 and i<599 and R[i-1]<u1*sum(R)<=R[i+1]):
            j=i
        if(i==0 and u1*sum(R)<=R[i+1]):
            j=i
        if (i==599 and R[i-1]<u1*sum(R)):
            j=i
    
    u2 = random.uniform(-1,1)
    u3 = random.uniform(-1,1)
    #carry out the event:
    if(j<300):
        interstitialsx[j]=interstitialsx[j]+u2*dist
        interstitialsy[j]=interstitialsy[j]+u3*dist
    if(j>299):
        j=j-300
        vacanciesx[j]=vacanciesx[j]+u3*dist
        vacanciesy[j]=vacanciesy[j]+u3*dist
                  
    distvac=func.distances(vacanciesx,vacanciesy,N)
    distint=func.distances(interstitialsx,interstitialsy,N)
    for i in range(N):
        for j in range(N):
            if(abs((distvac[i]-distint[j]))<=recomb):

                vacanciesx[i]=np.NaN
                vacanciesy[i]=np.NaN
                rates[i]=0
                defects=defects-2
                interstitialsx[j]=np.NaN
                interstitialsy[j]=np.NaN
                rates[j+299]=0
                distvac[i]=np.sqrt((vacanciesx[i]**2+vacanciesy[i]**2))
                distint[j]=np.sqrt((interstitialsx[j]**2+interstitialsy[j]**2))
    u=random.uniform(0,1)
    #calculate the time step:
    dt=-np.log(u)/sum(R)
    q=q+1
    if(q%50==0):
        print(t,k)
    t=t+dt
    if(k==2):
        print('t= '+str(t))
    k=k+1




vx=0
vy=0
ix=0
iy=0
for i in range(N):
    if(np.isnan(vacanciesx[i])):
        vx=vx+1
    if(np.isnan(vacanciesy[i])):
        vy=vy+1
    if(np.isnan(interstitialsx[i])):
        ix=ix+1
    if(np.isnan(interstitialsy[i])):
        iy=iy+1
   
print("NaN LKM:",vx,vy,ix,iy) 

plt.figure(3)
plt.plot(vacanciesx,vacanciesy,"o",color="b")
plt.plot(interstitialsx,interstitialsy,"o",color="r")
plt.title("Defect positions after KMC run")
plt.xlabel("x")
plt.ylabel("y")





