# Converte metros para centímetros

valor_em_metros = float(
    input("Digite o valor em metros que você quer converter para centímetros: ")
)
valor_em_centimetros = valor_em_metros * 100
print(
    "{:.2f} metros equivale a {:.2f} centímetros".format(
        valor_em_metros, valor_em_centimetros
    )
)
