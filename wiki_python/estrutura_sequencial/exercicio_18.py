"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link.
"""

tamanho = int(input("Digite o tamanho do arquivo para download (MB): "))
velocidade = int(input("Digite a velocidade de download (Mbps): "))
tempo_de_download = (tamanho / velocidade) / 60
print(tempo_de_download)
