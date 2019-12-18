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
		sgn=1
		if(i%2==1):
			sgn=-1
		n.append([sgn*cn(c,m),sgn*sn(c,m)])
		d.append(sgn*a*dn(c,m))

	return [n,d]

def mcfn(n,d):
    M=[[n[0,0],n[0,1],-1],[n[1,0],n[1,1],-1],[n[2,0],n[2,1],-1]]
    MM=np.array(M)
    MI = la.inv(MM)
    r = np.matmul(MI,d)
    return [r[0:2], r[2]]

a = int(input("Alpha: "))
b = int(input("Beta: "))
k = int(input("K: "))
s = float(input("S1: "))

[nl,dl]=mkl(a,b,k,0,0.25)
[nm,dm]=mkl(a,b,k,s,0.25)

nnl = np.array(nl)
ddl = np.array(dl)
nnm = np.array(nm)
nnm = nnm*-1
ddm = np.array(dm)
ddm = ddm*-1
lstr=""
mstr=""
for i in range(0,k):
	lstr=lstr+"l"+str(i)+": "+str(nnl[i,0])+"*x + "+str(nnl[i,1])+"*y = "+str(ddl[i])+"\n"
	mstr = mstr + "m" + str(i) + ": " + str(nnm[i, 0]) + "*x + " + str(nnm[i, 1]) + "*y = " + str(ddm[i])+ "\n"
nn = np.array([nl[0],nl[1],nnm[0]])
dd = np.array([[dl[0]],[dl[1]],[ddm[0]]])
cstr=""
for i in range(0,k-1):
	for j in range(0,k-1):
		if (i+j)%2==1: continue
		nn = np.array([nl[i], nl[i+1], nnm[j]])
		dd = np.array([[dl[i]], [dl[i+1]], [ddm[j]]])
		[m,r]=mcfn(nn,dd)
		cstr = cstr + "c"+str(i)+str(j)+": (x-" + str(m[0, 0]) + ")^2 + (y- " + str(m[1, 0]) + ")^2 = (" + str(r[0]) + ")^2"+"\n"
op=lstr+mstr+cstr
print(op)


		
