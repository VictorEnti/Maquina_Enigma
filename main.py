import Func.funciones as fun

update = True

while update:
    print("------ ENIGMA ------")
    print("1. Cifrar mensaje")
    print("2. Descrifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")
    op = input("> ")

    fun.diccionarios()

    if op == "1":
        fun.guardar_mensaje()
        fun.min_mayus("mensaje.txt")
        fun.cifrado("mensaje.txt")
    elif op == "2":
        fun.descifrado("cifrado.txt")
    #elif op == "3":
        
    elif op == "4":
        update = False
    else:
        print("Opcion no valida \n")