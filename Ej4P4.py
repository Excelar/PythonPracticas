def porcen(ad,ta):
	porcen=(ad*100)//ta
	return(porcen)
ta=0
ap=0
ad=0
print('Ingrese numero de legajo')
nleg=int(input())
while(nleg!=0):
	ta+=1
	print('Ingrese promedio del alumno')
	prom=float(input())
	if(prom>6.5):
		ap+=1
		if(prom>8.5)and(nleg<2000):
			ad+=1
	print('Ingrese numero de legajo')
	nleg=int(input())	
if(ta!=0):
	print('A.',ta)
	print('B.',ap)
	print('C.',porcen(ad,ta),'%')
