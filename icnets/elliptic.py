import scipy.special as sl

def sn(u,m):
    return sl.ellipj(u,m)[0]
def cn(u,m):
    return sl.ellipj(u,m)[1]
def dn(u,m):
    return sl.ellipj(u,m)[2]
def ns(u,m):
    return 1/sn(u,m)
def nc(u,m):
    return 1/cn(u,m)
def nd(u,m):
    return 1/dn(u,m)
def sd(u,m):
    return sn(u,m)/dn(u,m)
def sc(u,m):
    return sn(u,m)/cn(u,m)
def cs(u,m):
    return 1/sc(u,m)
def cd(u,m):
    return cn(u,m)/dn(u,m)
def dc(u,m):
    return 1/cd(u,m)
def ds(u,m):
    return 1/sd(u,m)


