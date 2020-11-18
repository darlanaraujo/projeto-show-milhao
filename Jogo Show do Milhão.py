
# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint
import pygame

# ===================== VARIAVEIS GLOBAIS =============================================================================
# Nome do arquivo para salvar dados do jogo;
arq = 'jogoshowmilhao.txt'
nome = 'Nome Jogador'

# Tabela de cores;
sc = '\033[m'       # 0 = Sem cor
br = '\033[30m'     # 1 = Branco
vm = '\033[31m'     # 2 = Vermelho
vd = '\033[32m'     # 3 = Verde
am = '\033[33m'     # 4 = Amarelo
az = '\033[34m'     # 5 = Azul
rx = '\033[35m'     # 6 = Roxo
# Cores com fundo;
fvm = '\033[41;30m' # 7 = Fundo Vermelho Letra Branca

# Ajudas do jogo;
pulo = 3
carta = 1
convidado = 1
colega = 1

# Definição da posição do jogador na partida;
p = 0

# Definição dos valores para cada rodada;
valor = ['R$ 1.000,00', 'R$ 2.000,00', 'R$ 3.000,00', 'R$ 4.000,00', 'R$ 5.000,00',
         'R$ 10.000,00', 'R$ 20.000,00', 'R$ 30.000,00', 'R$ 40.000,00', 'R$ 50.000,00',
         'R$ 100.000,00', 'R$ 200.000,00', 'R$ 300.000,00', 'R$ 400.000,00', 'R$ 500.000,00', 'R$ 1.000.000,00']

# Definição para a variável de premio que será exibida ao termino da jogada e mostrá-ra o valor ganho pelo jogador.
premio = 'R$ 0,00'
acerto = 'R$ 0,00'
errar = 'R$ 0,00'
parar = 'R$ 0,00'
# ===================== PERGUNTAS DO JOGO =============================================================================
# Essa função faz com que o sorteio não se repita; Lembrando que a ordem do sorteio corresponde a ordem das perguntas;

# NÍVEL 1
nivel1 = open('pergunta_nivel1', 'rt')

temp = []
lista1 = []

for dados in nivel1:
    dado = dados.split(';')
    dado[5] = dado[5].replace('\n', '')

    temp.append(dado[0])
    temp.append(dado[1])
    temp.append(dado[2])
    temp.append(dado[3])
    temp.append(dado[4])
    temp.append(dado[5])
    lista1.append(temp[:])
    temp.clear()

sorteio1 = []
while len(sorteio1) != len(lista1):
    r = randint(0, len(lista1) - 1)
    if r not in sorteio1:
        sorteio1.append(r)


# NÍVEL 2
nivel2 = open('pergunta_nivel2', 'rt')

temp = []
lista2 = []

for dados in nivel2:
    dado = dados.split(';')
    dado[5] = dado[5].replace('\n', '')

    temp.append(dado[0])
    temp.append(dado[1])
    temp.append(dado[2])
    temp.append(dado[3])
    temp.append(dado[4])
    temp.append(dado[5])
    lista2.append(temp[:])
    temp.clear()

sorteio2 = []
while len(sorteio2) != len(lista2):
    r = randint(0, len(lista2) - 1)
    if r not in sorteio2:
        sorteio2.append(r)

# NÍVEL 3
nivel3 = open('pergunta_nivel3', 'rt')

temp = []
lista3 = []

for dados in nivel3:
    dado = dados.split(';')
    dado[5] = dado[5].replace('\n', '')

    temp.append(dado[0])
    temp.append(dado[1])
    temp.append(dado[2])
    temp.append(dado[3])
    temp.append(dado[4])
    temp.append(dado[5])
    lista3.append(temp[:])
    temp.clear()

sorteio3 = []
while len(sorteio3) != len(lista3):
    r = randint(0, len(lista3) - 1)
    if r not in sorteio3:
        sorteio3.append(r)

# NÍVEL 4
nivel4 = open('pergunta_nivel4', 'rt')

temp = []
lista4 = []

for dados in nivel4:
    dado = dados.split(';')
    dado[5] = dado[5].replace('\n', '')

    temp.append(dado[0])
    temp.append(dado[1])
    temp.append(dado[2])
    temp.append(dado[3])
    temp.append(dado[4])
    temp.append(dado[5])
    lista4.append(temp[:])
    temp.clear()

