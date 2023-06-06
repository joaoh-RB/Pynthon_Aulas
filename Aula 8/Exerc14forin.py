

print("Tabuada")
tabuada = int(input("Digite a tabuada de qual numero: "))
while tabuada < 1 or tabuada > 10:
    print("Numero invalido, redigite: ",end="")
    tabuada = int(input())
for i in range(1,11):
    resultado = tabuada * i
    print(f"{tabuada:2} * {i:2} = {resultado:3}")