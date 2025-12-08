ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LONGITUD_ALFABETO = 26

# Nombres de archivos
ROTOR_FILES = ["Rotor1.txt", "Rotor2.txt", "Rotor3.txt"]
MENSAJE_FILE = "Missatge.txt"
CIFRADO_FILE = "Xifrat.txt"
DESCIFRADO_FILE = "Desxifrat.txt"

# Configuración por defecto de rotores
ROTOR_ESTANDAR_CONFIGURACION = [
    ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),  # Rotor 1 
    ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),  # Rotor 2 
    ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")   # Rotor 3 
]

#Aqui pongo las constantes de los Errores que se pueden generar a lo largo del programa en la logica try/except, tenemos que importar const en los demas archivos para poder usar los errores de las constantes.
MENSAJES_OK = {
    "cifrado": "[OK] Mensaje cifrado en '{file}' ({lletres} letras, {grups} grupos de 5)",
    "descifrado": "[OK] Mensaje cifrado en '{file}'",
    "rotor_guardado": "[OK] Rotor guardado en {file}"
}

MENSAJES_ERROR = {
    "fichero_no_encontrado": "[ERROR] {file}: fichero no encontrado",
    "permutacion_incorrecta": "[ERROR] {file}: permutacion incorrecta, hacen falta  26 letras unicas A-Z",
    "notch_invalido": "[ERROR] {file}: notch invalido",
    "fichero_vacio": "[ERROR] {file}: fichero_vacio",
    "guardar_error": "[ERROR] No se ha podido guardar {file}: {error}",
    "opcion_invalida": "[ERROR] Opcion no valida"
}

#los {file} son espacios en blanco que se rellenan despues cuando los usemos 
#por ejemplo 
#mensaje = "[OK] guardado en '{file}'".format(file="cifrado.txt")
#resultado: "[OK] guardado en 'cifrado.txt'"

#asi evitamos repetir el texto y que sea redundandte

