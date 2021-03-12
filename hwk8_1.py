import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#phi(r)=Aexp(-Br)-(C/(r**6))

def buck_potential(r):
    A = 1
    B = 1
    C = 1
    phi = A * np.exp(-B*r) - (C/(r**6))
    return phi

rlist = np.linspace(1, 100, 100)
phi_list = []

for i in rlist:
    phi = buck_potential(r=i)
    phi_list.append(phi)

plt.plot(rlist, phi_list)
plt.xlabel('Angstroms')
plt.ylabel('eV')
plt.show()

maximum = optimize.fmin(lambda r: -buck_potential(r), 0)