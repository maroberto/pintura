from decimal import Decimal

altura = float(input('Digite a altura do comodo: '))
comprimento = float(input('Digite o comprimento do comodo: '))
quantos_comodos = float(input('Quantos comodos tem? '))
preco_metro = float(input('Qual valor do metro quadrado de pintura?'))

parede = (altura * comprimento)
tamanho_do_comodo = (parede) * 4
casa = (comprimento * comprimento * quantos_comodos) + (tamanho_do_comodo * quantos_comodos)
orcamento = (casa * preco_metro)

print('Cada parede tem {} e o comodo tem {}'.format(parede, tamanho_do_comodo))
print('Uma casa com quarto, sala e cozinha nesse padrão de medidas tem: {} metros quadrados para pintura'.format(casa))
print('O orçamento para esse serviço é R$ {}'.format(orcamento))







