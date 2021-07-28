import math
import matplotlib.pyplot as plt
import numpy as np


def f(x): return 2 + math.cos(x) + math.cos(2*x - 1/2)/2


# vetor com valores de 1 até 6 incrementando de 0.001
xs = [x for x in np.arange(1, 6, 0.001)]
fxs = [f(x) for x in xs]  # será minha função com o vetor.
plt.plot(xs, fxs)


def golden(f, a, b, tol):

    test = 10
    gr = (1 + math.sqrt(5))/2

    c = b - (b-a)/gr
    d = a + (b-a)/gr
    fc = f(c)
    fd = f(d)
    cont = 0

    while abs(b-a) > tol:
        if fc > fd:
            a = c
            fa = fc
        else:
            b = d
            fb = fd

        c = b - (b-a)/gr
        d = a + (b-a)/gr
        fc = f(c)
        fd = f(d)

    return (b+a)/2


def f(x): return 2 + math.cos(x) + math.cos(2*x - 1/2)/2


x_s = golden(f, 3, 6.0, 0.00001)

print(x_s)
