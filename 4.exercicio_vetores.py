import os
os.system("cls")

#contagem pares e impares
pares = 0
impares = 0

lista_numeros = []
# leitura dos numeros
for i in range(6):
    numero = int(input(f"insira o {i+1} numero: "))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("numeros informados: ", lista_numeros)
print(f"quantidade de numero pares: {pares}")
print(f"quantidade de numero impares: {impares}")
