def cargar_polinomios():
    # pedir la cantidad de términos del polinomio
    n = int(input("Ingrese la cantidad de términos del polinomio: "))
    polinomio = []
    for i in range(n):
        # pedir cada término del polinomio
        termino = input(f"Ingrese el término {i+1} del polinomio: ")
        polinomio.append(termino)
    return polinomio


def division_sintetica():
    print("Ingrese el dividendo:")
    dividendo = cargar_polinomios()
    print("Ingrese el divisor:")
    divisor = cargar_polinomios()

    grado_dividendo = len(dividendo) - 1
    grado_divisor = len(divisor) - 1

    if grado_divisor > grado_dividendo:
        print("El grado del divisor es mayor que el grado del dividendo.")
        return

    resultado = [0] * grado_dividendo
    resultado.append(dividendo[grado_dividendo])
    for i in range(grado_dividendo - 1, -1, -1):
        resultado[i] = dividendo[i+1] + resultado[i+1] * divisor[0]
    print("Resultado:", resultado[:-1])
    print("Residuo:", resultado[-1])


def menu():
    opcion = 0
    while opcion != 3:
        print("\n--------Menú--------")
        print("1. Cargar polinomios desde un archivo.")
        print("2. Ingresar polinomios manualmente.")
        print("3. Salir.")
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            print("Cargar polinomios desde archivo.")
            # Cargar polinomios desde archivo
        elif opcion == 2:
            print("Ingresar polinomios manualmente.")
            division_sintetica()
        elif opcion == 3:
            print("Salir.")
        else:
            print("Opción inválida. Intente de nuevo.")


menu()

## Brandon Morales 