from const import ALFABETO, CIFRADO_FILE, MENSAJE_FILE

def guardar_mensaje():
    print("Por favor no utilize acentos")
    user_input = input("Mensaje a encriptar: ")
    with open(MENSAJE_FILE, "w") as mens:
        mens.write(user_input)

def cifrado(archivo):
    separador = 0
    max_letras = 4

    with open(MENSAJE_FILE) as mens:
        with open(CIFRADO_FILE, "w") as cifr:
            for mens_original in mens:
                mens_original_mayus = mens_original.upper()
                mens_mayus = mens_original_mayus.split()
                for palabra in mens_mayus:
                    for letra in palabra:
                        if separador < max_letras:
                            if letra in ALFABETO:
                                cifr.write(letra)
                                separador += 1
                        elif separador == max_letras:    
                            cifr.write(letra)
                            cifr.write(" ")
                            separador = 0