sorteio4 = []
while len(sorteio4) != len(lista4):
    r = randint(0, len(lista4) - 1)
    if r not in sorteio4:
        sorteio4.append(r)

# NÍVEL PULO
nivel_pulo = open('pergunta_nivel0', 'rt')

temp = []
lista_pulo = []

for dados in nivel_pulo:
    dado = dados.split(';')
    dado[5] = dado[5].replace('\n', '')

    temp.append(dado[0])
    temp.append(dado[1])
    temp.append(dado[2])
    temp.append(dado[3])
    temp.append(dado[4])
    temp.append(dado[5])
    lista_pulo.append(temp[:])
    temp.clear()

sorteio0 = []
while len(sorteio0) != len(lista_pulo):
    r = randint(0, len(lista_pulo) - 1)
    if r not in sorteio0:
        sorteio0.append(r)


# ===================== FUNÇÕES DE AUXILIO DAS PERGUNTAS DO JOGO ======================================================
def perguntas(pergunta, resposta, proxima, p):

    pergunta = pergunta
    resposta = resposta

    print(
        f'{fvm}>>>  {pergunta[0]}?   {sc}'
        f'\n{am}A) {br}{pergunta[1]}'
        f'\n{am}B) {br}{pergunta[2]}'
        f'\n{am}C) {br}{pergunta[3]}'
        f'\n{am}D) {br}{pergunta[4]}')

    linha()
    som('audio/frase_entendeu.mp3')
    while True:
        som('audio/frase_respondemos.mp3')
        escolha = str(input(f'VOCÊ VAI RESPONDER OU PEDIR AJUDA? {am}[R/A]{br}: ')).upper().strip()[0]
        linha()
        if escolha == 'R':
            confirmacao(pergunta, resposta, proxima, premio)
        elif escolha == 'A':
            menu_ajuda(pergunta, resposta, proxima, p)
        else:
            erro(f'ERRO! Dados inválidos, digite apenas {am}R{br} ou {am}A{br}.')


def pula(pergunta, resposta, proxima, p):
    global pulo

    if pulo > 0:
        pulo -= 1
        som('audio/frase_pular.mp3')

        pergunta = lista_pulo[sorteio0[p]]
        resposta = pergunta[5]

        print(
            f'{fvm}>>>  {pergunta[0]}?   {sc}'
            f'\n{am}A) {br}{pergunta[1]}'
            f'\n{am}B) {br}{pergunta[2]}'
            f'\n{am}C) {br}{pergunta[3]}'
            f'\n{am}D) {br}{pergunta[4]}')

        linha()
        confirmacao(pergunta, resposta, proxima, premio)
    else:
        erro('Você já pulou 3 vezes. Você não tem mais essa opção!')
        menu_ajuda(pergunta, resposta, proxima, p)


def colegas(pergunta, resposta, proxima, p):
    global colega

    if colega > 0:
        colega -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)

        som('audio/frase_dificil_ajuda.mp3')
        som('audio/frase_colegas.mp3')
        print('A escolha dos nossos colegas são: Opção ', end='')
        for pos, v in enumerate(lista):
            print(f'- {vm}{v}{br} {pos +1}0%', end=' ')
            sleep(1)
        print(f'- {am}{resposta}{br} 40%')

        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)

    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)


def convidados(pergunta, resposta, proxima, p):
    global convidado

    if convidado > 0:
        convidado -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)

        som('audio/frase_dificil_ajuda.mp3')
        som('audio/frase_convidados.mp3')
        print('Escolha dos convidados: ', end='')

        for c in range(1, 4):
            print(f'{c}ª convidado: ', end='')
            if c < 3:
                print(f'{am}{resposta}{br} |', end=' ')
                sleep(1)
            else:
                print(f'{vm}{lista[0]}{br}')

        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)

    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)


def cartas(pergunta, resposta, proxima, p):
    global carta

    if carta > 0:
        carta -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)

        som('audio/frase_cartas.mp3')
        excluir = randint(1, 3)

        print(f'Você tirou um {excluir} !', end=' ')
        sleep(1)
        if excluir == 1:
            print('Que pena, você ainda tem 3 opções!')
        elif excluir == 2:
            print('Boa! só resta 2 opções agora.')
        elif excluir == 3:
            print('Parabéns! Agora ficou fácil...')

        print('Desconsidere as opções:', end=' ')
        print(f'{vm}{lista[-3: -0 + excluir]}{br}')

        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)
    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)


