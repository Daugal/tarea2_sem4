altura = int(input("Digite un número entero para el triángulo: "))

for i in range(1, altura + 1): 
    for j in range(i):  
        print("*", end="")
    print() 
