n = int(input("Digite un número entero: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es un número primo")
else:
    print(str(n) + " no es un número primo")