def confirmacao(pergunta, resposta, proxima, premio):
    while True:
        som('audio/frase_pergunta_certa.mp3')
        resp = str(input(f'{am}QUAL A RESPOSTA CERTA?{br} ')).upper().strip()[0]
        if resp in 'ABCD':
            linha()

            while True:
                som('audio/frase_pergunta.mp3')
                resp2 = str(input(f'VOCÊ ESTÁ CERTO DISSO, POSSO PERGUNTAR? {am}[S/N]{br}: ')).upper().strip()[0]
                linha()
                if resp2 == 'S':
                    if resp == resposta:
                        som('audio/frase_parabens.mp3')
                        print(f'{am}CERTA RESPOSTA!{br}')
                        som('audio/frase_acerto.mp3')

                        stop(arq, nome, premio)
                        if pulo == 3 and carta == 1 and convidado == 1 and colega == 1:
                            som('audio/frase2.mp3')
                            som('audio/frase1.mp3')
                        proxima()
                    else:
                        som('audio/frase_erro.mp3')
                        print(f'{vm}QUE PENA, VOCÊ ERROU!{br}')
                        premio = errar
                        final(arq, nome, premio)
                        break
                elif resp2 == 'N':
                    continue
                else:
                    erro(f'ERRO! dados inválidos, digite apenas {am}S{br} ou {am}N{br}.')

        else:
            erro(f'ERRO! Dados inválidos, digite apenas as opções {am}A B C D{br}')


def menu_ajuda(pergunta, resposta, proxima, p):
    som('audio/frase_ajuda1.mp3')
    print(f'{rx}A) {br}PULAR')
    print(f'{rx}B) {br}CARTAS')
    print(f'{rx}C) {br}CONVIDADOS')
    print(f'{rx}D) {br}COLEGAS')
    linha()
    som('audio/frase_opcoes.mp3')
    while True:
        som('audio/frase_ajuda2.mp3')
        resp = str(input('E PARA QUEM VOCÊ VAI PEDIR AJUDA? ')).upper().strip()[0]
        linha()
        if resp == 'A':
            pula(pergunta, resposta, proxima, p)
        elif resp == 'B':
            cartas(pergunta, resposta, proxima, p)
        elif resp == 'C':
            convidados(pergunta, resposta, proxima, p)
        elif resp == 'D':
            colegas(pergunta, resposta, proxima, p)
        else:
            erro('ERRO! Dados inválidos, digite apenas as opções do menu.')


# ===================== PERGUNTAS DO JOGO =============================================================================
def rodada1():
    """
    P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
        será escolhida.
    pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
        indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
        repetem, isso é feito na variável sorteio em variáveis globais).
    resposta: Ocorre o mesmo que na pergunta.
    cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
        chamada moeda, apenas para converter inteiro para o formato dinheiro.
    SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
        aúdio está.
    :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
        posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
        rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
        recurso da ajuda pular.
    """
    global arq_pergunta, premio, acerto, errar, parar, p

    arq_pergunta = 'pergunta_nivel2'

    acerto = valor[0]
    p = 0

    pergunta = lista1[sorteio1[0]]
    resposta = pergunta[5]

    cabecalho(f' 1ª PERGUNTA, VALENDO {valor[0]} REAIS')
    placar()
    som('audio/frase_1mil.mp3')
    perguntas(pergunta, resposta, rodada2, p)


def rodada2():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[1]
    parar = valor[0]
    p = 1

    pergunta = lista1[sorteio1[1]]
    resposta = pergunta[5]

    cabecalho(f' 2ª PERGUNTA, VALENDO {valor[1]} REAIS')
    placar()
    som('audio/frase_2mil.mp3')
    perguntas(pergunta, resposta, rodada3, p)


def rodada3():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[2]
    parar = valor[1]
    errar = valor[0]
    p = 2

    pergunta = lista1[sorteio1[2]]
    resposta = pergunta[5]

    cabecalho(f' 3ª PERGUNTA, VALENDO {valor[2]} REAIS')
    placar()
    som('audio/frase_3mil.mp3')
    perguntas(pergunta, resposta, rodada4, p)


def rodada4():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[3]
    parar = valor[2]
    errar = valor[1]
    p = 3

    pergunta = lista1[sorteio1[3]]
    resposta = pergunta[5]

    cabecalho(f' 4ª PERGUNTA, VALENDO {valor[3]} REAIS')
    placar()
    som('audio/frase_4mil.mp3')
    perguntas(pergunta, resposta, rodada5, p)


