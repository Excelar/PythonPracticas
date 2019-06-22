import math
def radio(r):
	dia=2*r
	per=math.pi*(r**2)
	rad=dict(diametro=dia,perimetro=per)
	return(rad)
cp=0
tierra=12700
marte=6780
jupiter=439264
print('ingrese radio')
r=float(input())
while(r!=0):
	print('ingrese nombre')
	nom=input()
	print('ingrese distancia')
	dis=float(input())
	rad=radio(r)
	if(rad['diametro']<=tierra)and(rad['diametro']>=marte):
		print(nom,dis)
	if(rad['perimetro']>jupiter):
		cp+=1
	print('ingrese radio')
	r=float(input())
print('cantidad de planetas con un perimetro mayor a Jupiter:',cp)
