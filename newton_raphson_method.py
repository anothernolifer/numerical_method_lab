#newton raphson method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def F(x, eqn):
    return eval(eqn)  
def f(x, eqn):
    return F(x, eqn)  

def g(f, x, eqn, h=1e-10):
    
    return (f(x+h, eqn) - f(x, eqn)) / h


eqn = input("Enter the equation in x using Python syntax : \n")

a = float(input('Initial guess (a): '))
e = float(input("Enter tolerable error: "))
N = int(input("Enter maximum number of iterations: "))

itr = 1
A = []
m = []


while itr <= N:
    
    derivative = g(f, a, eqn)
    
    
    if abs(derivative) < 1e-10:
        print("Derivative is too close to zero. The method fails.")
        break

   
    b = a - (f(a, eqn) / derivative) 
    
    er = abs(b - a) 
    A.append([itr, a, b, f(a, eqn), f(b, eqn), er])
    m.append(b)
    
    
    if er < e:
        A = pd.DataFrame(A, columns=["iterations", "a", "b", "f(a)", "f(b)", "error"])
        print(A)
        print(f"The approximate root is {b} in {itr} iterations.")
        break
    
    
    a = b
    itr += 1


if itr > N:
        print(f"Solution does not reach in {N} iterations")

x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x, eqn), label=eqn, color='red') 
plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Newton Raphson Method')
plt.scatter(m, [f(val, eqn) for val in m])

for i, val in enumerate(m):
    plt.text(val, f(val, eqn), f'{i+1}')

plt.show()
