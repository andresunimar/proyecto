total_boletos = 0
ingresos_primera = 0
ingresos_segunda = 0
ingresos_tercera = 0
ingresos_nacional = 0
ingresos_internacional = 0
ingresos_ruta_caracas_porlamar = 0
ingresos_ruta_porlamar_caracas = 0
servicios_adicionales = 0
precio_primera = 200
precio_segunda = 150
precio_tercera = 100

def ver_sistema():
    print("\nREPORTE DE VENTAS")
    print(f"Total de boletos vendidos: {total_boletos}")
    print("Ingresos por clase:")
    print(f"  Primera Clase: ${ingresos_primera:.2f}")
    print(f"  Segunda Clase: ${ingresos_segunda:.2f}")
    print(f"  Tercera Clase: ${ingresos_tercera:.2f}")
    print("Ingresos por tipo de boleto:")
    print(f"  Nacional: ${ingresos_nacional:.2f}")
    print(f"  Internacional: ${ingresos_internacional:.2f}")
    print("Ingresos por ruta de viaje:")
    print(f"  Caracas - Porlamar: ${ingresos_ruta_caracas_porlamar:.2f}")
    print(f"  Porlamar - Caracas: ${ingresos_ruta_porlamar_caracas:.2f}")
    print(f"Número de servicios adicionales solicitados: {servicios_adicionales}")

def ejecutar():
    while True:
        print("\nMenú:")
        print("1. Comprar boleto")
        print("2. Ver sistema")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            comprar_boleto()
        elif opcion == "2":
            ver_sistema()
        elif opcion == "3":
            print("Gracias por usar el sistema de venta de boletos de LASER Airlines.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

ejecutar()

