from random import randint
posiçao = [19, 6]
minha_pokedex = {}
listapokemon = ['Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu', 'Evee']

mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]

def aleatorio(valor):
    return randint(0,valor)

def menu():
    print('''
    9 - Para abrir esse menu
    8 - Subir
    2 - Descer
    4 - Ir para esquerda
    6 - Ir para direta
    5 - Abrir Pokedex
    0 - Sair do Jogo
          ''')


def movimentaçao(mover):
    if mover == 8:
        if posiçao[0]-1 == -1:
            print('Você quer sair da rota? Tudo bem... até a próxima!')
            return False
        elif mapa[posiçao[0]-1][posiçao[1]] in ['E', 'A']:
            print('Bump!')
        else:
            if mapa[posiçao[0]-1][posiçao[1]] in ['G']:
                captura = randint(1,2)
                if captura == 1:
                    capturar()
                    posiçao[0] -= 1
                elif captura == 2:
                    posiçao[0] -= 1
            else:
                posiçao[0] -= 1
    if mover == 2:
        if posiçao[0]+1 == 20:
            print('Você quer sair da rota? Tudo bem... até a próxima!')
            return False
        elif mapa[posiçao[0]+1][posiçao[1]] in ['A']:
            print('Bump!')
        else:
            if mapa[posiçao[0]+1][posiçao[1]] in ['G']:
                captura = randint(1,2)
                if captura == 1:
                    capturar()
                    posiçao[0] += 1
                else:
                    posiçao[0] += 1
            elif mapa[posiçao[0]+1][posiçao[1]] in ['E']:
                if mapa[posiçao[0]+2][posiçao[1]] in ['G']:
                    captura = randint(1,2)
                    if captura == 1:
                        capturar()
                posiçao[0] += 2
            else:
                posiçao[0] += 1
    if mover == 4:
        if mapa[posiçao[0]][posiçao[1]-1] in ['A', 'E']:
            print('Bump!')
        else:
            if mapa[posiçao[0]][posiçao[1]-1] in ['G']:
                captura = randint(1,2)
                if randint == 1:
                    capturar()
                posiçao[1] -= 1
            else:
                posiçao[1] -= 1
    if mover == 6:
        if mapa[posiçao[0]][posiçao[1]+1] in ['A', 'E']:
            print('Bump!')
        else:
            if mapa[posiçao[0]][posiçao[1]+1] in ['G']:
                captura = randint(1,2)
                if captura == 1:
                    capturar()
                posiçao[1] += 1
            else:
                posiçao[1] += 1


def capturar():
    print('Um pokemon Selvagem apareceu!!!')
    print('Capturar ou correr? [1-Capturar ou 2-Correr]')
    capcor = int(input())
    while capcor not in [1, 2]:
        print('Capturar ou correr? [1-Capturar ou 2-Correr]')
        capcor = int(input())
    if capcor == 1:
        x = listapokemon[randint(0,9)]
        if x not in minha_pokedex:
            minha_pokedex[x] = {
                'Hp' : aleatorio(100),
                'Atk' : randint(0,100),
                'Def' : randint(0,100),
                'SP. Atk' : randint(0,100),
                'SP. Def' : randint(0,100),
                'Speed' : randint(0,100),
            }
            print('Pokemon Capturado!')
        elif x in minha_pokedex:
            print('Pokemon já registrado!')
    else:
        print('Fujão!')


def pokedex():
    print('Digite')
    print('1 para listar detalhes')
    print('2 para apagar registro')
    print('0 para voltar ao menu principal')
    escolhapokedex = int(input('Escolha uma ação: '))
    while escolhapokedex not in [1, 2, 0]:
        print('Resposta inválida!')     
        escolhapokedex = int(input('Escolha uma ação: '))   
    while True:
        if escolhapokedex == 1:
            print('Pokemons Registrados na pokedex: ')
            for k, v in minha_pokedex.items():
                print()
                print(k, v)
        elif escolhapokedex == 2:
            excluirpokemon = input('Qual registro deve ser apagado? ')
            while excluirpokemon not in minha_pokedex:
                print('Não há esse pokemon registrado!')
                excluirpokemon = input('Qual registro deve ser apagado? ')
            if excluirpokemon in minha_pokedex:
                del minha_pokedex[excluirpokemon]
                print(f'{excluirpokemon} excluído da pokedex!')
        elif escolhapokedex == 0:
            print('OK! vamos voltar para o mapa!')
            break
        print('Digite')
        print('1 para listar detalhes')
        print('2 para apagar registro')
        print('0 para voltar ao menu principal')
        escolhapokedex = int(input('Escolha uma ação: '))

print('-='*20)
print('        BEM VINDO AO FIRE RED        ')
print('-='*20)
print('A qualquer momento você pode escolher uma das opções:')
menu()
print('-='*20)
print('Entrando na Rota 1')
print('-='*20)

while True:
    if len(minha_pokedex) == 10:
        print('PARABÉNS! VOCÊ CONSEGUIU! POKEDEX CONCLUÍDA!')
        break
    print(f'Sua posição atual é {posiçao}')
    pergunta = int(input('Escolha uma opção: '))
    if pergunta == 8:
        conquista = movimentaçao(8)
        if conquista == False:
            print('Saindo do mapa...!')
            break
    elif pergunta == 2:
        conquista = movimentaçao(2)
        if conquista == False:
            print('Saindo do mapa...')
            break
    elif pergunta == 4:
        movimentaçao(4)
    elif pergunta == 6:
        movimentaçao(6)
    elif pergunta == 9:
        menu()
    elif pergunta == 5:
        pokedex()
        menu()
    elif pergunta == 0:
        break

print('-='*20)
print('              FIM DO JOGO!              ')
print('-='*20)