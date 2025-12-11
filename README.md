# Maquina_Enigma

DESCRIPCIÓN 
Este proyecto consiste en una simulación básica de la Maquina Enigma que fue utilizada durante la segunda Guerra Mundial para cifrara mensajes. Hemos desarrollado un programa con las funciones basicas de tres rotores intercambiales con notches configurables, que nos permite cifrar y descrifrar mensajes de manera flexible. 

OBJETIVOS DEL PROYECTO 
El objetivo es crear un programa en Python que simule el proceso de cifrado y descrigrado de la maquina, incliyendo: 
- Configurar y gestionar los tres rotores
- Cifrar eligiendo las posiciones iniciales
- Interfaz de usuario intuitiva por consola
- Archivos que almacenan los mensajes y las configuraciones

FUNCIONALIDADES QUE HEMOS IMPLEMENTADO
- Menú interactivo con 4 opciones principales
- Cifrar mensajes
- Descifrar mensajes
- Editar los rotores
- Gestionar los archivos
- Validar las permutaciones (26 letras únicas A-Z)
- Notches para controlar los rotores

DIFICULTADES ENCONTRADAS Y SOLUCIONES 

1. COMPRENDER EL FUNCIONAMIENTO DE ENIGMA
Entender la logica compleja del giro de los rotores y el cifrado y el descifrado de los mensajes nos supuso un problema que pudimos solucionar gracias a la ayuda de nuestro profesor y el soporte visual de videos de YouTube que encontramos.

2. VALIDAR PERMUTACIÓNES
Asegurar que cada rotor tenga exactamente 26 letras únicas. Lo conseguimos solucionar creando las funciones que validaban y revisaban la longitud y la unicidad.

....

METODOLOGÍA DE TRABAJO 

1.DIVISION DE TAREAS
Victor Rius se ha enfocado mas en la logica de cifrado/descifrado y gestión de archivos
Artur Abrahamyan se ha enfocado mas en la interfaz de usuario

2.REUNIONES REGULARES
Ambos haciamos reuniones diarias para sincronizar el progreso, hemos revisado el codigo conjuntamente y hemos usado GitKraken para registrar cada cambio. 

INSTRUCCIONES DE USO 

REQUISITOS PREVIOS: 
- Pyhton 3.x instalado
- Acceso de lecutra y escritura en el sistema de archivos

CONFIGUACIÓN: 
1. Clonar el repositorio
2. Asegurarse de que existen los archivos Rotores y Mensajes

EJECUCIÓN: "python main.py" 

FLUJO DE FUNCIONAMIENTO

1. Configruar rotores (este paso es opcional ya que vienen configurados por defecto)
2. Cifrar Mensaje, seleccionar opcion 1, introducir el mensaje y el resultado se guarda en "Cifrado.txt"
3. Descifrar el mensaje, seleccionar opcion 2, se descifra "Cifrado.txt" a "Descifrado.txt"

CREAR NUEVOS ROTORES 
1. Seleccionar opcion 3 en el menú
2. Elegir rotor que queremos editar(1,2 o 3) 
3. Introducir 26 letras únicas en cualquier orden
4. Especificar letras del notch

EJEMPLO DE USO: 
texto : Hola Victor guapo

PROCESOS
1. Normalización: HOLAVICTORGUAPO
2. Agrupación: HOLAV ICTOR GUAPO
3. Cifrado: Depende de la configuración de los rotores
4. Descifrado: Devuelve el mensaje original

LIMITACIONES 
1. Caracteres especiales se eliminan
2. Acentos no estan permitidos
3. Los esapcios solo se preservan en la agrupación final
4. Todo el texto de coniverte en mayúsculas

POSIBLES MEJORAS FUTURAS 

ALTA PRIORIDAD
1. Implementar el Reflector
2. Añadir tablero de conexiones
3. Permitir el intercambio de orden de los rotores

PRIORIDAD MEDIA 
1. Interfaz gráfica de usuario
2. Historial de configuraciones
   


