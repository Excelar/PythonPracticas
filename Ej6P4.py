def procesar(n):
	cd=0
	sm=0
	while(n!=0):
		dig=n%10
		sm+=dig
		cd+=1
		n=n//10
	np=dict(cantidad_digitos=cd,suma_digitos=sm)
	return(np)
print('ingrese los numeros')
n=int(input())
print(procesar(n))
	
