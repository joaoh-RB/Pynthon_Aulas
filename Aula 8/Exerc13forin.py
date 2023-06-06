#Leia a idade e 1000 pessoas e exiba a classe eleitoral

nObg = 0
eObg = 0
facul = 0

for i in range(1,1001):
    print("idade",i,"º eleitor : ")
    n1 = int(input("Digite a idade do eleitor: "))
    while n1 < 1 or n1 > 120:
        print("Idade invalida, redigite: ",end="")
        n1 = int(input())
    if n1 < 16:
        nObg = nObg+1
    elif n1 >= 18 and n1 <= 65 :
        eObg = eObg+1
    else:
        facul = facul+1
print("A quantidade não eleitores: {nObg}")
print("A quantidade eleitores obrigatórios: {eObg}")
print("A quantidade eleitores facultativos: {facul}")
