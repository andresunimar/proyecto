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

