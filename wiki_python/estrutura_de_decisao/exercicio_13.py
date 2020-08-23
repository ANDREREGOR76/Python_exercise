altura = float(input('Digite sua altura: '))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print()
print('Se você for homem, seu peso ideal é {:.2f} Kg.\n'.format(
    peso_ideal_homem))

print('Agora, se você for mulher, seu peso ideal é {:.2f} Kg.\n'.format(
    peso_ideal_mulher))
