#secant method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the eqn in x using python syntax: ")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

a, b = float(input('a: ')), float(input('b: '))

if f(a) == f(b):
    print("Divide by zero error")

else:
    e = float(input("Enter tolerable error: "))
    N = int(input("Enter maximum number of iterations: "))
    itr = 1
    A = []
    m = []

    while itr <= N:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        er = abs(c - b)
        A.append([itr, a, b, c, f(a), f(b), f(c), er])
        m.append(c)
        if er < e:
            A = pd.DataFrame(A, columns=["iterations", "a", "b", "c", "f(a)", "f(b)", "f(c)", "error"])
            print(A)
            print(f"The approximate root is {c} in {itr} iterations.")
            break
        a, b = b, c
        itr += 1

    if itr > N:
        print(f"The solution does not end in {N} iterations")

x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), label=eqn, color='red')  
plt.axhline(0, color='blue')
plt.axvline(0, color='green')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Secant Method')
plt.scatter(m, [f(val) for val in m])

for i, val in enumerate(m):
    plt.text(val, f(val), f'{i+1}')

plt.show()
