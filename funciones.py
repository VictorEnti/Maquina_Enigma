from const import MENSAJE_FILE

def guardar_mensaje():
    user_input = input("Mensaje a encriptar: ")
    with open(MENSAJE_FILE, "w") as mens:
        mens.write(user_input)



def cifrado(archivo):
    with open(MENSAJE_FILE) as mens:
        for letra in mens:
            letra_mayus = letra.upper()
            