# Solicita dois números inteiros e um número real.
# Calcula e mostra:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.
print()
print('=========================================')
int_um = int(input('Digite um número inteiro: '))
int_dois = int(input('Digite outro número inteiro: '))
num_real = float(input('Digite um número real: '))
print()
print(
    f'>>> O dobro do número {int_um} multiplicado pela metade do número {int_dois} é {(int_um * 2) * (int_dois / 2)}.')
print()
print('>>> A soma do triplo de {} com {:.2f} é {}'.format(
    int_um, num_real, ((int_um * 3) + num_real)))
print()
print('>>> O número {:.2f} elevado ao cubo é igual a {:.2f}'.format(
    num_real, (num_real ** 3)))
print()
