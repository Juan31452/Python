from math import pi
r = 0
h = 0
a = 0
v = 0
r = int(input("Valor radio :"))
h = int(input("Valor altura :"))
a = (2*(pi*r**2)+(2*pi*r)*h)
v = (pi*r**2)*h
print("Area : ",a)
print("Volumen : ",v)