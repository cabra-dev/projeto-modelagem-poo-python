def verificar_conflito(reservas, nova_reserva):
    for r in reservas:
        if r.sala.numero == nova_reserva.sala.numero and r.data == nova_reserva.data:

            # verifica sobreposição de horário
            if not (nova_reserva.fim <= r.inicio or nova_reserva.inicio >= r.fim):
                return True
    return False


def salas_disponiveis(reservas, salas, data, inicio, fim):
    livres = []

    for sala in salas:
        conflito = False

        for r in reservas:
            if r.sala.numero == sala.numero and r.data == data:
                if not (fim <= r.inicio or inicio >= r.fim):
                    conflito = True
                    break

        if not conflito:
            livres.append(sala)

    return livres