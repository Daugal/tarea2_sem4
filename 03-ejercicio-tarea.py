numero = int(input("Digite un número entero positivo: "))

print("Los números impares son:", end=" ")

for i in range(1, numero + 1, 2):
    if i < numero - 1:
        print(i, end=", ")
    else:
        print(i, end="")