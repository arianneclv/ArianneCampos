#Un servidor crea logs por cada acción que se realiza en él. El administrador desea
#un programa que todos los días borre todos los logs excepto si el log contiene la
#palabra "error"; si contiene esta palabra, se debe copiar el log al directorio #"Errores" y se debe enviar un correo al administrador.

#Paso 1: Entender

#¿Qué son logs? "Archivos de texto en los que se incluyen de forma cronológica los #acontecimientos como cambios".
#El programa necesita  crear logs por cada cambio que el usuario ocasione en él. Al #final del día estos deben ser borrados automaticamente excepto aquellos en los #cuales ocurrió un error y estén marcados así, en ese caso se deben guardar en una #sección especifica donde automaticamente sean enviados al correo del administrador.

#Paso 2: Planear

#¿Mi programa necesita una interfaz de usuario? ¿Cómo se va a
#ver? ¿Qué funcionalidades tendrá la interfaz? 
#No, el programa actua directamente sobre el servidor, no sobre algo introducido directamente sobre el programa.
#¿Qué inputs recibirá mi programa? ¿De dónde provendrán estos
#inputs?
#Son los cambios realizados sobre el servidor, deben de venir de este mismo.
#¿Cuál es el resultado o output que queremos obtener?
#Un listado de los logs que contenian error, así como un correo con estos dirigido al administrador.
#Dados los inputs, ¿cuáles son los pasos necesarios para llegar a
#los outputs?
#El programa debe de conectarse al servido de interes.
#Cada vez que ocurra un cambio dentro de la interfaz se debe de crear un nuevo log.
#Al final del día se deben guardar en una carpeta sola los logs con error.
#Los logs sin error deben ser borrados.
#La carpeta de los logs con error debe ser enviada al administrador por medio del correo.

#Paso 3: Dividir y conquistar

1. Concetar el programa con la interfaz.
2. Que el programa reconozca cuando se realizar un cambio en la interfaz.
3. Por cada cambio cree un log nuevo.
4. Reconozca los logs con error.
5. Borre los logs todos los días excepto los de error.
6. Guardar logs con error en carpetas por aparte.
7. Guarde el correo del administrador a donde se enviaran las cosas.
8. Enviar esta carpeta al correo del administrador.