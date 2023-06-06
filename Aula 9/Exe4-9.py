print("Calcule a quantidade e o valor total a ser pago pelo pedido")
total=0
item=0
count=1

while True:
#Cardapio Bom apetite lanchonete
    print("Código do lanche       Especificações     Preço")
    print("100                    Cachorro quente    2,50 \n101                    Bauru simples      2,00\n102                    Bauru c/ovo        3,50\n103                    Hamburguer         5,10\n104                    ChesseBurger       3,30\n105                    Refrigerante       2,00")

    print("Digite o código do produto desejado: ",end="")
    cod = int(input(""))

    while cod != 100 and cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod != 105:
        print("Digite um código válido do produto desejado: ",end="")
        cod = int(input("")) 

    print("Digite a quantidade do item desejado: ",end="")
    item = int(input(""))
    while item < 0 :
        print("Digite a quantidade válida: ",end="")
        item = int(input(""))

    if  cod == 100:
        total = 2.50 * item
    elif cod == 101: 
        total = 2.00 * item 
    elif cod == 102:
        total = 3.50 * item 
    elif cod == 103:
        total = 5.10 * item 
    elif cod == 104:
        total = 3.30 * item 
    elif cod == 105:
        total = 2.00 * item 

    continuar = str(input("Digite 'C' para continuar e 'F' para finalizar o pedido: ")).upper()
    while continuar != "C" and continuar != "F"  :
            print("Parece que não fucionou, Digite 'C' para continuar e 'F' para finalizar o pedido: ",end="")
            item = int(input(""))

    if continuar == "F":
        break

print(f"O Valor total dos pedidos foram R${total}")