#Calcule a media de 10 alunos e da média da sala
cona = 0
conr = 0
cone = 0

for i in range(1,61):
    print(i,"º aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2)/2
    if media >= 5:
        cona = cona+1
    elif media < 3:
        conr = conr+1
    else:
        cone = cone+1
print(f"A quantidade de alunos aprovados: {cona}")
print(f"A quantidade de alunos reprovados: {conr}")
print(f"A quantidade de alunos em exame: {cone}")
