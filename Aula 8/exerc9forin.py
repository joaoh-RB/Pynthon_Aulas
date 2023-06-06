#Calcule a media de 10 alunos e da média da sala
s=0
for i in range(1,11,1):
    print(i,"º aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2)/2
    print(f"A sua media é de: {media:.1f}")
    s = s + media
mediasala = s / 3
print(f"A media da sala é de: {mediasala:.2f}")