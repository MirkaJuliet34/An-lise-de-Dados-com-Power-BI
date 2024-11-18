"""
Neste desafio, você irá acumular os valores de venda ao longo dos meses, somando cada valor ao total anterior. Esse cálculo é essencial em relatórios de vendas, pois permite visualizar a tendência de crescimento ao longo do tempo. Imagine que você trabalha em uma equipe de vendas e precisa apresentar um relatório mensal; o total acumulado mostra não apenas quanto foi vendido em cada mês, mas também o desempenho geral da equipe.

Em um ambiente DAX (Data Analysis Expressions), utilizado em ferramentas como Power BI e Excel, funções como CALCULATE e FILTER são aplicadas para calcular o total acumulado de vendas. Ao simular esse cálculo em Python, você entenderá como essas operações são realizadas em uma plataforma de análise de dados.

Entrada
A entrada consiste em:

Um número inteiro n (1 ≤ n ≤ 12), representando a quantidade de meses.
Em seguida, serão fornecidos n pares de entradas, onde cada par consiste em:
Um string representando o nome do mês (por exemplo, "Janeiro", "Fevereiro", etc.).
Um número decimal representando o valor total de vendas desse mês (por exemplo, 5000.0).
Saída
A saída deve ser uma lista de strings, onde cada string corresponde a um mês e seu respectivo total acumulado de vendas.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
3      
Janeiro
5000
Fevereiro
11000
Março
18000	Janeiro: 5000.0   
Fevereiro: 16000.0
Março: 34000.0
3
Abril
1500
Maio
2500
Junho
3500	Abril: 1500.0
Maio: 4000.0
Junho: 7500.0
3
Julho
1000
Agosto
3000
Setembro
500	Julho: 1000.0
Agosto: 4000.0
Setembro: 4500.0
"""

def valor_acumulado_vendas(vendas_mensais):
    acumulado = 0
    vendas_acumuladas = []
    
    # Calcula o valor acumulado mês a mês
    for venda in vendas_mensais:
        acumulado += venda["valor_venda"]
        vendas_acumuladas.append(f"{venda['mes']}: {acumulado:.1f}")
    
    # Retorna a lista de vendas acumuladas
    return vendas_acumuladas

# Recebe a entrada do usuário
vendas_mensais = []
n = int(input())

for i in range(n):
    mes = input()
    valor_venda = float(input())
    vendas_mensais.append({"mes": mes, "valor_venda": valor_venda})

# Chama a função e imprime o resultado
resultado = valor_acumulado_vendas(vendas_mensais)
for linha in resultado:
    print(linha)
