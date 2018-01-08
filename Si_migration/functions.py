# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:56:32 2017

@author: hannu
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.constants as const
from constants import *

####### Functions for KMC ######

def f(sigma, x):
    normal = (1/(2*const.pi*sigma**2))*np.exp(-(x**2)/(2*sigma**2))
    return normal

#function to calculate the recombinations
def recombination(vacx,vacy,intx,inty,N,rates,defs):
    distvac=distances(vacx,vacy,N)
    distint=distances(intx,inty,N)
    for i in range(N):
        for j in range(N):
            #distvac=distances(vacx,vacy,N)
            #distint=distances(intx,inty,N)
            if(abs((distvac[i]-distint[j]))<=recomb):

                vacx[i]=np.NaN
                vacy[i]=np.NaN
                rates[i]=0
                defs=defs-2
                intx[j]=np.NaN
                inty[j]=np.NaN
                rates[j+299]=0
                distvac[i]=np.sqrt((vacx[i]**2+vacy[i]**2))
                distint[j]=np.sqrt((intx[j]**2+inty[j]**2))
    return(defs,vacx,vacy,intx,inty)

    

#calculates the distance from the origin
def distances(x,y,N):
    distances = np.linspace(-70*10**-10,70*10**-10, num=N)
    for i in range(N):
        distances[i]=np.sqrt(x[i]**2+y[i]**2)
    return distances

def cum(rates):
    R=[0 for i in range(600)]
    for i in range(600):
        R[i]=sum(R)+rates[i]
    return(R)