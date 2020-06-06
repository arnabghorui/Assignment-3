import numpy as np
import matplotlib.pyplot as plt


file=open("problem4.txt","r")           #Read the data obtained from Q2.c
Data=file.readlines()
i=0
N = 64
K=np.zeros(N) 
fK=np.zeros(N)
for D in Data:
    D1,D2=D.split()
    K[i]=float(D1)
    fK[i]=float(D2)
    i=i+1

plt.plot(K,fK,'b')
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}(k)$',fontsize=16)

plt.grid(True)
plt.show()