def rodada5():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[4]
    parar = valor[3]
    errar = valor[2]
    p = 4

    pergunta = lista1[sorteio1[4]]
    resposta = pergunta[5]

    cabecalho(f' 5ª PERGUNTA, VALENDO {valor[4]} REAIS')
    placar()
    som('audio/frase_5mil.mp3')
    perguntas(pergunta, resposta, rodada6, p)


def rodada6():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[5]
    parar = valor[4]
    errar = valor[3]
    p = 5

    pergunta = lista2[sorteio2[0]]
    resposta = pergunta[5]

    cabecalho(f' 6ª PERGUNTA, VALENDO {valor[5]} REAIS')
    placar()
    som('audio/frase_10mil.mp3')
    perguntas(pergunta, resposta, rodada7, p)


def rodada7():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[6]
    parar = valor[5]
    errar = valor[4]
    p = 6

    pergunta = lista2[sorteio2[1]]
    resposta = pergunta[5]

    placar()
    som('audio/frase_20mil.mp3')
    perguntas(pergunta, resposta, rodada8, p)


def rodada8():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[7]
    parar = valor[6]
    errar = valor[5]
    p = 7

    pergunta = lista2[sorteio2[2]]
    resposta = pergunta[5]

    cabecalho(f' 8ª PERGUNTA, VALENDO {valor[7]} REAIS')
    placar()
    som('audio/frase_30mil.mp3')
    perguntas(pergunta, resposta, rodada9, p)


def rodada9():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[8]
    parar = valor[7]
    errar = valor[6]
    p = 8

    pergunta = lista2[sorteio2[3]]
    resposta = pergunta[5]

    cabecalho(f' 9ª PERGUNTA, VALENDO {valor[8]} REAIS')
    placar()
    som('audio/frase_40mil.mp3')
    perguntas(pergunta, resposta, rodada10, p)


def rodada10():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[9]
    parar = valor[8]
    errar = valor[7]
    p = 9

    pergunta = lista2[sorteio2[4]]
    resposta = pergunta[5]

    cabecalho(f' 10ª PERGUNTA, VALENDO {valor[9]} REAIS')
    placar()
    som('audio/frase_50mil.mp3')
    perguntas(pergunta, resposta, rodada11, p)


def rodada11():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[10]
    parar = valor[9]
    errar = valor[8]
    p = 10

    pergunta = lista3[sorteio3[0]]
    resposta = pergunta[5]

    cabecalho(f' 11ª PERGUNTA, VALENDO {valor[10]} REAIS')
    placar()
    som('audio/frase_100mil.mp3')
    perguntas(pergunta, resposta, rodada12, p)


def rodada12():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[11]
    parar = valor[10]
    errar = valor[9]
    p = 11

    pergunta = lista3[sorteio3[1]]
    resposta = pergunta[5]

    cabecalho(f' 12ª PERGUNTA, VALENDO {valor[11]} REAIS')
    placar()
    som('audio/frase_200mil.mp3')
    perguntas(pergunta, resposta, rodada13, p)


def rodada13():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[12]
    parar = valor[11]
    errar = valor[10]
    p = 12

    pergunta = lista3[sorteio3[2]]
    resposta = pergunta[5]

    cabecalho(f' 13ª PERGUNTA, VALENDO {valor[12]} REAIS')
    placar()
    som('audio/frase_300mil.mp3')
    perguntas(pergunta, resposta, rodada14, p)


def rodada14():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[13]
    parar = valor[12]
    errar = valor[11]
    p = 13

    pergunta = lista3[sorteio3[3]]
    resposta = pergunta[5]

    cabecalho(f' 14ª PERGUNTA, VALENDO {valor[13]} REAIS')
    placar()
    som('audio/frase_400mil.mp3')
    perguntas(pergunta, resposta, rodada15, p)


def rodada15():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[14]
    parar = valor[13]
    errar = valor[12]
    p = 14

    pergunta = lista3[sorteio3[4]]
    resposta = pergunta[5]

    cabecalho(f' 15ª PERGUNTA, VALENDO {valor[14]} REAIS')
    placar()
    som('audio/frase_500mil.mp3')
    perguntas(pergunta, resposta, rodada16, p)


