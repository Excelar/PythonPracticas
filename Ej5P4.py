def prod():
	print('Ingrese precio')
	pre=float(input())
	print('Ingrese codigo')
	cod=input()
	print('Ingrese tipo')
	tipo=input()
	p=dict(pr=pre,co=cod,ti=tipo)
	return(p)
def imprimir(cc,cb):
	print('El codigo del producto pantalon mas caro es:',cc)
	print('El codigo del producto mas barato es:',cb)
	return()
maximo=-100
minimo=100000
codbar=''
codcar=''
for i in range(100):
	p=prod()
	if(p['pr']>maximo)and(p['ti']=='pantalon'):
		maximo=p['pr']
		codcar=p['co']
	if(p['pr']<minimo):
		codbar=p['co']
		minimo=p['pr']
imprimir(codcar,codbar)
