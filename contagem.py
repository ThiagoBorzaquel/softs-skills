from time import sleep


def contador(i, f, p):
    print('-=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        print('-=-' * 20)


inicio = int(input('Qual o inicio? '))
fim = int(input('Qual o fim? '))
passo = int(input('Qual o passo? '))
contador(inicio, fim, passo)
#contador(1, 10, 5)
print('-=-'*20)