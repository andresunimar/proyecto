total_boletos = 0
ingresos_primera = 0
ingresos_segunda = 0
ingresos_tercera = 0
ingresos_nacional = 0
ingresos_internacional = 0
servicios_adicionales = 0

# Precios por clase
precio_primera = 200
precio_segunda = 150
precio_tercera = 100
ruta_nombre = ""
# Rutas nacionales y sus precios
def obtener_precio_ruta(ruta_nombre):
    if ruta_nombre == "Porlamar - Caracas":
        return 50
    elif ruta_nombre == "Caracas - Porlamar":
        return 50
    elif ruta_nombre == "Puerto Ordaz - Caracas":
        return 45
    elif ruta_nombre == "Caracas - Puerto Ordaz":
        return 45
    elif ruta_nombre == "Maracaibo - Caracas":
        return 80
    elif ruta_nombre == "Caracas - Maracaibo":
        return 80
    elif ruta_nombre == "El Vigía - Caracas":
        return 75
    elif ruta_nombre == "Caracas - El Vigía":
        return 75
    elif ruta_nombre == "Barcelona - Caracas":
        return 30
    elif ruta_nombre == "Caracas - Barcelona":
        return 30
    elif ruta_nombre == "La Fría - Caracas":
        return 60
    elif ruta_nombre == "Caracas - La Fría":
        return 60
    else:
        return 0  # Ruta no válida

def comprar_boleto():
    global total_boletos, ingresos_primera, ingresos_segunda, ingresos_tercera
    global ingresos_nacional, ingresos_internacional, servicios_adicionales
    
    num_boletos = int(input("Ingrese el número de boletos a comprar: "))
    for _ in range(num_boletos):
        nombre = input("Nombre del pasajero: ")
        cedula_tipo = input("Seleccione tipo de cédula (V/E): ")
        cedula_numero = input("Ingrese número de cédula: ")
        edad = int(input("Edad del pasajero: "))
        
        if edad < 18:
            print("Solo se venden boletos a mayores de 18 años.")
            continue
        
        print("Seleccione la clase:")
        print("1. Primera")
        print("2. Segunda")
        print("3. Tercera")
        clase_opcion = int(input("Ingrese el número de la clase: "))
        
        if clase_opcion == 1:
            clase = "Primera"
            precio = precio_primera
        elif clase_opcion == 2:
            clase = "Segunda"
            precio = precio_segunda
        elif clase_opcion == 3:
            clase = "Tercera"
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
        
        # Solicitar y calcular el precio de la ruta
        ruta = input("Ingrese la ruta de viaje (ejemplo: Caracas - Porlamar): ")
        precio_ruta = obtener_precio_ruta(ruta)
        if precio_ruta == 0:
            print("Ruta no válida.")
            continue
        
        # Sumar el precio de la ruta al precio base
        precio += precio_ruta
        
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
        
        print(f"Boleto comprado con éxito. Total a pagar: ${precio:.2f} (Ruta: {ruta})")

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
