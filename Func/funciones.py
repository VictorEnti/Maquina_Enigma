from Func.const import ALFABETO, CIFRADO_FILE, LONGITUD_ALFABETO, MENSAJE_FILE
from Func.const import ROTOR_1, ROTOR_2, ROTOR_3, MENSAJE_FILE,CIFRADO_FILE,DESCIFRADO_FILE
from Func.const import MENSAJES_OK,MENSAJES_ERROR
from Func.const import ROTOR_ESTANDAR_CONFIGURACION

rotores=[]
dic_rot_1 = {}
dic_rot_2 = {}
dic_rot_3 = {}


def guardar_mensaje(): #Funcion para guardar los mensajes en su archivo correspondiente
    print("Por favor no utilice acentos")
    user_input = input("Mensaje a encriptar: ")
    with open(MENSAJE_FILE, "w") as mens:
        mens.write(user_input)

def min_mayus(archivo): #Funcion para poner en mayusculas y agrupar en grupos de 5
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

def diccionarios(): #Funcion para convertir los txt de los rotores en diccionarios

    with open(ROTOR_1, "r") as rot1:
        lineas_rotor = rot1.readlines(1)
        contador = 0

        for linea in lineas_rotor:
            l_rotor = linea
            letras_rotor = l_rotor.replace("\n", "")

        for posicion_letra in letras_rotor:
            dic_rot_1[contador] = posicion_letra
            contador += 1    

    with open(ROTOR_2, "r") as rot2:
        lineas_rotor = rot2.readlines(1)
        contador = 0

        for linea in lineas_rotor:
            l_rotor = linea
            letras_rotor = l_rotor.replace("\n", "")

        for posicion_letra in letras_rotor:
            dic_rot_2[contador] = posicion_letra
            contador += 1  

    with open(ROTOR_3, "r") as rot3:
        lineas_rotor = rot3.readlines(1)
        contador = 0

        for linea in lineas_rotor:
            l_rotor = linea
            letras_rotor = l_rotor.replace("\n", "")

        for posicion_letra in letras_rotor:
            dic_rot_3[contador] = posicion_letra
            contador += 1

def cifrado(archivo):
    separador = 0
    max_letras = 4

    with open(CIFRADO_FILE, "r") as cifr:
        for pack in cifr:
            paquetes = pack
    
    with open(CIFRADO_FILE, "w") as cifr:
        for letras in paquetes:
            for i in range(len(ALFABETO)):
                if dic_rot_1[i] == letras:
                    if separador < max_letras:
                        let_rot_2 = dic_rot_2[i]
                        cifr.write(dic_rot_3[i])
                        separador += 1
                    elif separador == max_letras:    
                        cifr.write(dic_rot_3[i])
                        cifr.write(" ")
                        separador = 0
        
        print("\n")
        print(f"[OK] Mensaje Cifrado en cifrado.txt, {len(paquetes)} letras, {len(paquetes)//5} packs de 5 letras (aprox)")

def descifrado(archivo):
    
    #Cifrado.txt tiene que existir para que esto funcione. poner try except

    with open(CIFRADO_FILE, "r") as cifr:
        for pack in cifr:
            paquetes = pack
    
    with open(DESCIFRADO_FILE, "w") as descifr:
        for letras in paquetes:
            for i in range(len(ALFABETO)):
                if dic_rot_3[i] == letras:
                    let_rot_2 = dic_rot_3[i]
                    descifr.write(dic_rot_1[i])

    print("\n")
    print(f"[OK] Mensaje descifrado en Desifrado.txt, {len(paquetes)} letras")



#Funcion que lee los archivos Rotor1.txt, Rotor2.txt, Rotor3.txt
#por cada rotor guarda el cableado que son 26 letras desordenadas
#y el notch que es la letra que hace girar el siguiente rotor

def cargar_rotores(): #Funcion para sobreescribir los rotores y poner combinaciones nuevas
    global rotores
    rotores=[]

    try:
       
        #cargar rotor 1
        with open(ROTOR_1, 'r') as f:
            lineas = f.readlines()
        if len(lineas) >= 1:
            cableado1 = lineas[0].strip() #el .strip() elimina los caracteres iniciales y finales de una cadena de texto
            if len(lineas) > 1:                #
                notch1 = lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                              #
                "Z"                            #
            rotores.append((cableado1,notch1))

        #cargar rotor 2
        with open(ROTOR_2, 'r') as f:
            lineas = f.readlines()
        if len(lineas) >= 1:
            cableado2 = lineas[0].strip()
            
            if len(lineas) > 1:                #
                notch2 = lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                              #
                "Z"                            #
            rotores.append((cableado2,notch2))

        #cargar rotor 3
        with open(ROTOR_3, 'r') as f:
            lineas = f.readlines()
        if len(lineas) >= 1:
            cableado3 = lineas[0].strip()
            if len(lineas) > 1:                #
                notch3 = lineas[1].strip()     # creo que todo esto se puede poner en una linea
            else:                              #
                "Z"                            #
            rotores.append((cableado3,notch3))

        return True

    except: 
        #si no hay rotores 
        rotores= ROTOR_ESTANDAR_CONFIGURACION[:] # esto es el slicing

        return True
        

    
     




