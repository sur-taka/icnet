import numpy as np
import scipy.special as sl
import scipy as sp
import numpy.linalg as la
import math

def getnormal(a,f,t):
    e = sl.ellipj(t,(1/f)**2)
    s=e[0]
    d=e[2]
    y=a/f*d
    x=a/f*s
    z=math.sqrt(x**2+y**2-1)
    return [x,y,z]

def normaltocirc(n):
    m=[n[0]/n[2],n[1]/n[2]]
    r=1/n[2]
    return [m,r]

def circtogg(m,r):
    op="(x-"+str(m[0]) +")^2 + (y - "+str(m[1]) + ")^2 =("+str(r)+")^2"
    return op

def printnet(a,f,k,start,stop,step):
    op=""
    for i in range(0,k):
        t=start+i*step
        s=stop+i*step
        nl=getnormal(a,f,t)
        nm=getnormal(a,f,s)
        [m,r]=normaltocirc(nl)
        op=op+"l"+str(i)+": "+circtogg(m,r)+"\n"
        [m, r] = normaltocirc(nm)
        op = op + "m"+str(i)+": " + circtogg(m, r) + "\n"
    print(op)
a = float(input("a: "))
f = float(input("f: "))
k = int(input("k: "))
start = float(input("Start: "))
stop = float(input("Stop: "))
step = float(input("Step: "))

printnet(a,f,k,start,stop,step)