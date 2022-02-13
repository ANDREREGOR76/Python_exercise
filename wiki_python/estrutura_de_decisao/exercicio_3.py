"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""


inicial_sexo = input(
    "Digite 'F' para 'feminino' ou 'M' para 'masculino': "
).capitalize()
sexo = "Sexo Inválido"

if inicial_sexo == "M":
    sexo = "M - Masculino"
elif inicial_sexo == "F":
    sexo = "F - Feminino"

print(sexo)
