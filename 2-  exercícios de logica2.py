"""
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
"""

num_int = input("Digite um numero: ")


# try:
#     num_int = int(num_int)
#     if num_int % 2 == 0:
#         print("Numero par")
#     else:
#         print("Numero ímpar")
# except:
#     print("O valor digitado não é um número inteiro")

if num_int.isdigit():
    num_int = int(num_int)

    if num_int % 2 == 0:
        print(f"{num_int} é par")
    else:
        print(f"{num_int} é ímpar")

else:
    print('Isso não é um número inteiro.')

"""
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? ')


# hora = int(hora)

# if hora >= 0 and hora <= 11:
#     print('Bom dia')
# elif hora >= 12 and hora <= 17:
#     print('Boa tarde')
# elif hora >= 18 and hora <= 23:
#     print('Boa noite')
# else:
#     print('Não existe essa hora')

# if hora.isdigit():
#     hora = int(hora)
#
#     if hora < 0 or hora > 23:
#         print("horário deve estar entre 0 e 23")
#     else:
#         if hora <= 11:
#             print('Bom dia!')
#         elif hora <= 17:
#             print('Boa tarde!')
#         else:
#             print('boa noite!')

try:
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    elif 18 <= hora <= 23:
        print('Boa noite')
    else:
        print('horário invalido')
except:
    print('Digite um horário entre 0-24')

"""
# Faça  um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "seu nome é normal", maior que 6 escreva "Seu nome é muito grande".
"""

qtd_letras = input('Digite seu primeiro nome: ')


# if qtd_letras.__len__() <= 4:
#     print("Seu nome é curto")
# elif qtd_letras.__len__() >= 6:
#     print("Seu nome é muito grande")
# else:
#     print("Seu nome é normal")


# if len(qtd_letras) <= 4:
#     print("Seu nome é curto")
# elif len(qtd_letras) >= 6:
#     print("Seu nome é muito grande")
# else:
#     print("Seu nome é normal")


tamanho = len(qtd_letras)

if tamanho <= 4:
    print('seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