def rodada16():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p, pulo, carta, convidado, colega
    acerto = valor[15]
    parar = errar = pulo = carta = convidado = colega = 0
    p = 15

    pergunta = lista4[sorteio4[0]]
    resposta = pergunta[5]

    cabecalho(f' PERGUNTA FINAL, VALENDO {valor[15]} REAIS')
    placar()
    som('audio/frase_final.mp3')
    perguntas(pergunta, resposta, final, p)


# ===================== FUNÇÕES DO JOGO ===============================================================================
def inicio():
    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq):
        criararquivo(arq)

    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura.mp3')
    pygame.mixer.music.play()
    layout()
    sleep(5)
    menu()


def cadastro_pergunta():
    global arq_pergunta
    cabecalho('CADASTRO DE PERGUNTAS')
    print(
        f'Para cadastrar uma pergunta, defina o nivel entra as opções {am}1{br} - {am}2{br} - {am}3{br} ou {am}4{br}'
        f'\nPara cadastrar perguntas da função pular escolha a opção {am}0{br}.')
    linha()
    while True:
        n = str(input('Qual o nível da pergunta? [0/1/2/3/4]: ')).lower().strip()
        linha()
        if n not in '01234':
            print(f'ERRO! Dados inválidos. Digite apenas {am}1{br} - {am}2{br} - {am}3{br} ou {am}4{br}!')
        else:
            arq_pergunta = f'pergunta_nivel{n}'
            break
        linha()

    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq_pergunta):
        criararquivo(arq_pergunta)
    else:
        #cadastro_pergunta()
        while True:
            pergunta = str(input('Qual a Pergunta: ')).upper().strip()
            a = str(input('Opção A: ')).upper().strip()
            b = str(input('Opção B: ')).upper().strip()
            c = str(input('Opção C: ')).upper().strip()
            d = str(input('Opção D: ')).upper().strip()
            linha()
            while True:
                resposta = str(input('Qual a resposta certa? [A/B/C/D]: ')).upper().strip()
                linha()
                if resposta not in 'ABCD':
                    erro('ERRO! Opção inválida, digite apenas A/B/C/D.')
                else:
                    try:
                        abrir = open(arq_pergunta, 'at')
                    except:
                        print('Houve um ERRO na abertura do arquivo!')
                    else:
                        try:
                            abrir.write(f'{pergunta};{a};{b};{c};{d};{resposta}\n')
                        except:
                            print(f'ERRO ao cadastrar a pergunta')
                        else:
                            abrir.close()
                    break
            print('Adicionando pergunta', end='')
            for c in range(1, 6):
                print('.', end='')
                sleep(.5)
            print(f'{am}concluido!{br}')
            linha()
            while True:
                resp = str(input('Cadastrar outra Pergunta? [S/N]: ')).upper().strip()[0]
                linha()
                if resp == 'S':
                    breakpoint(pergunta)
                elif resp == 'N':
                    menu()
                else:
                    print('ERRO! Dados inválidos, digite apenas S ou N.')




