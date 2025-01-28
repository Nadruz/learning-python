# criando uma lista de frutas
frutas = ["maçã", "banana", "laranja", "morango"]

# exibindo a lista 
print("lista de frutas: ", frutas)

# acessando elementos individuais - índices
print("Primeira fruta: ", frutas [0])
print("Última fruta: ", frutas [-1])

# adicionando mais uma fruta
frutas.append("melancia")
print("Lista após adicionar melancia: ", frutas)

# removendo uma fruta
frutas.remove("banana")
print("Lista após remover banana: ", frutas)

# ordenar em lista alfabética
frutas.sort()
print("Lista em ordem alfabética: ", frutas)

# verificando se uma fruta está na lista
if "laranja" in frutas:
    print("Laranja está na lista.")



