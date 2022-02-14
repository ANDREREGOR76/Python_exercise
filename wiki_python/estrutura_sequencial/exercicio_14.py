# ler a variável 'peso' (peso de peixes) e calcule o excesso (acima de 50 kg). Grava na variável 'excesso' a quantidade de quilos além do limite e na variável 'multa' o valor da multa devida. Imprime os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso de peixes pescados: "))
excesso = peso - 50
multa = excesso * 4.00
print()
if peso <= 50:
    print("Parabéns! Você pescou {:.2f} quilos de peixe!".format(peso))
else:
    print(
        "Parabéns, você pescou{: .2f} quilos de peixe!\nPorém, como você pescou{: .2f} quilos além do limite, você terá que pagar uma multa no valor de R${: .2f}.".format(
            peso, excesso, multa
        )
    )
