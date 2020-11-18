arq_pergunta = 'pergunta_nivel1'

nivel = arq_pergunta

def rodada1():
    global arq_pergunta, nivel
    arq_pergunta = 'pergunta_nivel2'
    nivel = arq_pergunta

    return nivel


print(nivel)
rodada1()