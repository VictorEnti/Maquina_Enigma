
import Func.funciones as fun

update = True
actualizado= True

fun.precargar_dic()

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
    op = input("Seleccione una opcion: ")
    print("\n")

    if op == "1":
        fun.diccionarios()
        fun.guardar_mensaje()
        fun.min_mayus()
        fun.cifrado()
    elif op == "2":
        fun.diccionarios()
        fun.descifrado()
    elif op == "3":
        elegir_rotor = input("Elige el rotor (1,2,3) que deseas editar \n(pulse cualquier otro caracter para salir): ")
        actualizado = True
        while actualizado:
            if elegir_rotor =="1":
                fun.cargar_rotor_1()
                actualizado=False
            elif elegir_rotor=="2":
                fun.cargar_rotor_2()
                actualizado=False
            elif elegir_rotor=="3":
                fun.cargar_rotor_3()
                actualizado=False
            else:
                actualizado=False
                
    elif op == "4":
        update = False
    else:
        print("Opcion no valida \n")