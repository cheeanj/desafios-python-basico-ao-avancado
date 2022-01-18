"""
* Criar varíaveis para nome (str, idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando f-strings (com as chaves)
"""

nome = 'Carlos Jean'
idade = 28
altura = 1.69
peso = 66.5
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos,{altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {nascimento}.")
