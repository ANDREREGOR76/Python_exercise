# Solicita a temperatura em graus Celsius
# tranforma e mostra em graus Farenheit

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_farenheit = (temp_celsius * 9 / 5) + 32
print("A temperatura em graus Farenheit é de {:.2f}° F.".format(temp_farenheit))
