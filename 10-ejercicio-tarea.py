frase = input("Escriba una frase: ")
letra1 = input("Escriba una letra: ")

contador = 0
for letra2 in frase:
    if letra2 == letra1:
        contador += 1

print(f"La letra '{letra1}' aparece {contador} veces en la frase.")
