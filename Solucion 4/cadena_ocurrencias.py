def contar_y_resaltar(cadena, palabra):
   
    contador = 0
    posicion = 0  
    
    while posicion < len(cadena):
        indice = cadena.find(palabra, posicion)
        if indice == -1:  
            break
        contador += 1  
        posicion = indice + len(palabra)  
    
    cadena_resaltada = cadena.replace(palabra, f"**{palabra}**")
    
    return contador, cadena_resaltada


def main():
    print("=== Contador y Resaltador de Ocurrencias ===")
    
    cadena = input("Ingrese la cadena C: ")
    palabra = input("Ingrese la palabra E: ")
   
    contador, cadena_resaltada = contar_y_resaltar(cadena, palabra)
    
    print(f"La palabra '{palabra}' aparece {contador} veces en la cadena.")
    print("Cadena con la palabra resaltada:")
    print(cadena_resaltada)


if __name__ == "__main__":
    main()