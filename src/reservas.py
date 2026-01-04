from typing import NamedTuple
from datetime import *
import csv
from collections import defaultdict
from collections import Counter

Reserva = NamedTuple("Reserva", 
                     [("nombre", str),
                      ("dni", str),
                      ("fecha_entrada", date),
                      ("fecha_salida", date),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str])
                    ])

def lee_reservas(ruta_fichero: str) -> list[Reserva]:
    reservas = []
    with open(ruta_fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
            fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d').date()
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales = servicios_adicionales.split(",")
            reserva = Reserva(nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales)
            reservas.append(reserva)
    return reservas

def total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> float:
    total = 0.0
    for r in reservas:
        if (
            (fecha_ini is None or r.fecha_entrada >= fecha_ini)
            and
            (fecha_fin is None or r.fecha_entrada <= fecha_fin)
        ):
            total += r.precio_noche * ((r.fecha_salida - r.fecha_entrada).days)
    return total

def reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> list[tuple[str, date]]:
    lista = []
    for r in reservas:
        lista.append((r.nombre, r.fecha_entrada, r.fecha_salida))
    return [(a, b) for a, b, _ in sorted(lista, reverse=True, key=lambda x:(x[2] - x[1]).days)[:n]]

def cliente_mayor_facturacion(reservas: list[Reserva], 
                              servicios: set[str] | None = None) -> tuple[str, float]:
    diccionario_clientes = defaultdict(float)
    for r in reservas:
        if (servicios != None and servicios & set(r.servicios_adicionales)) or servicios == None:
            diccionario_clientes[r.dni] += r.precio_noche * ((r.fecha_salida - r.fecha_entrada).days)
    return max(diccionario_clientes.items(), key=lambda x:x[1])

def servicios_estrella_por_mes(reservas: list[Reserva], 
                               tipos_habitacion: set[str] | None = None
                               ) -> dict[str, str]:
    diccionario_meses = defaultdict(list)
    for r in reservas:
        if tipos_habitacion is None or r.tipo_habitacion in tipos_habitacion:
            diccionario_meses[r.fecha_entrada.month] += r.servicios_adicionales
    return {e: max(Counter(n).items(), key=lambda x:x[1])[0] for e, n in diccionario_meses.items()}

def media_dias_entre_reservas(reservas: list[Reserva]) -> float:
    diferencias = []
    reservas.sort(key=lambda x:x.fecha_entrada)
    for r1, r2 in zip(reservas, reservas[1:]):
        dias = (r2.fecha_entrada - r1.fecha_entrada).days
        diferencias.append(dias)
    return sum(diferencias)/len(diferencias)

def cliente_reservas_mas_seguidas(reservas: list[Reserva], min_reservas: int) -> str:
    diccionario_clientes = defaultdict(list)
    for r in reservas:
        diccionario_clientes[r.dni].append(r)
    diccionario_medias = {e: media_dias_entre_reservas(res) for e, res in diccionario_clientes.items() if len(diccionario_clientes.items()) >= min_reservas}
    dni, media = min(diccionario_medias.items(), key=lambda x:x[1])
    return f"El DNI del cliente con al menos {min_reservas} reservas y menor media de días entre reservas consecutivas es {dni}, con una media de días entre reservas de {media}."