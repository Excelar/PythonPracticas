"""
Un supermercado requiere el procesamiento de los productos que dispone. 
De cada producto se conoce su cod, nom, marca, stock y precio unitario. 
El procesamiento finaliza con el codigo -1, los prductos de igual marca se leen consecutivamente 

Informar
a)cantidad en stock de productos de cada marca 
b)los nombres de los productos con stock en 0
c)los codigos de los productos que tienen exactamente 2 digitos iguales a 5
d)la cantidad de productos cuyo precio es mayor a 40 
"""
"""
leer cod
mientras (cod<>-1)
	prodmark=0
	leer marca
	mmarca=True
	mientras (mmarca)^(codigo<>-1)
		a)prodmark+=1
		p=cargaprod(cod,mar)
		d)si(p[precio]>40)
			mayor40+=1
		b)si(p[stock]==0)
			imprimir(p[nombre]
		c)si(procesarcinco(cod))
			imprimir(p[cod])
		leer marca
		si(marca<>p[marca])
			mmarca=false
		leer cod
	si cod<>-1
		leer cod
imprimir(mayor40)	
"""
def cargaprod(c,m):
	n=input()
	s=int(input())
	p=float(input())
	pr=dict(cod=c,mar=m,nom=n,sto=s,pre=p)
	return(pr)
def procesocod(c):
	ct5=0
	cumple=True
	while(c>0)
		dig=c%10
		if(dig==5):
			ct5+1
		c=c//10
	if(ct5!=2):
		return(not(cumple))
	else:
		return(cumple)
mayor40=0
print('ingrese el codigo')
cod=int(input())
while(cod!=0):
	prodmark=0
	mar=input()
	mmarca=True
	while(mmarca):
		prodmark+=1
		p=cargaprod(cod,mar)
		if(p['pre']>40):
			mayor40+=1
		if(p['sto']==0):
			print('B)Nombre del producto cuyo stock es 0:',p['nom'])
		if(procesocod(cod):
			print('C)Este codigo',p['cod'],'contiene 2 veces el codigo 5')
		mar=input()
		if(mar!=p['mar']):
			mmarca=False
		cod=int(input())
	print('A)cantidad de productos de la marca',p['mar'],':',prodmark)
print('D)cantidad de productos con precios mayores a $40:',mayor40)	
