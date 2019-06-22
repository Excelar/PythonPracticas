def procesar(n):
	p=0
	i=0
	while(n!=0):
		dig=n%10
		if(dig%2==0):
			p+=1
		else:
			i+=1
		n=n//10
	np=dict(imp=i,par=p)
	return(np)
def imprimir(np):
	print('Cantidad de numeros pares:',np['par'])
	print('Cantidad de numeros impares:',np['imp'])
	return()
print('ingrese numero a procesar')
n=int(input())
while(n!=123456):
	np=procesar(n)
	imprimir(np)
	print('ingrese numero a procesar')
	n=int(input())
