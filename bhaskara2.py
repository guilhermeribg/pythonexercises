import math
    
a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b ")) 
c = float(input("Digite o valor de c ")) 

def d (b,a,c):
    return(b**2 - 4*(a*c))
def x (b, a):
    return (-b/2*a)
def x1 (b, d2, a):
    return ((-b + math.sqrt(delta))/(2*a)) 
def x2 (b, d2, a):
    return ((-b - math.sqrt(delta))/(2*a))

if d(b,a,c) == 0:
    print("a raiz desta equação é",x (b, a))

elif d (b,a,c)<0:
    print("esta equação não possui raízes reais")

elif d (b,a,c)>0:
    delta = d(b,a,c)
    raiz1 = x1(b,math.sqrt(delta),a)
    raiz2 = x2(b,math.sqrt(delta),a)
    if raiz1>raiz2:
        print("as raízes da equação são",raiz2, "e",raiz1)
    else:
        print("as raízes da equação são",raiz1, "e",raiz2)