import numpy as np
import math
def ejercicio2(a,vectorX):
    temp = np.power(a, np.arange(8))
    temp = temp[::-1]
    return np.dot(temp,vectorX)
def funcion(x):
    return (1/(1+(25*(x**2))))
def error(x, vectorX):
    if(math.isclose(funcion(x),ejercicio2(x,vectorX))):
        return 0
    else:
        return abs(funcion(x)-ejercicio2(x,vectorX))
def ejercicio6(a,vectorXej6):
    temp = np.power(a, np.arange(16))
    temp = temp[::-1]
    return np.dot(temp,vectorXej6)
def errorej6(x,vectorXej6):
    if(math.isclose(funcion(x),ejercicio6(x,vectorXej6))):
        return 0
    else:
        return abs(funcion(x)-ejercicio6(x,vectorXej6))