from decimal import Decimal

def calcular_media(consumos):
    if not consumos:
        return 0
    return sum(consumos) / len(consumos)

def maior_consumo(consumos):
    return max(consumos) if consumos else 0

def menor_consumo(consumos):
    return min(consumos) if consumos else 0