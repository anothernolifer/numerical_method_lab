# to fit the second degree curve y = a+bx+cx^2
# 1 2 3 4 5 # 1090 1225 1390 1625 1915

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X = np.array(list(map(float,input('Enter x-data:').split())))
Y = np.array(list(map(float,input('Enter y-data:').split())))

n = len(X)

A = [[n,np.sum(X),np.sum(X**2)],
     [ np.sum(X),np.sum(X**2),np.sum(X**3)],
     [ np.sum(X**2),np.sum(X**3),np.sum(X**4) ]]

B = [[np.sum(Y)],
     [np.sum(X*Y)],
     [np.sum((X**2)*Y)]]

print('\n Coefficients matrix:')
print(A)

print('\n Constants:')
print(B)

inv_A = np.linalg.inv(A)

coeff = np.dot(inv_A,B)
a, b, c = coeff.flatten()
print(f'\nCoefficients:\na = {a}\nb = {b}\nc = {c}')


x = np.linspace(min(X)-5 , max(X)+5 ,1000)
plt.plot(x,a+b*x+c*x**2, color='red')
plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('Least square method')

plt.scatter(X, Y, color='blue', marker='x', label='Data points')
plt.legend()


plt.show()




