# Solicita as 4 notas bimestrais e mostra a média

nota_1 = float(input('Informe a nota do primeiro bimestre: '))
nota_2 = float(input('Informe a nota do segundo bimestre: '))
nota_3 = float(input('Informe a nota do terceiro bimestre: '))
nota_4 = float(input('Informe a nota do quarto bimestre: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print('A média das notas informadas é {:.2f}!'.format(media))
