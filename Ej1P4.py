def maximo(n1,n2):
	if(n1==n2):
		return('Son Iguales')
	else:
		if(n1>n2):
			return(n1,'Es el mayor')
		else:
			return(n2,'Es el mayor')
print('nro1')
n1=int(input())
print('nro2')
n2=int(input())
print(maximo(n1,n2))
