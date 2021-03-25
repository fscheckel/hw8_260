import numpy as np
import matplotlib.pyplot as plt
Import scipy.optimize import minimize

#f(x,y)=5exp[-(x-1)**2 - 2*(y-3)**2] + 3exp[-2*(x-4)**2 - (y-1)**2]
#maxima (1,3) 5
#maxima (4,1) 3

def funky(x, y):
    a = 5*np.exp(-(x-1)**2 - 2*(y-3)**2)
    b = 3*np.exp(-2*(x-4)**2 - (y-1)**2)
    c = a + b
    return c
xs = ys = np.arange(0, 5, h)
x, y = np.meshgrid(xs, ys)
h = 0.01

if __name__ == "__main__":
    xs = ys = np.arange(0, 5, h)
    x, y = np.meshgrid(xs, ys)
    h = 0.01
    z = funky(x, y)

plt.contour(z)
plt.ylabel('y')
plt.xlabel('x')
plt.show

#Gf=(pf/px),(pf/py)

#VX=[x,y]=>VX-gGf