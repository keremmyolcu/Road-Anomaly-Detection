import math

def distanceFromLeft(x, y):
    nom = abs(x*4+y*1 -1000)
    denom = math.sqrt(17)
    return nom/denom

def distanceFromMiddle(a, b):
    return abs(a-320)

def distanceFromRight(a, b):
    x = abs(b*1+a*(-4)+1560)
    y = math.sqrt(17)
    return x/y

