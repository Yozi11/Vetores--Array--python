import os
os.system("cls")



# Algoritmo que preenche um vetor com 5 números,
# mostra a quantidade de números negativos e a soma dos números positivos.




numeros = []

# Preenchendo o vetor com 5 números
for i in range(5):
    valor = int(input(f"digite o {i+1} numero"))
    numeros.append(valor)

quantidade_negativos = 0
soma_positivos = 0

for numero in numeros:
    if numero < 0:
        quantidade_negativos += 1
    elif  numero > 0:
          soma_positivos += numero
print(f"quantidade de numero negativos: {quantidade_negativos}")
print(f"soma dos numero positivos: {soma_positivos}")        



