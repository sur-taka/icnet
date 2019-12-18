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

		
