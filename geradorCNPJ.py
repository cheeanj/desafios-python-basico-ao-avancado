from random import randint
from cnpj import calcula_digito, remove_caracters


def gera():
    primeiro_bloco = randint(10, 99)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = '0001'

    # inicio_cnpj = ''.join((primeiro_bloco, segundo_bloco, terceiro_bloco, quarto_bloco), '.')
    inicio_cnpj = f'{primeiro_bloco}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = calcula_digito(cnpj=inicio_cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)

    return novo_cnpj


def formata(cnpj):
    cnpj = remove_caracters(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
