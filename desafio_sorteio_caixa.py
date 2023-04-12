
#importação da lib 
import random

#criando listas com o nome e telefone
client_names = []
client_phones = []


#criando o while 
while True:
    #digite o nome do cliente, e se o 'input_name' for igual a 'fim' da break
    input_name = input('Enter a client name: ')
    if input_name == 'fim':
        break
    #digite o telefone 
    input_phone = input('Enter a client phone: ')

    #função append pra acrescentar elementos à lista
    client_names.append(input_name)
    client_phones.append(input_phone)


    #print na lista final para saber os elementos
    print(client_names, client_phones)

  #sorteio do número aleatório
random_number = random.randrange(0, len(client_names))

  #uso do número aleatório para informar a pessoa vencedora
print(f'O ganhador foi {client_names[random_number]}, seu número é {client_phones[random_number]}')
