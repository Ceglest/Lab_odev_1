from matplotlib import pyplot as plt
Ali = [48,155]
Mehmet = [52,157]
Mustafa = [55,162]
Zeynep = [58,165]
Mihriban = [60,167]
Can = [63,170]
Kaan = [67,176]
Ayse = [70,181]
Umut = [72,185]
Emirhan = [82,191]

liste = [Ali,Mehmet,Mustafa,Zeynep,Mihriban,Can,Kaan,Ayse,Umut,Emirhan]

plt.plot([155,157,162,165,167,170,176,181,185,191],[48,52,55,58,60,63,67,70,72,82])
plt.title('Kilo - Boy Grafiği')
plt.ylabel('Boy Degerleri  ')
plt.xlabel('Kilo Degerleri')
plt.show()

