from Func.const import ALFABETO, LONGITUD_ALFABETO, CONFIGURACION_ESTANDAR_ROTOR
from Func.const import ROTOR_1, ROTOR_2, ROTOR_3, MENSAJE_FILE, CIFRADO_FILE, DESCIFRADO_FILE
from Func.const import MENSAJES_OK,MENSAJES_ERROR

rotores=[]
dic_rot_1 = {}
dic_rot_2 = {}
dic_rot_3 = {}

def guardar_mensaje(): #Funcion para guardar los mensajes en su archivo correspondiente
    
    try:
        print("-----------CIFRADO-----------")
        print("Por favor no utilice acentos \nya que estos no se guardaran")
        user_input = input("Mensaje a encriptar: ")
        with open(MENSAJE_FILE, "w") as mens:                                       #Abre el archivo donde se guardara el mensaje
            mens.write(user_input)                                                  #Escribe el mensaje
    
    except FileNotFoundError:                                                       #Posibles errores
        print(f"El archivo {MENSAJE_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

def min_mayus(): #Funcion para poner en mayusculas y agrupar en grupos de 5
    separador = 0
    max_letras = 4
    
    try:
        with open(MENSAJE_FILE) as mens:                                            #Abre el archivo donde esta el mensaje
            with open(CIFRADO_FILE, "w") as cifr:                                   #Abre el archivo donde se escribira el mensaje cifrado
                for mens_original in mens:                                          #Pone en mayusculas las letras
                    mens_original_mayus = mens_original.upper()
                    mens_mayus = mens_original_mayus.split()
                    for palabra in mens_mayus:
                        for letra in palabra:
                            if separador < max_letras:                              #Va escribiendo las letras mientras el separador
                                if letra in ALFABETO:                               #sea menor que 5, entonces hace un paquete
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
        with open(ROTOR_1, "w") as rot1:                                            #Abre el archivo del rotor y escribe una configuracion
            rot1.write(CONFIGURACION_ESTANDAR_ROTOR[0][0])                          #que se encuentra guardada en const.py
            rot1.write("\n")                                                        #El resto de la funcion hace lo mismo para los otros rotores
            rot1.write(CONFIGURACION_ESTANDAR_ROTOR[0][1])
    
    except FileNotFoundError:                                                       #Posibles errores
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
        with open(ROTOR_1, "r") as rot1:                                            #Abre el archivo del rotor
            lineas_rotor = rot1.readlines(1)                                        #Lee la cantidad de lineas
            contador = 0
            letras_rotor = ""

            for linea in lineas_rotor:
                letras_rotor = linea.replace("\n", "")

            for posicion_letra in letras_rotor:                                     #Convierte la lista de letras en un diccionario
                dic_rot_1[contador] = posicion_letra                                #El resto de la funcion hace lo mismo para los otros rotores
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
                letras_rotor = linea.replace("\n", "")

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
                letras_rotor = linea.replace("\n", "")

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
    saltos = 0
    lon_packs = 5

    try:
        with open(CIFRADO_FILE, "r") as cifr:                                       #Abre el archivo donde estan los packs de letras
            for pack in cifr:
                paquetes = pack                                                     #Los guarda en una variable para poder abrir el archivo
        
        with open(CIFRADO_FILE, "w") as cifr:                                       #en modo escritura y borrarlo todo
            for letras in paquetes:
                for i in range(len(ALFABETO)):
                    if dic_rot_1[i] == letras:                                      #Busca la posicion de la letra en el diccionario creado anteriormente
                        if separador < max_letras:                                  #Verifica que siga dentro del maximo del paquete
                            let_rot_2 = dic_rot_2[i]
                            if (i + saltos) >= LONGITUD_ALFABETO:                   #Se busca en el resto de diccionarios mientras que se aplica el giro
                                pos_letra = ((i + saltos) - LONGITUD_ALFABETO)      #de rotor
                                cifr.write(dic_rot_3[pos_letra])                    #En caso de pasarse del maximo de letras se resta la longitud del alfabeto
                            else:
                                pos_letra2 = (i + saltos)
                                cifr.write(dic_rot_3[pos_letra2])
                            if saltos == LONGITUD_ALFABETO:
                                saltos = 0
                            separador += 1                       
                        
                        elif separador == max_letras:                               #Misma logica pero para el separador
                            if (i + saltos) >= LONGITUD_ALFABETO:
                                pos_letra3 = ((i + saltos) - LONGITUD_ALFABETO)
                                cifr.write(dic_rot_3[pos_letra3])
                            else:
                                pos_letra4 = (i + saltos)
                                cifr.write(dic_rot_3[pos_letra4])
                            if saltos == LONGITUD_ALFABETO:
                                saltos = 0                           
                            cifr.write(" ")
                            separador = 0
                        saltos += 1
            
            print(f"[OK] Mensaje Cifrado en cifrado.txt, {len(paquetes)} letras, {len(paquetes)//lon_packs} packs de 5 letras (aprox)")

    except FileNotFoundError:
        print(f"El archivo {CIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False
    except UnboundLocalError:
        print("Mensaje vacio, por favor inserte el mensaje a encriptar")
        return False

def descifrado(): #Funcion para descifrar el archivo Cifrado.txt y escribirlo en Descifrado.txt
    
    saltos = 0

    try:
        with open(CIFRADO_FILE, "r") as cifr:                                       #Abre el archivo donde se encuentra el mensaje cifrado
            for pack in cifr:
                paquetes = pack
        
    except FileNotFoundError:
        print(f"El archivo {CIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    try:
        with open(DESCIFRADO_FILE, "w") as descifr:                                 #Abre el archivo en modo escritura
            for letras in paquetes:
                for i in range(len(ALFABETO)):                                      #Aplica el proceso inverso de la funcion anterior
                    if dic_rot_3[i] == letras:
                        let_rot_2 = dic_rot_2[i]
                        if (i - saltos) <= -1:
                            descifr.write(dic_rot_1[((i - saltos) + LONGITUD_ALFABETO)])
                        else:
                            descifr.write(dic_rot_1[i - saltos])
                        if saltos == LONGITUD_ALFABETO:
                            saltos = 0
                        saltos += 1
    
        print(f"[OK] Mensaje descifrado en Descifrado.txt, {len(paquetes)} letras")
    
    except FileNotFoundError:
        print(f"El archivo {DESCIFRADO_FILE} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False
    except UnboundLocalError:
        print("Archivo vacio, no se puede ejecutar")
        return False
    
#Funcion que lee los archivos Rotor1.txt, Rotor2.txt, Rotor3.txt
#por cada rotor guarda el cableado que son 26 letras desordenadas                   
#y el notch que es la letra que hace girar el siguiente rotor
#Funciones para sobreescribir los rotores y poner combinaciones nuevas

def cargar_rotor_1():

    letra_repetida = 2
    long_correcta = True
    notch = True

    try:
        print("\n")
        print("Para configurar el rotor 1 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 1: ")
        while long_correcta == True:                                                #Bucle para obligar al cumplimiento de la condicion
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:                                            #Revisa que no haya letras repetidas
                        if letra == x:
                            veces += 1
                            if veces == letra_repetida:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 1: ")    
                    else:                                                           #Reescribe el rotor
                        with open(ROTOR_1, "w") as rot1:
                            rot1.write(user_input.upper())
                            long_correcta = False                           
            else:                                                                   #Indica cuantas letras faltan para cumplir la condicion
                print(f"Faltan {LONGITUD_ALFABETO - len(user_input)} letras")       
                user_input = input("Rotor 1: ")

        with open(ROTOR_1, "a") as rot1:
            rot1.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
        
        while notch == True:                                                        #Bucle para asegurar que se cumple la condicion
            if len(user_input) == 1:                                                #Revisa que la longitud del notch sea 1
                with open(ROTOR_1, "a") as rot1:
                    rot1.write(user_input.upper())
                    print("Rotor 1 cambiado\n")
                    notch = False 
            else:
                print("Notch invalido: solo una letra")
                user_input = input("Letra de salto: ")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_1} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True

def cargar_rotor_2():

    letra_repetida = 2
    long_correcta = True
    notch = True

    try:
        print("\n")
        print("Para configurar el rotor 2 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 2: ")
        while long_correcta == True:                                                #Bucle para obligar al cumplimiento de la condicion
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:                                            #Revisa que no haya letras repetidas
                        if letra == x:
                            veces += 1
                            if veces == letra_repetida:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 2: ")    
                    else:                                                           #Reescribe el rotor
                        with open(ROTOR_2, "w") as rot2:
                            rot2.write(user_input.upper())
                            long_correcta = False
            else:                                                                   #Indica cuantas letras faltan para cumplir la condicion
                print(f"Faltan {LONGITUD_ALFABETO - len(user_input)} letras")
                user_input = input("Rotor 2: ")

        with open(ROTOR_2, "a") as rot2:
            rot2.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
            
        while notch == True:                                                        #Bucle para asegurar que se cumple la condicion
            if len(user_input) == 1:                                                #Revisa que la longitud del notch sea 1
                with open(ROTOR_2, "a") as rot2:
                    rot2.write(user_input.upper())
                    print("Rotor 2 cambiado\n")
                    notch = False
            else:
                print("Notch invalido: solo una letra")
                user_input = input("Letra de salto: ")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_2} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True

def cargar_rotor_3():

    letra_repetida = 2
    long_correcta = True
    notch = True

    try:
        print("\n")
        print("Para configurar el rotor 3 inserte la siguiente \ncadena en orden aleatorio y sin repeticiones:")
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        user_input = input("Rotor 3: ")
        while long_correcta == True:                                                #Bucle para obligar al cumplimiento de la condicion
            if len(user_input) == LONGITUD_ALFABETO:
                for letra in user_input:
                    veces = 0
                    for x in user_input:                                            #Revisa que no haya letras repetidas
                        if letra == x:
                            veces += 1
                            if veces == letra_repetida:
                                print("Hay letras repetidas")
                                user_input = input("Rotor 3: ")    
                    else:                                                           #Reescribe el rotor
                        with open(ROTOR_3, "w") as rot3:
                            rot3.write(user_input.upper())
                            long_correcta = False
            else:                                                                   #Indica cuantas letras faltan para cumplir la condicion
                print(f"Faltan {LONGITUD_ALFABETO - len(user_input)} letras")
                user_input = input("Rotor 3: ")

        with open(ROTOR_3, "a") as rot3:
            rot3.write("\n")

        print("\nInserte la letra de salto")
        user_input = input("Letra de salto: ")
        
        while notch == True:                                                        #Bucle para asegurar que se cumple la condicion
            if len(user_input) == 1:                                                #Revisa que la longitud del notch sea 1
                with open(ROTOR_3, "a") as rot3:
                    rot3.write(user_input.upper())
                    print("Rotor 3 cambiado\n")
                    notch = False
            else:
                print("Notch invalido: solo una letra")
                user_input = input("Letra de salto: ")

    except FileNotFoundError:
        print(f"El archivo {ROTOR_3} no se ha encontrado")
        return False
    except FileExistsError:
        print("Archivo corrupto")
        return False

    return True