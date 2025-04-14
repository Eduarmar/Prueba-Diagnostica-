import re

def fen_validar(cadena_c):
    comprobador = r'\s*^(((?:[rnbqkpRNBQKP1-8]+\/){7})[rnbqkpRNBQKP1-8]+)\s([b|w])\s(-|[K|Q|k|q]{1,4})\s(-|[a-h][1-8])\s(\d+\s\d+)$'
    
    if re.match(comprobador, cadena_c):
        return True
    return False



def main():
    cadena = input("Ingrese la cadena para validar: ")
    print(f"Cadena ingresada: {cadena}") 
    if fen_validar(cadena):
        print("✅ La cadena está en notación FEN válida.")
    else:
        print("❌ La cadena no está en notación FEN válida.")

if __name__ == "__main__":
    main()