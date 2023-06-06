import os
os.system('cls')

print("Programa para receber dados de 5 produtos e calcular o imposto, valor do transporte e o valor do seguro.")
soma=0
valorTrans=0
seguro=0
for i in range (1,6):

    print("Digite o preço do produto",i,": ",end="")
    price = float(input(""))
    while price < 0:
        price=int(input("Digite um preço valido: "))
    
    print("Opções de país de origem: \n 1 - EUA \n 2 - México \n 3 - Outros ")
    opcPais = int(input("Digite uma opção:"))
    while opcPais < 1 or opcPais >3:
        opcPais=int(input("Digite uma opção de país de origem valida: "))

    print("Opções de meio de transporte: \n T - Terrestre \n F - Fluvial \n A - Aéreo ")
    opcTrans = str(input("Digite uma opção:")).upper()
    while opcTrans != "T" and opcTrans != "F" and opcTrans != "A":
        opcTrans=int(input("Digite uma opção de meio de transporte valida: "))

    print("A carga é perigosa? Opções:\n S - Sim \n N - Não")
    opcCarga = str(input("Digite uma opção:")).upper()
    while opcCarga != "S" and opcCarga != "N":
        opcCarga=int(input("Digite uma opção de carga valida: "))

    if price >100:
        imposto = price*10/100

    else:
        imposto = price*5/100

    if opcCarga =="S":
        if opcPais == 1:
            valorTrans = 50
        elif opcPais == 2:
            valorTrans == 35
        elif opcPais == 3:
            valorTrans == 24

    else:
        if opcPais == 1:
            valorTrans = 12
        elif opcPais == 2:
            valorTrans == 35
        elif opcPais == 3:
            valorTrans == 60

    if opcPais==2:
        seguro = price/2
    elif opcTrans=="A":
        seguro = price/2
    
    else:
        seguro = 0

    soma= price+imposto+valorTrans+seguro

    print(f"O preço final do produto {i},com imposto, valor do transporte e seguro incluso é de {soma:.2f}")
