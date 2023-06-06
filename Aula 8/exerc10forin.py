#receber N numeros e contar quantos sao pares
from time import sleep

n = int(input("Digite a quantidade de numeros a serem analisados: "))
qtd = 0
for i in range(1,n+1,1):
    print(f"Digite o {i}º numero: ",end="")
    num = int(input())
    if num % 2 == 0:
        qtd = qtd+1
print("Analisando...")
sleep(1.5)
print(f"\nExistem {qtd} numeros pares")