import re

formula = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = remove_caracters(cnpj)

    try:
        if invalida_sequencias(cnpj):
            # print('É UMA SEQUENCIA')
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = formula[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = formula
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        # print(cnpj[indice], regressivo)
        total += int(cnpj[indice]) * regressivo
    # print(total)

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    # print(digito)

    return f'{novo_cnpj}{digito}'


def invalida_sequencias(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def remove_caracters(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
    # cnpj = cnpj.replace('/', '')
    # cnpj = cnpj.replace('.', '')
    # cnpj = cnpj.replace('_', '')
    # return cnpj
