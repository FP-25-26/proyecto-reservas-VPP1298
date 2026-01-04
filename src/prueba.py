from datetime import *

fecha1 = datetime.strptime("2022-01-06", "%Y-%m-%d").date()
fecha2 = datetime.strptime("2022-01-01", "%Y-%m-%d").date()

print((fecha2-fecha1).days)

lista1 = [1, 2, 4, 7]
lista2 = [8, 9, 0]

lista1 += lista2
print(lista1)