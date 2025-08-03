# trapezoidal rule

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = float(input('Enter lower limit: '))
b = float(input('Enter upper limit: '))
n = int(input('Enter no of partitions: '))
x = np.linspace(a,b,n+1)

func = input('Enter integrand function using python syntax: ')

def F(x,func):
    return eval(func)

def y(x):
    return F(x,func)


h = (b-a)/n
s = 0
integral = 0

for i in range (1,n):
    s += y(x[i])
    
integral = (h/2) * (y(x[0]) + 2*s + y(x[n]))

print('The approx integral value by trapezoidal rule is')
print(integral)

plt.plot(x,[y(x) for x in x], color='red')
xval = np.linspace(a-10 , b+10 ,1000)
plt.plot (xval , [y(x) for x in xval ])
ypoints = [y(x) for x in x]
plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

for i in range(n):
    xs = [x[i],x[i+1],x[i+1],x[i]]
    ys = [0,0,ypoints[i+1],ypoints[i]]
    plt.fill(xs,ys, color='pink' , edgecolor = 'yellow' )

plt.title('Trapezoidal method')
plt.show()

    
    
