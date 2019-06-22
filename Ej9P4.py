import math
def radio(r):
	dia=2*r
	per=math.pi*(r**2)
	rad=dict(diametro=dia,perimetro=per)
	return(rad)
print('ingrese radio')
r=float(input())
rad=radio(r)
print(rad)
