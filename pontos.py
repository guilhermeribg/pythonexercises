import math

x = float(input("Ponto 1: "))
y = float(input("Ponto 2: "))
x1 = float(input("Ponto 3: "))
y1 = float(input("Ponto 4: "))

dis = math.sqrt(((x1 - x)**2)+((y1-y)**2))

if (dis)>10:
    print("Longe")
else:
    print("Perto")