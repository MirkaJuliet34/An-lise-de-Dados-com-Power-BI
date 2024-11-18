"""
Neste desafio, você será responsável por implementar um simulador de cálculo de salários para uma lista de funcionários. Cada funcionário tem um nome, o número de horas trabalhadas e o valor que ele recebe por hora. Sua tarefa é calcular o salário de cada funcionário multiplicando as horas trabalhadas pelo valor da hora.

Você receberá primeiro um número que indica a quantidade de funcionários, seguido por uma lista de dicionários contendo as informações de cada funcionário. A função deve retornar uma lista de strings, onde cada string apresenta o nome do funcionário seguido do seu salário calculado.

Entrada
A entrada será composta por:

Um número inteiro n que representa a quantidade de funcionários.
Uma lista de n dicionários. Cada dicionário conterá três chaves:
"nome": uma string representando o nome do funcionário.
"horas_trabalhadas": um número inteiro representando as horas que o funcionário trabalhou.
"valor_hora": um número decimal representando o valor pago por hora trabalhada.
Saída
A saída deverá ser uma lista de strings. Cada string deverá seguir o formato:

"Nome: Salário", onde:
Nome é o nome do funcionário.
Salário é o resultado do cálculo das horas trabalhadas multiplicadas pelo valor por hora, formatado com duas casas decimais.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2
Ana
40
25
Pedro
35
30	Ana: 1000.0
Pedro: 1050.0
1
Maria
45
20	Maria: 900.0
3
João
30
15
Luiza
25
18
Carlos
20
22	João: 450.0
Luiza: 450.0
Carlos: 440.0
"""

def calcular_salarios(funcionarios):
    salarios = []
    for funcionario in funcionarios:
        nome = funcionario["nome"]
        horas_trabalhadas = funcionario["horas_trabalhadas"]
        valor_hora = funcionario["valor_hora"]
        salario = horas_trabalhadas * valor_hora
        # Formatando com uma casa decimal
        salarios.append(f"{nome}: {salario:.1f}")
    return salarios

# Função para entrada do usuário
def main_salario():
    n = int(input())
    funcionarios = []

    for _ in range(n):
        nome = input()
        horas_trabalhadas = int(input())
        valor_hora = float(input())
        funcionarios.append({
            "nome": nome,
            "horas_trabalhadas": horas_trabalhadas,
            "valor_hora": valor_hora
        })

    resultado = calcular_salarios(funcionarios)
    
    for salario in resultado:
        print(salario)

# Executando a função
main_salario()
