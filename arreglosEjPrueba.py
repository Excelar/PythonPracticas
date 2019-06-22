"""
Un super dispone de la información de sus 100 productos y desea informar los nombres de los productos cuyo precio supera el promedio
La info que se conoce de cada producto es: nombre, marca, stock y precio
"""
cprod=100		#inicializacion de var y contadores
total=0
def leer_prod(): #CARGA MODULAR CORRECTA DE REGISTROS(DICCIONARIOS)
	nom=input()
	mar=input()
	stock=int(input())
	precio=float(input())
	prod= dict(nom=nom,mar=mar,stock=stock, precio=precio)
return(prod)
arregloprod=[] #creación de 
for i in range(cprod): #carga y acumulacion
	p=leer_prod()
	total=total+p['precio']
	arregloprod[i].append(p)
prom=total/cprod #sacar promedio
for i in range(cprod): #imprimir precios > prom
	if(arregloprod[i]['precio']>prom):
		print(arregloprod[i]['precio'])
