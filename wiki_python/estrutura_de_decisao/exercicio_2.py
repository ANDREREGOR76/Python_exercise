"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

numero = int(input("Digite um número: "))
valor = "positivo"
if numero < 0:
    valor = "negativo"

print(f"O número {numero} é {valor}")
