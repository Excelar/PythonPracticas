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
def cargarprod():
	nom=input()
	mar=input()
	cod=int(input())
	pre=float(input())
	sto=int(input())
	p=dict(n=nom,m=mar,c=cod,p=pre,s=sto)
	return(p)
def procesocod(c):
	dig=c%10
	ct5=0
	cumple=True
	while(c>0):
		if(dig==5):
			ct5+1
		c=c//10
	if(ct5==2):
		return(cumple)
	else:
		return(not(cumple))
p=cargaprod()
mayor40=0
while(p['c']!=-1):
	cmarca=0
	mar=p['m']
	while(mar==p['m']):
		cmarca+1 #a
		if(procesocod(p['c']): #c
			print('c)',p['c'])
		if(p['p']>40): #d
			mayor40+1
		if(p['s']==0): #b
			print('b)',p['n'])
		p=cargaprod()
	print('a)',cmarca) #a
print('d)',mayor40)
