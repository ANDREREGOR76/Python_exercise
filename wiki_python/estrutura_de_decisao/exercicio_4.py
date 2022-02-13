"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input("Digite uma letra: ").lower()
valor = "consoante"
if letra in "aeiou":
    valor = "vogal"

print(f"A letra digitada é uma {valor}.")
