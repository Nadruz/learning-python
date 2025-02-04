fluxo_caixa = []

print("_____________")
print("@ Fluxo caixa")
print("_____________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")

def adicionar_transicao():
    nome = input("Nome: ")
    valor = float( input("Valor: ") )
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })
    
while True:
    
    opcao = int( input("Digite a opcao: ") )

    if opcao == 1:
        adicionar_transicao()
    elif opcao == 2:
        adicionar_transicao()
    else:
        break

# Nota fiscal
total = 0 
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valor'])
    total = total + fc['valor']

print("Saldo atual: R$", total)
