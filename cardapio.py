# Cardapio Davi

print('Vamos comer filho!\n')

escolha = str(input('Uma refeição ou todas? [uma/ todas] '))
refeição = str(input('Qual refeição? ')).capitalize()
dia = str(input('Que dia da semana? ')).capitalize()

def escolhe():
    if escolha in 'todas':
        print('teste')
    if escolha in 'todas':
       print('Teste')

def refeicao(refeiçao):

    if refeiçao in 'Cafe':
        cafedamanha(dia)

    if refeição in 'Almoço':
        almoço(dia)

    if refeição in 'Lanche':
        lanchetarde(dia)

def cafedamanha(dia):

    if dia in 'Domingo':
        print('A fruta é banana')

    if dia in 'Segunda':
        print('A fruta é pêra')

    if dia in 'Terça':
        print('A fruta é manga espada')

    if dia in 'Quarta':
        print('A fruta é mamão papaia')

    if dia in 'Quinta':
        print('A fruta é Maça')

    if dia in 'Sexta':
        print('A fruta é Morango')

    if dia in 'Sabado':
        print('A fruta é Caqui')

    print('Bom Apetite!!!')

    return dia

def almoço(dia):

    if dia in 'Domingo':
        print('o Almoço é:\n Carne\n Couve flor\n Abobora\n Feijão')

    if dia in 'Segunda':
        print('O almoço é:\n Peixe\n Brócolis\n Beterraba\n Feijão\n')

    if dia in 'Terça':
        print('O almoço é:\n Frango\n Couve\n chuchu\n Feijão\n')

    if dia in 'Quarta':
        print('O almoço é:\n Ovo\n Espinafre\n Cenoura\n Feijão\n')

    if dia in 'Quinta':
        print('O almoço é:\n Carne\n Repolho\n Berinjela\n Feijão\n')

    if dia in 'Sexta':
        print('O almoço é:\n Peixe\n Chicoria\n Abobrinha\n Feijão\n')

    if dia in 'Sabado':
        print('O almoço é:\n Frango\n Bertalha\n Quiabo\n Feijão\n')

    print('\nBom apetite!!!')

    return dia


def lanchetarde(dia):

    if dia in 'Domingo':
        print('O lanche é caqui!')

    if dia in 'Segunda':
        print('O lanche é morango!')

    if dia in 'Terça':
        print('O lanche é maça!')

    if dia in 'Quarta':
        print('O lanche é mamão papaia!')

    if dia in 'Quinta':
        print('O lanche é manga espada!')

    if dia in 'Sexta':
        print('O lanche é pêra!')

    if dia in 'Sabado':
        print('O lanche é banana!')

    print('\nBom apetite!!!')

    return dia

refeicao(refeição)
