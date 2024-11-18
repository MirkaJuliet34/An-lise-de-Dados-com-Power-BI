"""
Você deverá calcular o crescimento percentual entre dois meses consecutivos de vendas, um conceito essencial em análises financeiras. Esse cálculo permite visualizar a evolução das vendas ao longo do tempo. Para isso, você deverá comparar o valor total de vendas de dois meses consecutivos e determinar a variação percentual.

Para calcular o crescimento, subtraia o valor de vendas do mês anterior do valor de vendas do mês atual, depois divida essa diferença pelo valor de vendas do mês anterior e multiplique por 100 para obter a porcentagem de crescimento.

Entrada
Dois pares de entradas, cada um contendo o nome de um mês e o valor total de vendas desse mês (um número decimal).

Saída
O percentual de crescimento de vendas, com duas casas decimais.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Janeiro
5000
Fevereiro
6000	Crescimento percentual de vendas: 20.00%
Março
8000
Abril
10000	Crescimento percentual de vendas: 25.00%
Maio
7000
Junho
8400	Crescimento percentual de vendas: 20.00%
"""

def crescimento_percentual(vendas_mensais):
    # Extraia os valores de venda de dois meses consecutivos
    valor_venda_mes_anterior = vendas_mensais[0]["valor_venda"]
    valor_venda_mes_atual = vendas_mensais[1]["valor_venda"]
    
    # Calcule o crescimento percentual
    crescimento = ((valor_venda_mes_atual - valor_venda_mes_anterior) / valor_venda_mes_anterior) * 100
    return crescimento

# Lista para armazenar as vendas mensais
vendas_mensais = []

# Coleta de dados para dois meses consecutivos
for i in range(2):
    mes = input()
    valor_venda = float(input())
    vendas_mensais.append({"mes": mes, "valor_venda": valor_venda})

# Chama a função e imprime o resultado formatado com duas casas decimais
resultado = crescimento_percentual(vendas_mensais)
print(f"Crescimento percentual de vendas: {resultado:.2f}%")
