import scipy as sp
import numpy as np
import scipy.special as ssp

def ell(u,m):
	return ssp.ellipj(u,m)
def sn(u,m):
	return ell(u,m)[0]
def cn(u,m):
	return ell(u,m)[1]
def dn(u,m):
	return ell(u,m)[2]

def mkl(a,b,k,s,st):
	m=1-(a**2)/(b**2)
	n=[]
	d=[]
	for i in range(0,k):
		c=s+i*st
		n.append([cn(c,m),sn(c,m)])
		d.append(a*dn(c,m))

	return [n,d]

mcfn(n,d)
M=[[,-1],[,-1],[,-1]]
MM=np.array(M)


a = int(input("Alpha: "))
b = int(input("Beta: "))
k = int(input("K: "))
s = int(input("S1: "))

[nl,dl]=mkl(a,b,k,0,0.2)
[nm,dm]=mkl(a,b,k,s,0.2)
print(nl)
print(dl)
print(nm)
print(dm)

		
