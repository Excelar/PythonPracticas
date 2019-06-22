def absoluto(x):
	x=x**2**(1/2)
	return(x)
print('ingrese nro a evaluar')
x=float(input())
a=absoluto(x)
if(x>=0):
	print('|',x,'|=',a,'cuando',x,'es mayor o igual a cero')
else:
	print('|',(-1)*x,'|=',a,'cuando',(-1)*x,'es menor a cero')
