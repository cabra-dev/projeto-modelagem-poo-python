def agrupar_por_categoria(controle):
    resultado = {}
    for gasto in controle.gastos:
        cat = gasto.categoria.value
        resultado[cat] = resultado.get(cat, 0) + gasto.valor
    return resultado


def agrupar_por_pagamento(controle):
    resultado = {}
    for gasto in controle.gastos:
        pag = gasto.pagamento.value
        resultado[pag] = resultado.get(pag, 0) + gasto.valor
    return resultado