#Joguinho do advinha
count=0
j1 = int(input("Jogador 1, digite um número de 1 a 10: "))

while j1 < 1 or j1 > 10:
        print("Digite novamente um número: ",end="")
        j1 = int(input())

j2 = int(input("Jogador 2, digite um número de 1 a 10: "))

while j2 < 1 or j2 > 10:
        print("Digite novamente um número: ",end="")
        j2 = int(input())

while j1 != j2:
    count = count + 1
    print("Número incorreto, digite novamente um número: ",end="")
    j2 = int(input())
    while j2 < 1 or j2 > 10:
        print("Digite novamente um número: ",end="")
        j2 = int(input())
    
print(f"O Número é {j1}. Você tentou {count} vezes")