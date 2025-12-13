from Func.const import ALFABETO, CIFRADO_FILE, CONFIGURACION_ESTANDAR_ROTOR, LONGITUD_ALFABETO, MENSAJE_FILE
from Func.const import ROTOR_1, ROTOR_2, ROTOR_3, MENSAJE_FILE,CIFRADO_FILE,DESCIFRADO_FILE
from Func.const import MENSAJES_OK,MENSAJES_ERROR
from Func.const import CONFIGURACION_ESTANDAR_ROTOR

rotores=[]
dic_rot_1 = {}
dic_rot_2 = {}
dic_rot_3 = {}

def guardar_mensaje(): #Funcion para guardar los mensajes en su archivo correspondiente
    
    try:
        print("-----------CIFRADO-----------")
        print("Por favor no utilice acentos")
        user_input = input("Mensaje a encriptar: ")
        with open(MENSAJE_FILE, "w") as mens:
            mens.write(user_input)
    
    except FileNotFoundError:
        print(f"El archivo {MENSAJE_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def min_mayus(): #Funcion para poner en mayusculas y agrupar en grupos de 5
    separador = 0
    max_letras = 4
    
    try:
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
    except FileNotFoundError:
        print(f"El archivo {MENSAJE_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def precargar_dic(): #Funcion que carga una configuracion preestablecida de los 3 rotores

    try:
        with open(ROTOR_1, "w") as rot1:
            rot1.write(CONFIGURACION_ESTANDAR_ROTOR[0][0])
            rot1.write("\n")
            rot1.write(CONFIGURACION_ESTANDAR_ROTOR[0][1])
    
    except FileNotFoundError:
        print(f"El archivo {ROTOR_1} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False
        
    try:
        with open(ROTOR_2, "w") as rot2:
            rot2.write(CONFIGURACION_ESTANDAR_ROTOR[1][0])
            rot2.write("\n")
            rot2.write(CONFIGURACION_ESTANDAR_ROTOR[1][1])
    
    except FileNotFoundError:
        print(f"El archivo {ROTOR_2} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False
    
    try:    
        with open(ROTOR_3, "w") as rot3:
            rot3.write(CONFIGURACION_ESTANDAR_ROTOR[2][0])
            rot3.write("\n")
            rot3.write(CONFIGURACION_ESTANDAR_ROTOR[2][1])
    
    except FileNotFoundError:
        print(f"El archivo {ROTOR_3} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def diccionarios(): #Funcion para convertir los txt de los rotores en diccionarios

    try:
        with open(ROTOR_1, "r") as rot1:
            lineas_rotor = rot1.readlines(1)
            contador = 0
            letras_rotor = ""

            for linea in lineas_rotor:
                l_rotor = linea
                letras_rotor = l_rotor.replace("\n", "")

            for posicion_letra in letras_rotor:
                dic_rot_1[contador] = posicion_letra
                contador += 1
    
    except FileNotFoundError:
        print(f"El archivo {ROTOR_1} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    try:
        with open(ROTOR_2, "r") as rot2:
            lineas_rotor = rot2.readlines(1)
            contador = 0
            letras_rotor = ""

            for linea in lineas_rotor:
                l_rotor = linea
                letras_rotor = l_rotor.replace("\n", "")

            for posicion_letra in letras_rotor:
                dic_rot_2[contador] = posicion_letra
                contador += 1  

    except FileNotFoundError:
        print(f"El archivo {ROTOR_2} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    try:
        with open(ROTOR_3, "r") as rot3:
            lineas_rotor = rot3.readlines(1)
            contador = 0
            letras_rotor = ""

            for linea in lineas_rotor:
                l_rotor = linea
                letras_rotor = l_rotor.replace("\n", "")

            for posicion_letra in letras_rotor:
                dic_rot_3[contador] = posicion_letra
                contador += 1

    except FileNotFoundError:
        print(f"El archivo {ROTOR_3} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def cifrado(): #Funcion para cifrar el contenido del archivo Cifrado.txt y reescribirlo en el mismo sitio
    separador = 0
    max_letras = 4

    try:
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
            
            print(f"[OK] Mensaje Cifrado en cifrado.txt, {len(paquetes)} letras, {len(paquetes)//5} packs de 5 letras (aprox)")

    except FileNotFoundError:
        print(f"El archivo {CIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def descifrado(): #Funcion para descifrar el archivo Cifrado.txt y escribirlo en Descifrado.txt
    
    try:
        with open(CIFRADO_FILE, "r") as cifr:
            for pack in cifr:
                paquetes = pack
        
    except FileNotFoundError:
        print(f"El archivo {CIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    try:
        with open(DESCIFRADO_FILE, "w") as descifr:
            for letras in paquetes:
                for i in range(len(ALFABETO)):
                    if dic_rot_3[i] == letras:
                        let_rot_2 = dic_rot_3[i]
                        descifr.write(dic_rot_1[i])

        print(f"[OK] Mensaje descifrado en Desifrado.txt, {len(paquetes)} letras")
    
    except FileNotFoundError:
        print(f"El archivo {DESCIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False
      
#Funcion que lee los archivos Rotor1.txt, Rotor2.txt, Rotor3.txt
#por cada rotor guarda el cableado que son 26 letras desordenadas
#y el notch que es la letra que hace girar el siguiente rotor
#Funciones para sobreescribir los rotores y poner combinaciones nuevas

def cargar_rotor_1(): 
    try:
        print("\n")
        print("Para configurar el rotor 1 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 1: ")
        long_correcta = True
        while long_correcta == True:
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:
                        if letra == x:
                            veces += 1
                            if veces == 2:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 1: ")    
                    else:    
                        with open(ROTOR_1, "w") as rot1:
                            rot1.write(user_input.upper())
                            long_correcta = False                           
            else:
                print(f"Faltan {26 - len(user_input)} letras")
                user_input = input("Rotor 1: ")

        with open(ROTOR_1, "a") as rot1:
            rot1.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
        if len(user_input) == 1:
            with open(ROTOR_1, "a") as rot1:
                rot1.write(user_input.upper())
                print("Rotor 1 cambiado\n")
        else:
            print("Solo una letra")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_1} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True

def cargar_rotor_2():
    try:
        print("\n")
        print("Para configurar el rotor 2 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 2: ")
        long_correcta = True
        while long_correcta == True:
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:
                        if letra == x:
                            veces += 1
                            if veces == 2:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 2: ")    
                    else:    
                        with open(ROTOR_2, "w") as rot2:
                            rot2.write(user_input.upper())
                            long_correcta = False
            else:
                print(f"Faltan {26 - len(user_input)} letras")
                user_input = input("Rotor 1: ")

        with open(ROTOR_2, "a") as rot2:
            rot2.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
        if len(user_input) == 1:
            with open(ROTOR_2, "a") as rot2:
                rot2.write(user_input.upper())
                print("Rotor 2 cambiado\n")
        else:
            print("Solo una letra")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_2} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True

def cargar_rotor_3():
    try:
        print("\n")
        print("Para configurar el rotor 3 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 3: ")
        long_correcta = True
        while long_correcta == True:
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:
                        if letra == x:
                            veces += 1
                            if veces == 2:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 3: ")    
                    else:    
                        with open(ROTOR_3, "w") as rot3:
                            rot3.write(user_input.upper())
                            long_correcta = False
            else:
                print(f"Faltan {26 - len(user_input)} letras")
                user_input = input("Rotor 1: ")

        with open(ROTOR_3, "a") as rot3:
            rot3.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
        if len(user_input) == 1:
            with open(ROTOR_3, "a") as rot3:
                rot3.write(user_input.upper())
                print("Rotor 3 cambiado\n")
        else:
            print("Solo una letra")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_3} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True