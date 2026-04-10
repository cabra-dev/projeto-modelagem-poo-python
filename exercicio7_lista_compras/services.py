def resumo_lista(lista):
    dados = []
    for item in lista.itens:
        dados.append({
            "produto": item.produto.nome,
            "previsto": item.total_previsto(),
            "real": item.total_real()
        })
    return dados