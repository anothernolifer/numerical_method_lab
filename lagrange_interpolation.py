# to find lagrange interpolation polynomial 
# 1 2 3 4 5 # 1 4 9 16 25 # 3.25

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X = np.array(list(map(float,input('Enter x-data:').split())))
Y = np.array(list(map(float,input('Enter y-data:').split())))
X_p = float(input('Enter value to interpolate:'))

n = len(X)
x = sp.symbols('x')
poly = 0

for i in range(n):
    lbp = 1
    
    for j in range(n):
        if j != i:
            lbp *= (x-X[j])/(X[i]-X[j])
            
    poly += Y[i] * lbp
    
poly = sp.simplify(poly)

print('The lagrange inter polynomial is : \n',poly)

int_val = poly.subs(x,X_p)
print(f'The interpolated value at x = {X_p} is {int_val}')

poly1 = sp.lambdify(x,poly,'numpy')
xval = np.linspace(min(X)-5 , max(X)+5 ,1000)
plt.plot(xval,poly1(xval),color='red')
plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('Lagrange polynomial')
plt.scatter(X_p, float(int_val), color='green', label=f'Interpolated point at x={X_p}')
plt.scatter(X, Y, color='blue', marker='x', label='Data points')
plt.legend()


plt.show()
    
