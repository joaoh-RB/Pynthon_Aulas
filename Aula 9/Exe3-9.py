#Produção de 400  peças
a=0
r=0
count=1

while count < 5:
    print("Digite o estado da peça",count,"com A de aprovado ou R de reprovado: ",end="")
    est = str(input("")).upper()
    while est != "R" and est != "A":
        print("Digite novamente o estado da peça, de forma válida: ",end="")
        est = str(input("")).upper()

    if est == "R":
        r=r+1
        print(f"A peça de número {count} foi reprovada.")
        count= count+1
    else:
        a=a+1
        count= count+1

print(f"A quantidade de peças aprovadas foram {a}. \n Peças reprovadas foram {r}")