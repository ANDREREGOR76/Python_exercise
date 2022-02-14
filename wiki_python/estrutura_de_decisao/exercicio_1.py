"""
Faça um Programa que peça dois números e imprima
o maior deles.
"""
num1 = input("Digite um número: ")
while not num1.isnumeric():
    print("Você tem que digitar um número!")
    num1 = input("Digite um número: ")

num2 = input("Digite outro número: ")
while not num2.isnumeric():
    print("Você tem que digitar um número!")
    num2 = input("Digite outro número: ")
num_1 = float(num1)
num_2 = float(num2)
if num_1 > num_2:
    print("{} é maior que {}!".format(num_1, num_2))
elif num_1 == num_2:
    print("{} e {} são iguais!".format(num_1, num_2))
else:
    print("{} é maior que {}!".format(num_2, num_1))
