from collections import Counter


def formatar_reais(var):
    var = f'R${var:_.2f}'
    var = var.replace('.', ',').replace('_', '.')
    return var


def media_aritmetica(lst):
    return sum(lst) / len(lst)


def listar_produtos(*listas):
    lista_produtos = []
    for lista in listas:
        for produto, estoque in lista:
            lista_produtos.append(produto)
    lista_produtos = set(lista_produtos)
    lista_produtos = list(lista_produtos)
    return lista_produtos


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {(proporcao * 100):.2f}%')
