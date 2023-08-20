import random
import os

#1 - Criar listas com nomes, e-mails, telefones, cidades e estados.
nomes = ['Josiel', 'Lucas', 'Laura', 'João', 'Joyce', 'Dhiego', 'Lourdes']
emails = ['josiel@gmail.com','lucas@gmail.com', 'joyce@gmail.com', 'dhiego@gmail.com', 'joao@gmail.com', 'lourdes@gmail.com']
telefones = ['(81) 9 9745-5422', '(81) 9 8748-2358', '(81) 9 8516-8619', '(81) 9 8723-4688', '(81) 9 7305-8910', '(81) 9 8519-2301']
cidades = ['Recife', 'São Paulo', 'Rio de Janeiro', 'Manaus', 'Gramado', 'Fortaleza']
estados = ['Pernambuco', 'São Paulo', 'Rio de Janeiro', 'Amazonas', 'Rio Grande do Sul', 'Ceará']

#2 - Codar o loop que só irá parar se receber a resposta "parar"
while True:
#3 - Criar o menu.
    print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"')
    print('-----------------------')
    print('Escolha uma ou mais opções abaixo para serem geradas aleatóriamente: ')
    print("""
    [1] - Nome
    [2] - E-mail
    [3] - Telefone
    [4] - Cidade
    [5] - Estado
    """)
    resposta1 = input('Digite uma ou mais opções separadas por vírgula: ')
#4 - Realizar o gerador de informações através das listas criadas com if
    if resposta1.lower() == 'parar':
        break

    opcoes = resposta1.split(',')

    resultados = []
    
    for opcao in opcoes:
        opcao = opcao.strip()
        if opcao == '1':
            nome_gerado = (random.choice(nomes))
            print(nome_gerado)
            resultados.append(nome_gerado)
        elif opcao == '2':
            email_gerado = (random.choice(emails))
            print(email_gerado)
            resultados.append(email_gerado)
        elif opcao == '3':
            telefone_gerado = (random.choice(telefones))
            print(telefone_gerado)
            resultados.append(telefone_gerado)
        elif opcao == '4':
            cidade_gerada = (random.choice(cidades))
            print(cidade_gerada)
            resultados.append(cidade_gerada)
        elif opcao == '5':
            estado_gerado = (random.choice(estados))
            print(estado_gerado)
            resultados.append(estado_gerado)
        elif opcao == '1, 2, 3, 4, 5':
            nome_gerado = (random.choice(nomes))
            print(nome_gerado)
            resultados.append(nome_gerado)
            email_gerado = (random.choice(emails))
            print(email_gerado) 
            resultados.append(email_gerado)                  
            telefone_gerado = (random.choice(telefones))
            print(telefone_gerado)
            resultados.append(telefone_gerado)
            cidade_gerada = (random.choice(cidades))
            print(cidade_gerada)
            resultados.append(cidade_gerada)
            estado_gerado = (random.choice(estados))
            print(estado_gerado)
            resultados.append(estado_gerado) 
                            
#5 - Criar o controle if e salvar os dados em um arquivo .txt 

    print('-----------------------')
    resposta2 = input('Deseja salvar os dados em um arquivo de texto? (S/N)')
    if resposta2.lower() == 's':
        with open('dados.txt', 'w', encoding='utf-8', newline='') as arquivo:
            for resultado in resultados:
                arquivo.write(resultado + '\n')
        print('Dados salvos no arquivo dados.txt')
    elif resposta2.lower() == 'n':
        break