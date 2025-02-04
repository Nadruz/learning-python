import os

mensagem = []

nome = input("Nome: ")

while True:

    # Limpando terminal
    os.system('cls')

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])

    print("______________")

    # Obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # Adicionando mensagem na lista
    mensagem.append({
        "nome": nome,
        "texto": texto
    })
