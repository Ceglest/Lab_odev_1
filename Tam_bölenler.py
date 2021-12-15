sayi = int(input("Sayı giriniz : "))
T= []
for i in range(1, sayi + 1):
    if sayi % i == 0:
        T.append(i)
        T.append(-i)



print(sayi,"Sayısının Tam Bölenleri :",T)
