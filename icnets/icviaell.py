import scipy as sp
import numpy as np
import scipy.special as ssp
import numpy.linalg as la

def ell(u,m):
	return ssp.ellipj(u,m)
def sn(u,m):
	return ell(u,m)[0]
def cn(u,m):
	return ell(u,m)[1]
def dn(u,m):
	return ell(u,m)[2]

def mkl(a,b,k,s,st):
	m=1-(b**2)/(a**2)
	n=[]
	d=[]
	for i in range(0,k):
		c=s+i*st
		n.append([cn(c,m),sn(c,m)])
		d.append(a*dn(c,m))

	return [n,d]

def mcfn(n,d):
    M=[[n[0,0],n[0,1],-1],[n[1,0],n[1,1],-1],[n[2,0],n[2,1],-1]]
    MM=np.array(M)
    print(MM)
    MI = la.inv(MM)
    print(d)
    r = np.matmul(MI,d)
    return [[r[0],r[1]], r[2]]

a = int(input("Alpha: "))
b = int(input("Beta: "))
k = int(input("K: "))
s = int(input("S1: "))

[nl,dl]=mkl(a,b,k,0,0.25)
[nm,dm]=mkl(a,b,k,s,0.25)
print(nl)
print(dl)
print(nm)
print(dm)
nn = np.array([nl[0],nl[1],nm[0]])
dd = np.array([[dl[0]],[dl[1]],[dm[0]]])
[m,r]=mcfn(nn,dd)
print(m)
print(r)


		
