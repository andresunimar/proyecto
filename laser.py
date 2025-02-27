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

def comprar_boleto():
    global total_boletos, ingresos_primera, ingresos_segunda, ingresos_tercera
    global ingresos_nacional, ingresos_internacional, ingresos_ruta_caracas_porlamar
    global ingresos_ruta_porlamar_caracas, servicios_adicionales
    
    num_boletos = int(input("Ingrese el número de boletos a comprar: "))
    for _ in range(num_boletos):
        nombre = input("Nombre del pasajero: ")
        cedula_tipo = input("Seleccione tipo de cédula (V/E): ")
        cedula_numero = input("Ingrese número de cédula: ")
        edad = int(input("Edad del pasajero: "))
        
        if edad < 18:
            print("Solo se venden boletos a mayores de 18 años.")
            continue
        
        clase = input("Seleccione la clase (Primera Clase, Segunda Clase, Tercera Clase): ")
        if clase == "Primera":
            precio = precio_primera
        elif clase == "Segunda":
            precio = precio_segunda
        elif clase == "Tercera":
            if edad >= 60:
                print("Los boletos de tercera clase no están disponibles para mayores de 60 años.")
                continue
            precio = precio_tercera
        else:
            print("Clase no válida.")
            continue
        
        tipo = input("Tipo de boleto (N para Nacional, I para Internacional): ")
        if tipo.upper() == "N":
            tipo = "Nacional"
        else:
            tipo = "Internacional"
        
        ruta = input("Ingrese la ruta de viaje (ejemplo: Caracas - Porlamar): ")
        
        if edad < 12 or edad >= 60:
            precio *= 0.9  # Aplicar descuento del 10%
        
        adicional = input("¿Requiere servicios adicionales? (S/N): ")
        if adicional.upper() == "S":
            servicios_adicionales += 1
        
        total_boletos += 1
        if clase == "Primera":
            ingresos_primera += precio
        elif clase == "Segunda":
            ingresos_segunda += precio
        elif clase == "Tercera":
            ingresos_tercera += precio
        
        if tipo == "Nacional":
            ingresos_nacional += precio
        else:
            ingresos_internacional += precio
        
        if ruta == "Caracas - Porlamar":
            ingresos_ruta_caracas_porlamar += precio
        elif ruta == "Porlamar - Caracas":
            ingresos_ruta_porlamar_caracas += precio
        
        print(f"Boleto comprado con éxito. Total a pagar: ${precio:.2f}")

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

