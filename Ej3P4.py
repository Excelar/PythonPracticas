def maximo(n):
	if((n['n1']>n['n2'])and(n['n1']>n['n3'])):
		if(n['n2']>n['n3']):
			return(n)
		else:
			va=n['n3']
			n['n3']=n['n2']
			n['n2']=va
			return(n)
	else:
		if((n['n2']>n['n1'])and(n['n2']>n['n3'])):
			va=n['n2']
			n['n2']=n['n1']
			n['n1']=va
			if(n['n2']>n['n3']):
				return(n)
			else:
				va=n['n3']
				n['n3']=n['n2']
				n['n2']=va
				return(n)
		else:
			if((n['n3']>n['n1'])and(n['n3']>n['n2'])):
				va=n['n3']
				n['n3']=n['n1']
				n['n1']=va
				if(n['n2']>n['n3']):
					return(n)
				else:
					va=n['n3']
					n['n3']=n['n2']
					n['n2']=va
					return(n)
def carga():
	print('ingrese el primer numero')
	n1=int(input())
	print('ingrese el primer numero')
	n2=int(input())
	print('ingrese el primer numero')
	n3=int(input())
	n=dict(n1=n1,n2=n2,n3=n3)
	return(n)

n=carga()
maximo(n)
print(n)
