def resumo_comanda(comanda):
    dados = []
    for item in comanda.itens:
        dados.append({
            "produto": item.produto.nome,
            "qtd": item.quantidade,
            "subtotal": item.get_subtotal()
        })
    return dados