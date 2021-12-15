import time

a1 = int(input("A'nın x eksenindeki değeri : "))
a2 = int(input("A'nın y eksenindeki değeri : "))
b1 = int(input("B'nin x eksenindeki değeri : "))
b2 = int(input("B'nin y eksenindeki değeri : "))
c1 = int(input("C'nin x eksenindeki değeri : "))
c2 = int(input("C'nin y eksenindeki değeri : "))

p1 = int(input("P noktasının x eksenindeki degeri :"))
p2 = int(input("P noktasının y eksenindeki degeri : "))

A = (a1,a2)
B = (b1,b2)
C = (c1,c2)
P = (p1,p2)
print("--",A,B,C,"------->>>",P)

bx = b1-a1
by = b2-a2
cx = c1-a1
cy = c2-a2
x = p1-a1
y = p2-a2
d = (b1*c2) - (c1*b2)


WA = (x*b2*c2) + ((y*c1)-(y*b1) + (b1*c2) - (c1*b2)) / d
WB = ((x*c2) - (y*c1))/ d
WC = ((y*b1) - (x*b2)) /d




if WA > 0 and WB and WC < 1 :
    print("WA degeri : ",WA)
    print("WB degeri : ",WB)
    print("WC degeri : ",WC)
    time.sleep(3)
    print("P noktası, üçgenin alanının içindedir .")

else:
    print("WA degeri : ", WA)
    print("WB degeri : ", WB)
    print("WC degeri : ", WC)

    time.sleep(3)
    print("P noktası, üçgenin alanının dışındadır.")
