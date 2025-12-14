# Maquina_Enigma

DESCRIPCI�N 
Este proyecto consiste en una simulaci�n b�sica de la M�quina Enigma que fue utilizada durante la Segunda Guerra Mundial para cifrar mensajes. Hemos desarrollado un programa con las funciones b�sicas de tres rotores intercambiables con notches configurables, lo que permite cifrar y descifrar mensajes de manera flexible. 

OBJETIVOS DEL PROYECTO 
El objetivo es crear un programa en Python que simule el proceso de cifrado y descifrado de la m�quina, incluyendo: 
- Configuraci�n y gesti�n de los tres rotores
- Cifrar eligiendo las posiciones iniciales
- Interfaz de usuario intuitiva por consola
- Archivos que almacenan los mensajes y las configuraciones de los rotores

FUNCIONALIDADES QUE HEMOS IMPLEMENTADO
- Men� interactivo con 4 opciones principales:
   * Cifrar mensajes
   * Descifrar mensajes
   * Editar los rotores
   * Gestionar los archivos
- Validaci�n de las permutaciones (26 letras �nicas A-Z)
- Notches para controlar los rotores

DIFICULTADES ENCONTRADAS Y SOLUCIONES 

1. COMPRENDER EL FUNCIONAMIENTO DE ENIGMA
Entender la l�gica compleja del giro de los rotores, del cifrado y del descifrado de los mensajes nos supuso un problema que pudimos solucionar gracias a la ayuda de nuestro profesor y el soporte visual de videos de YouTube que encontramos.

2. VALIDAR PERMUTACIONES
Asegurar que cada rotor tenga exactamente 26 letras �nicas. Lo conseguimos solucionar creando las funciones que validaban y revisaban la longitud y la unicidad.

3. CONSEGUIR SIMULAR EL GIRO DE ROTOR
Hacer que cada letra que cifrase se "moviese" un posici�n adelante el "cifrador" ha sido una de las partes m�s complejas que nos hemos encontrado

METODOLOG�A DE TRABAJO 

1.DIVISI�N DE TAREAS
V�ctor se ha enfocado m�s en la l�gica de cifrado/descifrado y gesti�n de archivos
Artur se ha enfocado m�s en la interfaz de usuario

2.REUNIONES REGULARES
Hac�amos reuniones diarias para sincronizar el progreso, hemos revisado el c�digo conjuntamente y hemos usado GitKraken para registrar los avances. 

INSTRUCCIONES DE USO 

REQUISITOS PREVIOS: 
- Pyhton 3.x instalado
- Permisos de lectura y escritura en el sistema de archivos

CONFIGURACI�N: 
1. Clonar el repositorio
2. Asegurarse de que existen los archivos Rotores y Mensajes

EJECUCI�N: "python main.py" 

FLUJO DE FUNCIONAMIENTO
1. Configurar los rotores (este paso es opcional, ya que vienen configurados por defecto)
2. Cifrar Mensaje: seleccionar opci�n 1, introducir el mensaje y el resultado se guarda en "Cifrado.txt"
3. Descifrar el mensaje: seleccionar opci�n 2, se descifra "Cifrado.txt" y se guarda en "Descifrado.txt"

CREAR NUEVOS ROTORES 
1. Seleccionar opci�n 3 en el men�
2. Elegir rotor que queremos editar(1,2 o 3) 
3. Introducir 26 letras �nicas en cualquier orden
4. Especificar letras del notch

EJEMPLO DE USO: 
Mensaje : Hola V�ctor guapo

PROCESOS
1. Normalizaci�n: HOLAVICTORGUAPO
2. Agrupaci�n: HOLAV ICTOR GUAPO
3. Cifrado: Depende de la configuraci�n de los rotores
4. Descifrado: Devuelve el mensaje original

LIMITACIONES 
1. Los caracteres especiales se eliminan
2. Acentos no est�n permitidos
3. Los espacios solo se preservan en el mensaje original
4. Todo el texto se convierte en may�sculas

POSIBLES MEJORAS FUTURAS 

ALTA PRIORIDAD
1. Implementar el reflector
2. A�adir tablero de conexiones
3. Permitir el intercambio de orden de los rotores

PRIORIDAD MEDIA 
1. Interfaz gr�fica de usuario
2. Historial de configuraciones