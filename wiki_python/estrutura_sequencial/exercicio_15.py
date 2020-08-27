# Pergunta quanto o usuário ganha por hora e o número de horas que ele trabalhou no mês.
# Calcula e mostra o total do salário dele no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.
# Mostra: a. salário bruto; b. quanto pagou ao INSS; c. quanto pagou ao sindicato; d. o salário líquido; e
# e. calcula os descontos e o salário líquido


ganho_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = int(
    input('Digite a quantidade de horas que você trabalhou: '))
sal_bruto = ganho_hora * horas_trabalhadas
imp_renda = sal_bruto * (11/100)
inss = sal_bruto * (8/100)
sindicato = sal_bruto * (5/100)
sal_liq = sal_bruto - (imp_renda + inss + sindicato)

print('+ Salário Bruto: R${:.2f}'.format(sal_bruto))
print('- IR (11%): R${:.2f}'.format(imp_renda))
print('- INSS (8%): R${:.2f}'.format(inss))
print('- Sindicato (5%): R${:.2f}'.format(sindicato))
print('= Salário Líquido: R${:.2f}'.format(sal_liq))
