# Marcas de portero automático convencional, en el orden del menú.
MARCAS = {
    "Tegui": "1-2-3-4-5",
    "Fermax": "4-3-1-2-6",
    "Golmar": "0-3-P1-5-10",
    "Alcad": "6-2-1-3-4",
    "Auta": "12-4-10-3-7",
    "Guinaz": "P-5-8-6-7",
    "Fringe": "4-1-2-3-6",
    "Bticino": "14-10-1-8-9",
    "Farfisa": "6-3-5-1-2",
    "Comelit": "1-4-P1-3-2",
}


def pedir_opcion(maximo):
    while True:
        try:
            opcion = int(input("Introduce el número:"))
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
            continue

        if 1 <= opcion <= maximo:
            return opcion

        print(f"Opción no válida. Elige un número entre 1 y {maximo}.")


def pedir_estado():
    while True:
        estado = input("¿Tu telefonillo es viejo o nuevo?").strip().lower()
        if estado in ("viejo", "nuevo"):
            return estado
        print("Respuesta no válida. Escribe 'viejo' o 'nuevo'.")


def seleccionar_marca(titulo):
    marcas = list(MARCAS)
    print(titulo)
    print()
    for numero, marca in enumerate(marcas, start=1):
        print(f"    {numero}){marca}")
    print()
    return marcas[pedir_opcion(len(marcas)) - 1]


def mostrar_equivalencias(marca_instalada, marca_nueva):
    titulo_instalado = f"Instalado: {marca_instalada}"
    titulo_nuevo = f"Nuevo: {marca_nueva}"
    bornes_instalados = MARCAS[marca_instalada].split("-")
    bornes_nuevos = MARCAS[marca_nueva].split("-")
    ancho_instalado = max(len(titulo_instalado), *(len(borne) for borne in bornes_instalados))
    ancho_nuevo = max(len(titulo_nuevo), *(len(borne) for borne in bornes_nuevos))

    print()
    print("Correspondencia de bornes")
    print(f"{titulo_instalado:<{ancho_instalado}} | {titulo_nuevo:<{ancho_nuevo}}")
    print(f"{'-' * ancho_instalado}-+-{'-' * ancho_nuevo}")
    for instalado, nuevo in zip(bornes_instalados, bornes_nuevos):
        print(f"{instalado:<{ancho_instalado}} → {nuevo:<{ancho_nuevo}}")


def mostrar_presentacion():
    print(r"""
       __________________        _________
      |                  |      /  _____  \
      |   .----------.   |     |  |     |  |
      |   |  SOPORTE |   |     |  |_____|  |
      |   '----------'   |     |           |
      |                  |      \         /
      |     [ ABRIR ]    |       |       |
      |                  |       |       |
      |      o o o       |      /         \
      |      o o o       |     |   . . .   |
      |__________________|     |   . . .   |
               |                \_________/
               |                     |
               |                     |
               \_/\_/\_/\_/\_/\_/\_/

              SwapBellCLI · V 0.2
       Equivalencias de telefonillos 4+n
                    EYIlabs
""")


def main():
    mostrar_presentacion()
    if pedir_estado() == "nuevo":
        print("Revise las conexiones, por favor")
        return

    print()
    marca_instalada = seleccionar_marca("Elige la marca del telefono instalado")
    marca_nueva = seleccionar_marca("Elige la marca del telefono a instalar")

    mostrar_equivalencias(marca_instalada, marca_nueva)
    print()
    print("¡¡No olvides revisar!!")
    print("el tipo de llamada y las masas")


if __name__ == "__main__":
    main()
