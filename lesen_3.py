# Copyright (c) 2021 FaniPi
import math


def enthalpie(temp, feucht):
    feu = feucht / 100
    a = 0.622
    k = (17.62 * temp) / (243.12 + temp)
    j = math.exp(k)
    m = j * 6.112
    n = m * 100
    b = round(n)
    c = 100000
    d = feu * b
    f = c - d
    g = d / f
    h = a * g
    i = 1.005 * temp + h * (2500 + 1.86 + temp)
    j = round(i, 2)
    print(j)
    #return j


if __name__ != '__main__':
    pass
else:
    enthalpie(23, 55)
