import re

def Evaluar_Aritmetica(expresion):

    expresion = expresion.replace(" ", "")
    
    if not re.match(r"^[\dEe\+\-\*/\.\(\)]+$", expresion):
        return "Error: Expresión contiene caracteres no permitidos."
   
    tokens = re.findall(r"\d+(?:\.\d+)?(?:[eE][\+\-]?\d+)?|[\+\-\*/\(\)]", expresion)
    print (tokens)

    # Función auxiliar
    def operar(a, b, operador):
        a, b = float(a), float(b)
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            if b == 0:
                raise ZeroDivisionError("División por cero.")
            return a / b
    
    
    def evaluar(tokens):
        
        operandos = []
        operadores = []
        
        prioridad = {'+': 1, '-': 1, '*': 2, '/': 2}
        
        for token in tokens:
            if re.match(r"\d+(?:\.\d+)?(?:[eE][\+\-]?\d+)?", token):  # Es un numero
                operandos.append(token)
            elif token in "+-*/":  # Es un operador
                while (operadores and operadores[-1] in "+-*/" and
                       prioridad[token] <= prioridad[operadores[-1]]):
                    
                    b = operandos.pop()
                    a = operandos.pop()
                    operador = operadores.pop()
                    resultado = operar(a, b, operador)
                    operandos.append(resultado)
                operadores.append(token)
            elif token == "(":
                operadores.append(token)
            elif token == ")":
                while operadores and operadores[-1] != "(":
                    b = operandos.pop()
                    a = operandos.pop()
                    operador = operadores.pop()
                    resultado = operar(a, b, operador)
                    operandos.append(resultado)
                operadores.pop()  # Eliminar (
        
    
        while operadores:
            b = operandos.pop()
            a = operandos.pop()
            operador = operadores.pop()
            resultado = operar(a, b, operador)
            operandos.append(resultado)
        
        return operandos[0]

    
    try:
        resultado = evaluar(tokens)
        return resultado
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error al evaluar la expresión: {e}"


if __name__ == "__main__":
    print("=== Evaluador de Expresiones Aritméticas ===")
    expresion = input("Ingrese la expresión aritmética a evaluar: ")
    resultado = Evaluar_Aritmetica(expresion)
    print(f"Resultado: {resultado}")