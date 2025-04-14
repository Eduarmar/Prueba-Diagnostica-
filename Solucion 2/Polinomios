from math import comb

def generar_coeficientes_polinomio(n):
    """
    Genera los coeficientes del polinomio (x+1)^n usando el triángulo de Pascal.
    """
    coeficientes = [comb(n, i) for i in range(n + 1)]
    print(f"Coeficientes:{coeficientes}")
    return coeficientes

def calcular_polinomio(coeficientes, x):
    """
    Calcula f(x) = (x+1)^n paso a paso según el polinomio generado.
    """
    n = len(coeficientes) - 1  # Grado del polinomio
    resultado = 0
    pasos = []
    
    for i, coef in enumerate(coeficientes):
        exponente = n - i
        termino = coef * (x ** exponente)
        pasos.append(f"{coef} * (x^{exponente}) = {termino}")
        resultado += termino
    
    return resultado, pasos

def main():
    
    n = int(input("Ingrese un número entero no negativo n: "))
    x = float(input("Ingrese el valor de x: "))
    
    
    coeficientes = generar_coeficientes_polinomio(n)
    
    
    polinomio = " + ".join([f"{coef}x^{n-i}" if i < n else f"{coef}" for i, coef in enumerate(coeficientes)])
    print(f"Polinomio generado para (x+1)^{n}: {polinomio}")
    
    # Calcular el valor de f(x) y mostrar los pasos
    resultado, pasos = calcular_polinomio(coeficientes, x)
    print(f"Valor de f(x) = {resultado} para x={x}")
    print("Pasos del cálculo:")
    for paso in pasos:
        print(paso)

# Ejecutar el programa
if __name__ == "__main__":
    main()
