"""
Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o imc da pessoa com duas casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Junio'
idade = 32
peso = 140
altura = 1.88
ano_atual = 2022
imc = peso/(altura**2)
ano_de_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, pesa {peso}Kg, tem um IMC de {imc:.2f} e nasceu no ano de {ano_de_nascimento}')
