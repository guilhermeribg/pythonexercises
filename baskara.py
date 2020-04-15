import math
    
a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b ")) 
c = float(input("Digite o valor de c ")) 

d = (b**2 - 4*(a*c))
print("Delta ", d)

if d == 0:
    x = -b/2*a
    print("Tem uma raiz real que é", x)

elif d<0:
    print("Não tem raiz")

elif d>0:
    d2 = math.sqrt(d) 
    x1 = ((-b + d2)/(2*a)) 
    x2 = ((-b - d2)/(2*a))
    print("Tem duas raizes real que são ",x1, "e ", x2)