from FileInput import inp
from JADE import JADE
from Function import F
import numpy as np


[h, R, I] = inp("2022_06_14_MM_.txt")

a = input().split()
nbva_1 = float(a[0])
a_2 = float(a[1])

b = input().split()
b_1 = float(b[0])
b_2 = float(b[1])

c = input().split()
c_1 = float(c[0])
c_2 = float(c[1])

print(R, I, h)
print(a_1, a_2, b_1, b_2, c_1, c_2)


def F_(x):
    return F(a_1, b_1, c_1, a_2, b_2, c_2, R, h, x[0], x[1], x[2])


A = np.max([R, h])
#def f(x):
#    return (1-(x[0]-3)**2)

print(JADE(F_, 20, 3, 1000, -A, A, max = True))
