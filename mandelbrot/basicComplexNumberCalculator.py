Web VPython 3.2
z =[1/sqrt(2), 1/sqrt(2)]
#Basic Code
def modulus(v):
    #the v[0] component is the real component, the v[1] component is the imaginary component
    return sqrt(v[0]**2+v[1]**2)
def phase(v):
    return atan2(v[1], v[0])
def conjugate(v):
    return [v[0], -1*v[1]]
def prtstr(v):
    print(v[0], "i:", v[1])
def add(v, b):
    return [v[0] + b[0], v[1]+b[1]]
def sub(v, b):
    return[v[0]-b[0],v[1]-b[1]]
def mult(v, b):
    return[v[0]*b[0]-v[1]*b[1], v[0]*b[1]+v[1]*b[0]]

def div(v, b):
    return(mult(mult(v, conjugate(b)), [modulus(b), 0]))
##Tests
#prtstr(z)
#print(modulus(z))
#print(phase(z))
#print(conjugate(z))
#zstar = conjugate(z)
#print(modulus(zstar))
#multiconj = mult(z, zstar)
#prtstr(multiconj)
#print(modulus(z))
#print(div(multiconj, z))
