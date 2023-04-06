senha = int(input('cadastre sua primeira senha:'))
print('senha cadastrada')

print("Confirme a senha cadastrada")
while True:
    conf1 = int(input("digite sua senha cadastrada:"))
    if senha == conf1:
        break
    elif senha != conf1:
        print("Senha não confirmada, tente novamente!")

cont = 0
for tentativa in range(3):
    conf = int(input('Insira sua senha cadastrada e já confirmada: '))
    if conf == senha:
        print('senha confirmada')
        break
    elif conf != senha:
        cont = cont + 1
        if cont == 3:
            print('celular bloqueado. Procure uma assistência técnica especializada')
            break
        print('Senha incorreta, tente novamente')
        print(f'Você está na {cont+1}ª tentativa, de 3 possíveis.')

print('Hello Moto!')
