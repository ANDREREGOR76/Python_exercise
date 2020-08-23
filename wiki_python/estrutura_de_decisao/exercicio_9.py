# Solicita ao usuário a temperatura em graus Farenheit, transforma
# e mostra a temperatura em graus Celsius

temp_farenheit = float(input('Qual a temperatura em Farenheit: '))
temp_celsius = 5 * ((temp_farenheit - 32) / 9)
print('A temperatura em Celsius é {:.2f}°.'.format(temp_celsius))
