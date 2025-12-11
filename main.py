
import Func.funciones as fun

update = True
actualizado= True
while update:
    print(r" _____ _   _ _____ _____ ___  ___  ___   ")
    print(r"|  ___| \ | |_   _|  __ \|  \/  | / _ \  ")
    print(r"| |__ |  \| | | | | |  \/| .  . |/ /_\ \ ")
    print(r"|  __|| . ` | | | | | __ | |\/| ||  _  | ")
    print(r"| |___| |\  |_| |_| |_\ \| |  | || | | | ")
    print(r"\____/\_| \_/\___/ \____/\_|  |_/\_| |_/ ")
                                        

    print("\n1. Cifrar mensaje")
    print("2. Descrifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")
    op = input("Seleccione una opcion:  ")

    fun.diccionarios()

    if op == "1":
            fun.guardar_mensaje()
            fun.min_mayus("mensaje.txt")
            fun.cifrado("mensaje.txt")
    elif op == "2":
            fun.descifrado("cifrado.txt")
    elif op == "3":
            elegir_rotor= input("Elige el rotor (1,2,3) que deseas editar (pulse cualquier otro caracter para salir):  ")
            actualizado= True
            while actualizado:
                if elegir_rotor =="1":
                    fun.cargar_rotor_1()
                elif elegir_rotor=="2":
                    fun.cargar_rotor_2()
                elif elegir_rotor=="3":
                    fun.cargar_rotor_3()
                    actualizado=False
                else:
                    actualizado=False
                
    elif op == "4":
            update = False
    else:
            print("Opcion no valida \n")
            #actualizado=False

            

'''
import Func.funciones as fun

update = True

while update:
    print(r" _____ _   _ _____ _____ ___  ___   ___   ")
    print(r"|  ___| \ | |_  _|  __ \|  \/  | / _ \  ")
    print(r"| |__ |  \| | | | | |  \/| .  . |/ /_\ \ ")
    print(r"|  __|| . ` | | | | | __ | |\/| ||  _  | ")
    print(r"| |___| |\  |_| |_| |_\ \| |  | || | | | ")
    print(r"\____/\_| \_/\___/ \____/\_|  |_/\_| |_/ ")
                                        
    print("\n1. Cifrar mensaje")
    print("2. Descrifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")
    op = input("Seleccione una opcion: ")

    fun.diccionarios()
    # Este loop 'while True' es el que debemos controlar con 'break'
    while True: 
        if op == "1":
            fun.guardar_mensaje()
            fun.min_mayus("mensaje.txt")
            fun.cifrado("mensaje.txt")
            break # <-- ¡Añade break! Vuelve al menu principal
        
        elif op == "2":
            fun.descifrado("cifrado.txt")
            break # <-- ¡Añade break! Vuelve al menu principal
        
        elif op == "3":
            elegir_rotor = input("Elige el rotor (1,2,3) que deseas editar (pulse cualquier otro caracter para salir): ")
            actualizado = True
            
            # Este loop controla la edición específica del rotor
            while actualizado: 
                if elegir_rotor == "1":
                    fun.cargar_rotor_1()
                elif elegir_rotor == "2":
                    fun.cargar_rotor_2()
                elif elegir_rotor == "3":
                    fun.cargar_rotor_3()
                
                # Independientemente de si se editó o no, salimos de este loop interno
                actualizado = False 
            
            # Una vez que salimos del loop de edición, salimos del while True 
            # para volver a imprimir el menú principal.
            break # <-- ¡Añade break! Vuelve al menu principal
            
        elif op == "4":
            update = False
            break # <-- ¡Añade break! Sale del while True y luego del while update
            
        else:
            print("Opcion no valida \n")
            # Si la opción no es válida, no queremos que se quede en el loop 'while True'
            # así que también salimos para pedir la opción nuevamente.
            break
            '''