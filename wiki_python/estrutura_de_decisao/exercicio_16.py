# Pede o tamanho em metros quadrados da área a ser pintada e informa ao
# usuário a quantidade de latas de tinta a serem compradas e o preço total.
# A cobertura da tinta é de 1 litro para cada 3 metros quadrados e a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00.

tamanho = float(input('Digite o tamanho da área a ser pintada: '))
lata = 18
cobertura = 3
preco_lata = 80
litros_tinta = tamanho / cobertura
qtd_latas = 0

if litros_tinta % lata == 0:
    qtd_latas = int(litros_tinta / lata)
    print(qtd_latas)
else:
    qtd_latas = int(litros_tinta / lata) + 1
    print(qtd_latas)
