from math import comb

def generar_coeficientes_polinomio(n):
    
    coeficientes = [comb(n, i) for i in range(n + 1)]
    print(f"Coeficientes:{coeficientes}")
    return coeficientes

def calcular_polinomio(coeficientes, x):
  
    n = len(coeficientes) - 1  
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
    
    
    resultado, pasos = calcular_polinomio(coeficientes, x)
    print(f"Valor de f(x) = {resultado} para x={x}")
    print("Pasos del cálculo:")
    for paso in pasos:
        print(paso)


if __name__ == "__main__":
    main()
