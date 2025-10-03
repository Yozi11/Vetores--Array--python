import os 
os.system("cls")

# Cria uma lista (vetor) vazia para armazenar os números.
vetor = []


for i in range(5):
    valor = int(input(f"digite o valor{i+1}: "))
     # Verifica se o número informado pelo usuário é negativo.
    if valor < 0:
       # Se for negativo, adiciona o valor 0 à lista.
        vetor.append(0)
        # Se não for negativo (for 0 ou positivo),
        # adiciona o próprio número que o usuário digitou à lista.
    else:
        vetor.append(valor)    

# Após o laço terminar, o programa imprime uma linha em branco para organização.
print("\n--------------------")
# Imprime o texto para informar o que será exibido.
print("Valores do vetor:")
# Imprime a lista final com todos os números.
print(vetor)
