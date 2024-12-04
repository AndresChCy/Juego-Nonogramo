 Juego-Nonogramo
El juego se inicia desde Window.py en srcs/Visuals


----------Como instalar el juego---------
Requerimientos: 
-Tener pycharm instalado.
-Interprete de python version 3 o mayor.

¿Como instalarlo?
Primero clona este repositorio o descarga el archivo zip y descomprimelo.
Accede a la carpeta srcs luego a la carpeta Visuals y luego abre Window.py con pycharm y abre el proyecto
Seguramente te salga una alerta como esta: ![imagen](https://github.com/user-attachments/assets/4a058604-790b-494e-897d-e00742f1dd9f)
Si es asi presiona en configurar interprete, en otro caso ve a las barras en la esquina superior de pycharm y presiona File ![imagen](https://github.com/user-attachments/assets/112e9e0c-6219-4095-a04a-9abd44512b4f)
Accede a settings, luego a project y python interpreter ![imagen](https://github.com/user-attachments/assets/2ba092c8-7f77-4c0d-ba07-a2e91c3f373b)
Presiona en añadir interprete.
![imagen](https://github.com/user-attachments/assets/6cb6709a-1fbc-475d-9dc6-9ce170f87ab4)
Establece una ruta para tu entorno virtual y tu version de python y al final aprieta OK.

Una vez instalado el interprete quizas te salga algo asi :![imagen](https://github.com/user-attachments/assets/06175974-a43e-4fb1-a055-42dc5e0965de)
Si es asi puedes apretar en install requirements, sino ve a la terminal e pycharm y asegurate que estas conectao al entorno virtual(si sale venv): ![imagen](https://github.com/user-attachments/assets/d7a5a858-1cad-41d5-b774-1ec034cfdcf8)
Y escribe "pip install -r requirements.txt" ![imagen](https://github.com/user-attachments/assets/018e578f-c9bf-4685-8140-87b855663799)

Luego para correr el programa tienes que apretar especificamente click derecho en el archivo Window.py y darle a Run. No servira si corres el programa desde Current File.
![imagen](https://github.com/user-attachments/assets/c43b4f0d-8b12-4a85-a3c7-f46779707e28)

Para probar los test puedes ir a la carpeta test y correrlos manualmente.

Ya puedes disfrutar de nuestro juego nonogram!



----------Normas para el proyecto---------
-
-Para clases visuales:
  * Guardarlas en la carpeta respectiva Visuals
  * En caso de ser un panel o usar pygame en la clase utilizar la interfaz "Panel" para definir los comandos que se usaran ante los eventos y como se dibujan los paneles. No crear loops infinitos en el constructor.
  * Pueden probar individualmente la interfaz grafica implementada creando un metodo "execute" el cual tendrá la misma implementacion que tiene execute en la clase "Window" de Window.py y luego llamarla en un main.
  * Intentar especificar el tipo de dato de propiedades importantes.

-Para clases logicas:
* Guardarlas en en la carpeta respetica Logica.
* Hacer Unit Test de los metodos mas importantes.
* Intentar abordar varios casos posibles distintos con los tests.
* Mejor intentar hacer TDD.
* Evitar hacer clases que se escapen demasiado de la idea inicial del UML.

-Pull Requests(Que hay que poner): 
* Que cambios se introducen.
* Para que se introducen esos cambios
* Alguna descripcion de las nuevas clases o clases cambiadas
* Intentar sintetizar la información.

