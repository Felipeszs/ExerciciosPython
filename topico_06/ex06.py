# Exercício 1: Agrupamento de Dados (Dicionários e Listas)
# Você recebeu uma lista de dicionários representando produtos em um e-commerce. Cada dicionário contém o nome do produto, a categoria e o preço.

# Dado:
produtos = [
    {'nome': 'Laptop', 'categoria': 'Eletrônicos', 'preco': 4500},
    {'nome': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 150},
    {'nome': 'Cadeira Gamer', 'categoria': 'Móveis', 'preco': 1200},
    {'nome': 'Smartphone', 'categoria': 'Eletrônicos', 'preco': 2800},
    {'nome': 'Mesa de Escritório', 'categoria': 'Móveis', 'preco': 800},
    {'nome': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 300},
]

# O que fazer: Crie uma função que agrupe esses produtos por categoria. A função deve retornar um dicionário onde cada chave é uma categoria e o valor é uma lista de dicionários contendo apenas os produtos daquela categoria.

# Exercício 1: Agrupamento de Dados (Dicionários e Listas)


def agrupar_por_categoria(lista_produtos):
    agrupados = {} 

    for dicionario in lista_produtos:
        categoria = dicionario['categoria']  

        if categoria not in agrupados:
            agrupados[categoria] = []  

        agrupados[categoria].append(dicionario)  

    return agrupados
    

resultado = agrupar_por_categoria(produtos)
print(resultado)