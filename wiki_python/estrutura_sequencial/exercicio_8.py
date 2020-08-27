# Calcula e mostra o total do salário do usuário com
# base no valor que ele informa ganhar por hora e o número
# de horas trabalhadas no mês

valor_hora = float(input('Digite quanto você ganha por hora trabalhada: '))
quant_horas = float(input('Digite quantas horas você trabalhou no mês: '))
salario = quant_horas * valor_hora
print('O total do seu salário no mês foi de R$ {:.2f}.'.format(salario))
