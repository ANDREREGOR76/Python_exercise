'''
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.
'''

tamanho = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
cobertura = 6
lata = 18
preco_lata = 80.00
galao = 3.6
preco_galao = 25.00
litros_tinta = tamanho / cobertura
litros_tinta *= 0.1

embalagem = input('Gostaria de levar a tinta em lata(L), galão(G) ou misto(M)? ')
embalagem = embalagem.lower()

qtd_latas = 0
qtd_galoes = 0

if embalagem == 'l':
    if litros_tinta < lata:
        qtd_latas = 1
    elif litros_tinta % lata == 0:
        qtd_latas = int(litros_tinta / lata)
    else:
        qtd_latas = int(litros_tinta / lata) + 1

    print(f'{qtd_latas} latas!')


elif embalagem == 'g':
    if litros_tinta < galao:
        qtd_galoes = 1
    elif litros_tinta % galao == 0:
        qtd_galoes = int(litros_tinta / galao)
    else:
        qtd_galoes = int(litros_tinta / galao) + 1
    print(f'{qtd_galoes} galões!')

else:
    qtd_latas = int(litros_tinta / lata)
    sobra = 40 % lata
    if sobra < galao:
        qtd_galoes = 1
    elif sobra % galao == 0:
        qtd_galoes = int(sobra / galao)
    else:
        qtd_galoes = int(sobra / galao) + 1
    print(qtd_latas)
    print(qtd_galoes)
