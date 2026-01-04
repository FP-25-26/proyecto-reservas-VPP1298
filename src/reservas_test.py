from reservas import *

def test_lee_reservas(ruta_fichero: str):
    reservas = lee_reservas(ruta_fichero)
    print("Total reservas: " + str(len(reservas)))
    print("Las tres primeras: ")
    for i in reservas[0:3]:
        print(i)

def test_total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> None:
    print("Test total_facturado")
    print(f"De {fecha_ini} a {fecha_fin}: {total_facturado(reservas, fecha_ini, fecha_fin)}")

def test_reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> None:
    print("Test reservas_mas_largas")
    print(f"Con n = {n}: {reservas_mas_largas(reservas, n)}")

def test_cliente_mayor_facturacion(reservas: list[Reserva], 
                              servicios: set[str] | None = None) -> None:
    print("Test cliente_mayor_facturacion")
    print(f"Servicios: {servicios} -> {cliente_mayor_facturacion(reservas, servicios)}")

def test_servicios_estrella_por_mes(reservas: list[Reserva], 
                               tipos_habitacion: set[str] | None = None
                               ) -> None:
    print("Test servicios_estrella_por_mes")
    print(f"Para {tipos_habitacion}: {sorted(servicios_estrella_por_mes(reservas, tipos_habitacion).items())}")

def test_media_dias_entre_reservas(reservas: list[Reserva]) -> None:
    print("Test media_dias_entre_reservas\n", media_dias_entre_reservas(reservas))

def test_cliente_reservas_mas_seguidas(reservas: list[Reserva], min_reservas: int) -> None:
    print("Test cliente_reservas_mas_seguidas")
    print(cliente_reservas_mas_seguidas(reservas, min_reservas))

if __name__ == "__main__":
    reservas = lee_reservas("data/reservas.csv")
    #test_lee_reservas("data/reservas.csv")
    #test_total_facturado(reservas)
    #test_total_facturado(reservas, datetime.strptime("2022-02-01", '%Y-%m-%d').date(), datetime.strptime("2022-02-28", '%Y-%m-%d').date())
    #test_total_facturado(reservas, datetime.strptime("2022-02-01", '%Y-%m-%d').date())
    #test_total_facturado(reservas, fecha_fin=datetime.strptime("2022-02-28", '%Y-%m-%d').date())
    #test_reservas_mas_largas(reservas)
    #test_cliente_mayor_facturacion(reservas)
    #test_cliente_mayor_facturacion(reservas, {"Parking"})
    #test_cliente_mayor_facturacion(reservas, {"Parking", "Spa"})
    #test_servicios_estrella_por_mes(reservas)
    #test_servicios_estrella_por_mes(reservas, {'Familiar', 'Deluxe'})
    #test_media_dias_entre_reservas(reservas)
    test_cliente_reservas_mas_seguidas(reservas, 5)
