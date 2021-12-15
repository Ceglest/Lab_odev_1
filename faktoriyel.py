


def faktoriyel(sayi):
    baslangic = 1
    if sayi < 0:
        return "Sayilar negatif olmamalıdır.!!!"
    elif sayi == 0:
        return 1
    else:
        for i in range(1,sayi+1):
            baslangic *= i
        return baslangic
sayi = int(input(" Sayi Giriniz :  "))
c = faktoriyel(sayi)
print(c)