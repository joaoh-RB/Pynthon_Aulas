import os
os.system('cls')

print('''Criar uma agenda eletronica, em python que armazene em uma lista nome, telefone, empresa em que trabalha. Criar um menu com as seguintes opções:
1- Adicionar Contato | 2- Excluir Contato | 3- Listar todos os contatos | 4- Alterar contato | 5- Listar dados de um determinado contato | 6- Sair\n''')

lista = []
lista2 = []
confi = "S"

while confi == "S":
    menu = int(input("\tAGENDA ELETRONICA\n1- Adicionar Contato\n2- Excluir Contato\n3- Listar todos os contatos\n4- Alterar contato\n5- Listar dados de um determinado contato\n6- Sair\nEscolha umas das opções do menu: "))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6:
        menu = int(input("Digite somente 1,2,3,4,5 ou 6!"))

    if menu == 1: #Adicionar contato
        nome = str(input('Digite o nome: ')).title().strip()
        lista.append(nome)
        num = int(input('Digite o numero de telefone: '))
        lista.append(num)
        emp = input(f'Digite em qual empresa {nome} trabalha: ')
        lista.append(emp)
        lista2.append(lista[:])
        lista.clear()
                
    elif menu == 2: #Excluir contato
        rem = input("Quem voce deseja remover: ").upper()
        achou = False
        for e in range(len(lista2)):
            if rem == lista2[e][0]:
                del lista2[e]
                achou = True
                break
        if achou:
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado na lista.")
            

    elif menu == 3: # Listar todos os contatos
        if not lista2:
            print("A lista de contatos está vazia.")
        else:
            for j in range(len(lista2)):
                nome = lista2[j][0]
                telefone = lista2[j][1]
                empresa = lista2[j][2]
                print('nome: {}, telefone: {}, empresa: {}'.format(nome, telefone, empresa))

    elif menu == 4: #Alterar contato
        alt = input("Digite o nome do contato que deseja alterar: ").title().strip()
        achou = False
        for e in range(len(lista2)):
            if alt == lista2[e][0]:
                novo_nome = str(input('Digite o novo nome: ')).title().strip()
                novo_num = int(input('Digite o novo numero de telefone: '))
                nova_emp = input(f'Digite a nova empresa de {novo_nome}: ')
                lista2[e] = [novo_nome, novo_num, nova_emp]
                achou = True
                break
        if achou:
            print("Contato alterado com sucesso!")
        else:
            print("Contato não encontrado na lista.")
    
    elif menu == 5: #Listar dados de um determinado contato
        busca = input("Digite o nome do contato que deseja buscar: ").title().strip()
        achou = False
        for e in range(len(lista2)):
            if busca == lista2[e][0]:
                print(f"Nome: {lista2[e][0]}")
                print(f"Telefone: {lista2[e][1]}")
                print(f"Empresa: {lista2[e][2]}")
                achou = True
                break
        if not achou:
            print("Contato não encontrado na lista.")
            
    elif menu == 6: #Sair
        break
                
    confi = input("Deseja acessar novamente o menu? S/N: ").upper()
    while confi != "S" and confi != "N":
        confi = input("Digite S/N: ").upper()