def cadastro():
    global nome
    som('audio/frase_participante.mp3')
    cabecalho('CADASTRO DO JOGADOR')
    nome = str(input('Nome do jogador: ')).title().strip()
    linha()
    print(f'{"Seja bem vindo(a) "f"{am}{nome}{br} começa agora o jogo "f"{am}SHOW DO MILHÃO!{br}"}')
    linha()
    while True:
        som('audio/frase_inicio.mp3')
        resp = str(input('VAMOS JOGAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp == 'S':
            rodada1()
        elif resp == 'N':
            cabecalho('MENU DO JOGO')
            menu()
        else:
            erro(f'ERRO! Dados inválidos. Digite apenas {am}S{br} ou {am}N{br}.')


def menu():
    print(f'{am}A) {br}COMEÇAR NOVO JOGO')
    print(f'{am}B) {br}RANKING DOS JOGADORES')
    print(f'{am}C) {br}CADASTRAR PERGUNTA')
    print(f'{am}D) {br}SAIR DO JOGO')
    linha()
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).strip().upper()[0]
        if resp == 'A':
            cadastro()
        elif resp == 'B':
            som('audio/frase_lombardi.mp3')
            ranking(arq)
        elif resp == 'C':
            som('audio/frase_lombardi.mp3')
            cadastro_pergunta()
        elif resp == 'D':
            sair()
        else:
            erro('ERRO! Dados inválidos, digite as opções do menu!')


def sair():
    som('audio/frase_tchau.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura_continuacao.mp3')
    pygame.mixer.music.play()
    linha()
    print('Saindo do jogo', end='')
    sleep(.5)
    for c in range(1, 12):
        print('.', end='')
        sleep(.5)
    # sleep(1)
    print(f'.....{am}Até a próxima!')
    exit()


def stop(arq, nome, premio):
    linha()
    while True:
        resp = str(input(f'VOCÊ QUER CONTINUAR? {am}[S/N]{br} ')).upper().strip()[0]
        linha()
        if resp == 'N':
            som('audio/frase_parar.mp3')
            resp2 = str(input(f'ESTÁ CERTO DISSO? {am}[S/N]{br}: ')).upper().strip()[0]
            linha()
            if resp2 == 'S':
                premio = parar
                final(arq, nome, premio)
        elif resp == 'S':
            break
        else:
            erro(f'ERRO! Dados inválidos, digite apenas {am}S{br} ou {am}N{br}!')


def final(arq, nome, premio):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        som('audio/frase_lombardi.mp3')
        cabecalho('RESULTADO DA PARTIDA')
        print(f'| {am}{"JOGADOR":^37}{br} | {am}{"PREMIAÇÃO":^36}{br} |')
        linha()
        print(f'| {nome:^37} | {premio:^36} |')
        linha()
        try:
            a.write(f'{nome};{premio}\n')
        except:
            print(f'ERRO ao cadastrar o jogador {nome}')
        else:
            # print(f'Novo registro de {nome} adicionado.')
            a.close()
            sair()


def ranking(arq):
    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura_continuacao.mp3')
    pygame.mixer.music.play()
    try:
        abrir = open(arq, 'rt')
    except:
        print(f'Houve um ERRO na abertura do aquivo!')
    else:
        cabecalho('HANKING DOS JOGADORES')
        print(f'| {am}{"JOGADOR":^37}{br} | {am}{"PREMIAÇÃO":^36}{br} |')
        linha()
        for dados in abrir:
            dado = dados.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'| {dado[0]:^37} | {dado[1]:^36} |')
            linha()
            sleep(.5)
    finally:
        #abrir.close()
        menu()


# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    print(br)
    linha('=')
    print(f'|{am + "JOGO SHOW DO MILHÃO - V2.0".center(98) + br}|')
    linha('=')
    print(f'|               {am}{"BEM VINDO AO"} {br}{"JOGO SHOW DO MILHÃO"} {am}{" - DESENVOLVIDO POR "}  '
          f'{br}{"DARLAN ARAUJO"}               |')
    linha('=')
    print(f'|              {az}{"Acerte as perguntas e concorra ao premio de"} {vm}{"R$ 1.000,000,00"} '
          f'{az}{"de reais"}{br}                |')
    linha('=')


def placar():
    print(f'|  {am}{"  AJUDAS DO JOGO >>>  "}{br} |  {"PULAR: "}  {am}{pulo}{br}   |  {"CARTAS: "}  {am}{carta}{br}   |'
          f'  {"CONVIDADOS: "}  {am}{convidado}{br}   |  {"COLEGAS: "}  {am}{colega}{br}    |')
    linha('=')
    print(f'| {am}{"PLACAR >>>"}{br} | {"ERRAR:"} {vm}{errar:<17}{br} |'
          f' {"PARAR:"} {rx}{parar:<19}{br} | {"ACERTO:"} {am}{acerto:<19}{br} |')
    linha('=')


def cabecalho(msg):
    print(br)
    linha('=')
    print(f'|{am}{msg.center(98)}{br}|')
    linha('=')


def som(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass


def linha(caractere='-', tam=100):
    print(caractere * tam)


def erro(msg):
    linha()
    print(f'{vm}{msg}{br}')
    linha()


def tempo():
    temp = 'on'
    print('TEMPO: ', end='')
    for c in range(1, 31):
        print(f'{c}', end=' ')
        sleep(1)
    temp = 'off'

    if temp == 'off':
        som('audio/frase_acabou_tempo.mp3')
        print('Que pena seu tempo acabou')
        final(arq, nome, premio)


# ===================== CRIAÇÃO DO ARQUIVO PARA SALVAR DADOS ==========================================================
def criararquivo(arq):
    # Função que cria o arquivo (banco de dados) caso não exista.
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def arquivoexiste(arq):
    # Função que verifica se o arquivo (banco de dados) existe.
    try:
        a = open(arq, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


# ===================== INÍCIO DO PROGRAMA ============================================================================
inicio()
