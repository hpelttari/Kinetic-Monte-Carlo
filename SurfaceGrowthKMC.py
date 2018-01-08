import numpy as np
from matplotlib import pyplot as plt
import random as rand
import lattice
import constants as con
import functions as func


simulationLength = 1
t=0
p_sum=100
rand.seed(None)
w=10**13
N=100
Es=0.75 #eV
En=0.18 #eV
F=0.0033 #ML/s

energies=np.array([Es,Es+En,Es+2*En,Es+3*En,Es+4*En])

lattice = np.ones((10,10),dtype=int)
i=0
for x in np.nditer(lattice,op_flags=['readwrite']):
    x[...]=rand.randrange(4)
    i+=1
'''
print(lattice)
print("energies:")
print(energies)
'''
energyBarriers=func.energyBarriers(lattice,energies)
print("hopping rates:")
print(energyBarriers)


'''
i=0
#KMC algorithm
while(i<=N):
    u=rand.random()
    dt=-np.log(u)/p_sum
    print(t)
    t=t+dt
    i=i+1
'''
i=0

'''
while(i<=N):
    E =func.energyBarriers(lattice,energies)
''' 

