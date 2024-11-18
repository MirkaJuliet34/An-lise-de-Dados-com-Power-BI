""" 
Você deve desenvolver um programa que analise a produção de celulose em diferentes regiões. O programa receberá dados sobre a quantidade de celulose produzida em toneladas por região e calculará a produção total, assim como a média de produção por região. Os dados devem ser fornecidos no formato "Região: Produção".

Entrada
O usuário deve inserir as produções no formato "Região: Produção" (ex: "Norte: 150.5"), separando cada entrada por vírgula. O valor da produção deve ser um número real representando a quantidade em toneladas.

Saída
O programa deve exibir a produção total e a média de produção por região, formatadas em duas linhas. A produção total e a média devem ser apresentadas com duas casas decimais.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Norte: 150.5, Sul: 200.0, Leste: 175.8, Oeste: 160.2	Produção total: 686.50 toneladas
Média por região: 171.62 toneladas
Nordeste: 300.0, Sudeste: 500.5, Centro-Oeste: 250.2	Produção total: 1050.70 toneladas
Média por região: 350.23 toneladas
Norte: 100.5, Sul: 150.0, Leste: 175.5	Produção total: 426.00 toneladas  
Média por região: 142.00 toneladas
"""

def calcular_producao():
    # Entrada de dados do usuário
    entrada = input()

    # Separando as entradas de cada região e produção
    regioes_producao = entrada.split(',')

    # Variáveis para armazenar a produção total e o número de regiões
    total_producao = 0.0
    numero_regioes = 0

    # Iterando sobre cada entrada de região: produção
    for regiao in regioes_producao:
        # Dividindo a região e produção com base no caractere ":"
        nome_regiao, producao = regiao.split(':')
        
        # Convertendo a produção para float e somando ao total
        producao = float(producao.strip())
        total_producao += producao
        numero_regioes += 1

    # Calculando a média de produção por região
    media_producao = total_producao / numero_regioes

    # Exibindo a produção total e média formatada
    print(f"Produção total: {total_producao:.2f} toneladas")
    print(f"Média por região: {media_producao:.2f} toneladas")

# Executa a função
calcular_producao()
