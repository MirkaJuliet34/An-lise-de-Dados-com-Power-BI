"""
Neste desafio, você vai simular a operação de uma consulta que filtra funcionários por cargo, semelhante ao comportamento de uma consulta SQL com a cláusula WHERE. O objetivo é filtrar uma lista de funcionários pelo cargo especificado e retornar os nomes daqueles que ocupam o cargo desejado.

Embora o SQL seja uma linguagem utilizada para consultas em bancos de dados, aqui estamos simulando uma operação similar em Python, filtrando uma lista de dicionários que contém as informações dos funcionários.

Entrada
Você receberá:

Um número inteiro n representando o número de funcionários.
Uma lista de dicionários, onde cada dicionário contém três chaves:
id: o identificador único do funcionário,
nome: o nome do funcionário,
cargo: o cargo ocupado pelo funcionário.
Uma string representando o cargo que você deseja filtrar.
Saída
Uma lista com os nomes dos funcionários que ocupam o cargo especificado.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
3
1
Ana
Desenvolvedora
2
Pedro
Gerente
3
Maria
Desenvolvedora
Desenvolvedora	['Ana', 'Maria']
2
4
João
Analista
5
Luiza
Analista
Analista	['João', 'Luiza']
2
6
Carlos
Gerente
7
Sofia
Diretora
Gerente	['Carlos']
"""

def filtrar_funcionarios(funcionarios, cargo):
    # Filtra os funcionários pelo cargo especificado e retorna uma lista com os nomes
    return [funcionario["nome"] for funcionario in funcionarios if funcionario["cargo"] == cargo]

# Função para entrada do usuário
def main_filtro():
    n = int(input())
    funcionarios = []

    for _ in range(n):
        id_funcionario = int(input())
        nome = input()
        cargo = input()
        funcionarios.append({"id": id_funcionario, "nome": nome, "cargo": cargo})

    cargo_filtro = input()
    resultado = filtrar_funcionarios(funcionarios, cargo_filtro)
    
    print(resultado)

# Executando a função
main_filtro()
