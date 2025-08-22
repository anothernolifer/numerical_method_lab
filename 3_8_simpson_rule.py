# to evaluate integral using simpson 3/8 rule
# a = 0 b=6  func = 1/(1+x**2)

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a = float(input('enter the lower limit (a): '))
b = float(input('enter the upper limit (b): '))
n = int(input('enter the no. of partition : '))

if n%3 !=0:
    print('No of partition must be multiple of 3')
    exit()
    
else:
    ode = input('enter the integrand function in x using python syntax:')
    def F(x,ode):
        return eval(ode)
    def y(x):
        return F(x,ode)
    
    h = (b-a)/n
    
    x = np.linspace(a,b,n+1)
    ypoints = [y(x) for x in x]
    
    I = 0
    S1 = 0
    S2 = 0
    
    for i in range (1,n):
        if i%3!=0:
            S1+=y(x[i])
        else:
            S2+=y(x[i])
            
    I = ((3*h)/8) * (y(x[0]) + 3*S1 + 2*S2 + y(x[n]))

    print('The integral by simpsons 3/8 rule is :')
    print(I)    

plt.plot(x,ypoints,label = 'Partition points',marker = 'x')
xval = np.linspace(a-10 , b+10 ,1000)
plt.plot (xval , [y(x) for x in xval ],label = 'Integrand function')

plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

for i in range(0,n,2):
    x_list = x[i:i+3]
    y_list = ypoints[i:i+3]
   
plt.fill_between(x_list,y_list, color='pink' , alpha = 0.2 , label = 'Area by Simpson 3/8 rule' )

plt.title('Simpson 3/8 rule')
plt.legend()
plt.show()
     
