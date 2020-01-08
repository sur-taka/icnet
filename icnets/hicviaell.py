import numpy as np
import scipy.special as sl
import scipy as sp
import numpy.linalg as la
from scipy.linalg import det
import math
from elliptic import *

#get normal calculates a tangentnormal of the form (A*sn(t),B*cn(t),C*dn(t) for a hyperbolic conic corresponding to the
#equation: (x/a)^2+(y/b)^2-z^2=0, 0<a<b<1
def getnormal(a,b,t):
    e = sl.ellipj(t,1-((a**2*(1-b**2))/(b**2*(1-a**2))))
    s=e[0]
    c=e[1]
    d=e[2]
    x=1/(math.sqrt(1-a**2)) * s
    y=1/(math.sqrt(1-b**2)) * c
    z=math.sqrt(b**2/(1-b**2))*d
    return [x,y,z]

#normaltocirc calculates circle center and radius in the poincare model of a hyp line given by normal
def normaltocirc(n):
    m=[n[0]/n[2],n[1]/n[2]]
    r=1/n[2]
    return [m,r]

#makenet returns sets of normals of k net-lines l and m for hyp conic with eq (x/a)^2+(y/b)^2
#ps0,s1 are start parametrization with stepwidth step
def makenet(a,b,k,s0,s1,step):
    l=[]
    m=[]
    for i in range(0,k):
        t=s0+i*step
        s=s1+i*step
        l.append(getnormal(a,b,t))
        m.append(getnormal(a,b,s))
    return [m,l]

#printnet turns normals of the lines l,m into poincare lines in geogebra input
def printnet(m,l):
    op=""
    for i in range(0,k):
        #print(str(l[i]))
        [m0, r] = normaltocirc(l[i])
        op = op + "l" + str(i) + ": " + circtogg(m0, r) + "\n"
        [m0, r] = normaltocirc(m[i])
        op = op + "m" + str(i) + ": " + circtogg(m0, r) + "\n"
    print(op)

#circtogg turns circle center and radius into geogebra input
def circtogg(m,r):
    op="(x-"+str(m[0]) +")^2 + (y - "+str(m[1]) + ")^2 =("+str(r)+")^2"
    return op

#start read input for net
a = float(input("a: "))
b = float(input("b: "))
k = int(input("k: "))
start = float(input("Start: "))
stop = float(input("Stop: "))
step = float(input("Step: "))
#stop read input
#make the corresponding net and print gg output
[l,m]= makenet(a,b,k,start,stop,step)
printnet(m,l)
