"""
04,252,011/0001-10 40,688,134/0001-61 71,506,168/0001-11 12,544,992/0001-05
0 4  2 5  2  0 1 1 0 0 0 1   x   x
5 4  3 2  9  8 7 6 5 4 3 2
0 16 6 10 18 0 7 6 0 0 0 2 = 65 ##
fórmula -> 11 - (65 % 11) = 1
primeiro digito = 1

0 4  2 5  2 0 1 1 0 0 0 1 1   x
6 5  4 3  2 9 8 7 6 5 4 3 2
0 20 8 15 4 0 8 7 0 0 0 3 2 = 67 ##
fórmula -> 11 - (65 % 11) = 1 (Como o resultado é maior que 0, então é 0)
primeiro digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito


"""
import cnpj
import geradorCNPJ


# cnpj1 = '12,544,992/0001-05'
# cnpj.valida(cnpj1)
#
# if cnpj.valida(cnpj1):
#     print(f'{cnpj1} é válido')
# else:
#     print(f'{cnpj1} é inválido')

print(geradorCNPJ.formata('82158974000162'))

novo = geradorCNPJ.gera()
formatado = geradorCNPJ.formata(novo)
print(formatado)

for i in range(5):
    novos_cnpj = geradorCNPJ.gera()
    formatados = geradorCNPJ.formata(novos_cnpj)
    print(formatados)
