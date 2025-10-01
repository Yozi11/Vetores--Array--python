import os
os.system

#criando um vetor(lista)
listas_notas = []
#inserir notas
for i in range(3):
    nota = int(input(f"digite a{i+1}: nota"))
    listas_notas.append(nota)
media = sum(listas_notas)/3
#mostrar notas
print("\nresultados: ")
for i in range(3):
    print(f"nota:{listas_notas}")
    if listas_notas[i] >=7:
        resultado = "aprovado"
    elif listas_notas[i] >= 5:
        resultado = "recuperação"
    else:
        resultado = "reprovado"



print("f\nMedia: {media}")
print(f"media: {media}")        
     