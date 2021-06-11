#Crie um programa que leia vários números inteiros pelo teclado. Nesta
#leitura de números o programa deve validar se o usuário não está informando
#números, e deve tratar a exceção em caso de informar algum valor que não pode
#ser convertido para inteiro, com por exemplo uma letra ou palavra.
#No final da execução, mostre a média entre todos os valores e qual foi o maior
#e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
#não continuar a digitar valores.
#ATENÇÃO:  Não deve ser usado as funções max e min, prontas do python, o objetivo e testar sua lógica.

while True:
    try:
        maior = 0
        menor = 9999999999999999999999999999
        cont = 1
        soma = 0
        numero = int(input('digita um número ae: '))
        soma += numero
        cont += 1
        media = (soma/cont)
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

        decisao = input('quer digitar mais? s/n ')
        if decisao == 'n':
            print('o maior numero e:', maior)
            print('O menor e: ', menor)
            print('A media foi de', media)
            break
        else:
            print('blz')

    except:
        print('apenas numeros interos pffffr  ')