import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.e**x

def g(x):
    return -x*x +4

def altura(x):
    return math.fabs(f(x) - g(x))

#calcula el area entre las dos curva de a a b con un delta de x = h
def area(a , b , h):
    float(a)
    float(b)
    float(h)
    acum = 0
    i = a
    while i <= b:
        acum  = acum + (altura(i) * h)
        i = i+h

    return acum


def plotear(ini , fin ):
    x = np.arange(ini,fin, 0.01)
    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append(f(x[i]))
        y2.append(g(x[i]))

    fig, ax = plt.subplots()
    ax.plot(x, y1, x, y2, color='black')
    ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
    ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='green', interpolate=True)
    ax.set_title('area entre las dos funciones')

    plt.show()



def main():
    ini = float(input("Valor inicial: "))
    fin = float(input("Valor final: "))
    print(area(ini, fin, 0.00001))
    plotear(ini , fin)

main()
