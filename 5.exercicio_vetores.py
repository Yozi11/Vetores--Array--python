cardapio = [
    [1,"picanha", 25.00],
    [2,"lasanha",20.00],
    [3,"strogonff",18.00],
    [4,"bife acebolado",15.00],
    [5,"pao com ovo",5,00],
]
#lista com os pratos do cardapio. Cada prato é uma lista com:[código, nome, valor]
pedidos = []
#lista para guardar os pratos escolhidos pelo usúario

continuar = "s"
# Variável de controle para o loop, começa como "s"(sim)
while continuar == "s":
    #mostra o cardapio formatado
    print("CODIGO | PRATO           | VALOR(R$)")
    print("---------------------------------------")
    for prato in cardapio:
        print(f"{prato[0]:<7} |{prato[1]:<15} | {prato[2]:>7.2f}")

    codigo = int(input("digite o codigo do prato desejado: "))
    #pede para o usuario digitar o codigo do prato


    match codigo:
        case 1:
            pedidos.append(cardapio[0])
            print(f"voce escolheu: {cardapio[0][1]} -R$ {cardapio[0][2]:.2f} ")
        case 2:
            pedidos.append(cardapio[1])
            print(f"voce escolheu: {cardapio[1][1]} -R$ {cardapio[1][2]:.2f}")
        case 3:
            pedidos.append(cardapio[2])
            print(f"voce escolheu: {cardapio[2][1]} -R${cardapio[2][2]:.2f}")
        case 4:
            pedidos.append(cardapio[3])
            print(f"voce escolheu: {cardapio[3][1]} -R$ {cardapio[3][2]:2f}")
        case 5:
            pedidos.append(cardapio[4])
            print(f"voce escolheu: {cardapio[4][1]} -R${cardapio[4][2]:.2f} ")
        case _:
            print("codigo invalido. tente novamente.")
            continue
    #usando match case, verifica qual prato foi escolgido e adiciona a lista de pedidos
    # se o codigo nao existir, mostra mensagem de erro e volta pra o inicio de loop
    
    continuar = input("deseja escolher outro prato? (s/n)").strip().lower
    #pergunta se o usuario quer pedir mais pratos

print("\npratos escolhidos: ")
total = 0
for prato in pedidos:
    print(f"{prato[1]}- R$ {prato[2]:.2f}")
    total += prato [2]
# mostra todos os pratos escolhidos e soma o valor total

print(f"total a paga:R$ {total:.2f}")

#exibe o valor total da conta

        

