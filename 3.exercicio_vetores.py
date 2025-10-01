import os
os.system("cls")


numeros = []

for i in range(5):
   num = int(input(f"digite o {i+1}numero: "))
   numeros.append(num)
maior =max(numeros)
menor = min(numeros)

print("\nnumeros informados:",numeros )
print("menor numero informado: ", menor)
print("maior numero informado",maior)