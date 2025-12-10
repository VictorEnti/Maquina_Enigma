ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
LONGITUD_ALFABETO = 26

# Nombres de archivos
ROTOR_1 = "Rotores\Rotor_1.txt"  
ROTOR_2 = "Rotores\Rotor_2.txt"
ROTOR_3 = "Rotores\Rotor_3.txt"
MENSAJE_FILE = "Mensajes\Mensaje.txt"
CIFRADO_FILE = "Mensajes\Cifrado.txt"
DESCIFRADO_FILE = "Mensajes\Descrifrado.txt"

# Configuración por defecto de rotores
ROTOR_ESTANDAR_CONFIGURACION = [
    ("FNHCORPGZYWJAMDSLBUVQTKXIE", "P"),  # Rotor 1 
    ("VLZJMXTBSGEQKIYCROFWHAPNUD", "C"),  # Rotor 2 
    ("PSWGKQAHUFZORLVETDJYCBMNIX", "G")   # Rotor 3
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

