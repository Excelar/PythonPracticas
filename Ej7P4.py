def procesar(n,cd):
	sm=0
	while(n!=0):
		dig=n%10
		sm+=dig
		cd+=1
		n=n//10
	np=dict(cantidad_digitos=cd,suma_digitos=sm)
	return(np)
cd=0
repeat
	print('ingrese los numeros')
	n=int(input())
	num=procesar(n,cd)
	until(num['sumar_digitos']!=10)
print('Cantidad de digitos leídos',num['cantidad_digitos']
