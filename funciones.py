from const import ALFABETO, CIFRADO_FILE, MENSAJE_FILE
from const import ROTOR_1, ROTOR_2, ROTOR_3, MENSAJE_FILE,CIFRADO_FILE,DESCIFRADO_FILE
from const import MENSAJES_OK,MENSAJES_ERROR
from const import ROTOR_ESTANDAR_CONFIGURACION

rotores=[]

def guardar_mensaje():
    print("Por favor no utilize acentos")
    user_input = input("Mensaje a encriptar: ")
    with open(MENSAJE_FILE, "w") as mens:
        mens.write(user_input)

def min_mayus(archivo):
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

#Funcion que lee los archivos Rotor1.txt, Rotor2.txt, Rotor3.txt
#por cada rotor guarda el cableado que son 26 letras desordenadas
#y el notch que es la letra que hace girar el siguiente rotor

def cargar_rotores():
    global rotores
    rotores=[]

    try:
        

        #cargar rotor 1
        with open(ROTOR_1, 'r') as f:
            lineas= f.readlines()
        if len(lineas) >=1:
            cableado1= lineas[0].strip() #el .strip() elimina los caracteres iniciales y finales de una cadena de texto
            if len(lineas)> 1:                #
                notch1= lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                             #
                "Z"                           #
            rotores.append((cableado1,notch1))


        #cargar rotor 2
        with open(ROTOR_2, 'r') as f:
            lineas = f.readlines()
        if len(lineas) >= 1:
            cableado2 = lineas[0].strip()
            
            if len(lineas)> 1:                #
                notch2= lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                             #
                "Z"                           #
            rotores.append((cableado2,notch2))

        #cargar rotor 3
        with open(ROTOR_3, 'r') as f:
            lineas = f.readlines()
        if len(lineas) >= 1:
            cableado3 = lineas[0].strip()
            if len(lineas)> 1:                #
                notch3= lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                             #
                "Z"                           #
            rotores.append((cableado3,notch3))

        return True
    

    except: 
        #si no hay rotores 
        rotores= ROTOR_ESTANDAR_CONFIGURACION[:] # esto es el slicing

        return True
    

    
     




