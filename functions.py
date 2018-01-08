import numpy as np


def energyBarriers(lattice,energies):
    x=0 #x-component of the lattice
    y=0 #y-component of the lattice
    barriers=np.zeros(lattice.shape)
    while(x<lattice.shape[1]):
        n=0
        y=0
        while(y<lattice.shape[0]):
            n=0
            if(lattice[y-1,x]==lattice[y,x]):
                n+=1
            if(lattice[y,x-1]==lattice[y,x]):
                n+=1
            if(y<lattice.shape[0]-1):
                if(lattice[y+1,x]==lattice[y,x]):
                    n+=1
            if(y>lattice.shape[0]-1):
                if(lattice[0,x]==lattice[y,x]):
                    n+=1
            if(x<lattice.shape[1]-1):
                if(lattice[y,x+1]==lattice[y,x]):
                    n+=1
            if(x>lattice.shape[1]-1):
                if(lattice[y,0]==lattice[y,x]):
                    n+=1
            
            #if(y<lattice.shape[0]-2 and lattice[y+1,x]==lattice[y,x]):
             #   n+=1
            #if(x<lattice.shape[1]-2 and lattice[y,x+1]==lattice[y,x]):
             #   n+=1
            barriers[y,x]=energies[n]
                
            y+=1
        x+=1
    return barriers

#unfinished rate function using iterator
'''
def hoppingRates(lattice,energies):
    for x in np.nditer(lattice):
'''
