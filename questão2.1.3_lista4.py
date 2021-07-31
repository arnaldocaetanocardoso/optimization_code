import math


def quadratic_search(f, a, b, tol=1e-6):

    c = b
    b = (c-a)/2

    fa = f(a)
    fb = f(b)
    fc = f(c)

    while abs(c-a) < tol:
        x = 0.5*(fa*(b**2-c**2)+fb*(c**2-a**2)+fc*(a**2-b**2)) / \
            (fa*(b-c) + fb*(c-a) + fc*(a-b))
        fx = f(x)
        print(x)
        if x > b:
            if fx > fb:
                c = x
                fc = fx
            else:
                a = b
                fa = fb
                b = x
                fb = fx
        else:
            if fx > fb:
                a = x
                fa = fx
            else:
                c = b
                fc = fb
                b = x
                fb = fx

    return (a+c)/2
