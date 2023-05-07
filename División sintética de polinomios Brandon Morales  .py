def dividir_polinomios():
    dividendo_str = input("Ingrese el dividendo en forma de lista de coeficientes separados por espacios, de mayor a menor grado: ")
    dividendo = [int(x) for x in dividendo_str.split()]

    divisor_str = input("Ingrese el divisor en forma de lista de coeficientes separados por espacios, de mayor a menor grado: ")
    divisor = [int(x) for x in divisor_str.split()]

    dividendo = sorted(dividendo, reverse=True)
    divisor = sorted(divisor, reverse=True)

    if len(divisor) == 1:
        resultado = []
        for coeficiente in dividendo:
            resultado.append(coeficiente / divisor[0])
        return resultado

    if len(dividendo) < len(divisor):
        return [0]

    resultado = [0] * (len(dividendo) - len(divisor) + 1)

    for i in range(len(resultado)):
        resultado_i = dividendo[i] / divisor[0]
        resultado[i] = resultado_i

        for j in range(1, len(divisor)):
            dividendo[i + j] -= resultado_i * divisor[j]

    return resultado


if __name__ == '__main__':
    print("División sintética de polinomios")
    print("Ingrese los coeficientes de los polinomios separados por espacios, en el orde de mayor a menor grado")
    resultado = dividir_polinomios()
    print("El resultado de la división es:", resultado)

    ##BrandonMoralesGonzalez
    
