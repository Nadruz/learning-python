# Utilizando for
notas = []

for x in range(5):
    codigo_aluno = input ("RM: ")
    nota = float (input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("Quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota: ", nota)


