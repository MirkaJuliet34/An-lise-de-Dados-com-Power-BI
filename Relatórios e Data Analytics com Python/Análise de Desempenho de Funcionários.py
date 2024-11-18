""" 
A avaliação de desempenho é uma prática comum em empresas que ajuda a identificar os pontos fortes e fracos de cada funcionário. Neste desafio, você deve criar um programa que analisa as pontuações em avaliações de funcionários e os classifica em categorias de desempenho. O objetivo é facilitar a identificação de talentos e áreas de melhoria dentro da equipe.

Detalhes da Classificação:

Você deve classificar os funcionários com base em suas pontuações em três categorias:

Excelente: para pontuações acima de 90.
Bom: para pontuações entre 75 e 90.
Regular: para pontuações abaixo de 75.
Entrada
O usuário fornecerá uma sequência de registros de funcionários no formato "Nome: Pontuação", onde "Nome" é o nome do funcionário e "Pontuação" é um número inteiro representando a pontuação obtida. Os registros estarão em uma única linha, separados por vírgula. Por exemplo: João: 85, Maria: 92, Pedro: 78.

Saída
A saída deve ser uma lista que contém o nome do funcionário e sua respectiva categoria de desempenho.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
João: 85, Maria: 92, Pedro: 78	João: Bom
Maria: Excelente
Pedro: Bom
Ana: 65, Lucas: 88, Beatriz: 95	Ana: Regular
Lucas: Bom
Beatriz: Excelente
Ricardo: 70, Sofia: 90, Carla: 80	Ricardo: Regular
Sofia: Bom
Carla: Bom
"""

def analisar_desempenho_funcionarios():
    # Entrada de dados
    registros = input()
    desempenho = []

    # Processamento dos dados
    for registro in registros.split(', '):
        nome, pontuacao = registro.split(': ')
        pontuacao = int(pontuacao)

        # Implementação da classificação de desempenho
        if pontuacao > 90:
            categoria = "Excelente"
        elif 75 <= pontuacao <= 90:
            categoria = "Bom"
        else:
            categoria = "Regular"
        
        # Armazenar o resultado formatado
        desempenho.append(f"{nome}: {categoria}")

    # Exibição da saída
    for resultado in desempenho:
        print(resultado)

# Chama a função
analisar_desempenho_funcionarios()
