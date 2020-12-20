cp = float(input('Digite o comprimento do piso: '))
lp = float(input('Digite a Largura do piso: '))
vp = float(input('Digite o valor do piso R$: '))
piso = cp * lp
valor = piso * vp


cpa = float(input('Digite o comprimento da parede: '))
lpa = float(input('Digite a altura da parede: '))
vpa = float(input('Digite o valor do revestimento R$: '))
parede = cpa * lpa
valorpa = parede * vpa

valor_argamassa = float(input('Digite o valor do argamassa R$: '))

totalm = piso + parede
argamassa = totalm / 4
total_argamassa = argamassa * valor_argamassa
total_geral = totalm + valor + valorpa



print('O tamanho do piso em M2 é: {} e o valor é R$: {} ' .format(piso, valor))

print('O tamanho da parede em m2 é: {:.2f} e o valor do revestimento é R$: {:.2f}'.format(parede, valorpa))

print('O valor da argamassa é R$: {:.2f} e o total geral é {:.2f} '.format(total_argamassa, total_geral))

# Piso Banheiro 2.00 * 1.30
# Piso da cozinha 2.00 * 3.00
# total 4.00 * 4.50
# Parede do banheiro 5.30
# Parede cozinha 9.00
# total 14.50 * 2.40
# argamassa 18,90 cobre 4m2