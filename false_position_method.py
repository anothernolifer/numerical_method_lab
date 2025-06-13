#false position method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


eqn = input("Enter the equation in x using python syntax: ")


def f(x):
    return eval(eqn)


a, b = float(input('a: ')), float(input('b: '))


if f(a) * f(b) >= 0:
    print("False Position method fails: f(a) and f(b) must have opposite signs.")
else:
    e = float(input("Enter tolerable error: "))
    N = int(input("Enter maximum number of iterations: "))
    itr = 1
    A = []
    m = []

    while itr <= N:
        # False Position formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        er = abs(f(c))  # Optional: abs(c - previous_c)
        A.append([itr, a, b, c, f(a), f(b), f(c), er])
        m.append(c)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if er < e:
            A = pd.DataFrame(A, columns=["iterations", "a", "b", "c", "f(a)", "f(b)", "f(c)", "error"])
            print(A)
            print(f"The approximate root is {c} in {itr} iterations.")
            break

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
plt.title('False Position Method')
plt.scatter(m, [f(val) for val in m])

for i, val in enumerate(m):
    plt.text(val, f(val), f'{i+1}')

plt.show()
