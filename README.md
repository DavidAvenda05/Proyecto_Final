# PROYECTO FINAL: ALGORITMOS Y PROGRAMACIÓN
## NEW PACMAN GAME MODE
### Protecto realizado por:
*Juan David Avendaño Rodríguez

*Juan Diego Hernández Ramírez

Universidad EAN - Segundo Semestre - Ciclo 4

21-11-2022 Bogota D.C.

## INTRODUCCIÓN
Pacman es un famoso videojuego que sin duda ha hecho historia, siendo el más exitoso en los años 80 ganando un Récord Guiness, se trata de un circulo amarillo que simula una boca, va moviéndose por laberintos para obtener puntos hasta comer todos los que se encuentren en la pantalla y es perseguido por fantasmas que, si cruzan con el jugador, se pierde una vida automáticamente y reaparece desde el punto inicial sin perder el progreso. Cuenta con habilidades que lo hacen más rápido o inmune a los fantasmas por un límite de tiempo y que así el juego sea más entretenido, cada jugador posee 3 vidas y entre más se avance, más complicado se hace. Fue lanzado el 22 de mayo de 1980 por Toru Iwatani de la empresa Namco, consolidándose como uno de los videojuegos más icónicos de la historia.
Una vez aclarada cual es la inspiración de este proyecto, a continuación, se abordará como fue su realización y explicamos como funciona.
## PROGRAMAS Y EXTENSIONES
### PYTHON
Python es un lenguaje de programación imprescindible para el entorno del desarrollo web, siendo el lenguaje más usado a nivel mundial, es utilizado en la creación de aplicaciones web, machine learning y ciencia de datos, al ser un lenguaje tan sencillo de aprender y compatible con multiples plataformas a la hora de ser usado, lo hace catalogarse en esta posición. Además de la sintaxis de código que se tiene, una biblioteca estándar amplia, y menor iso de líneas de código.
### VISUAL STUDIO CODE
Visual Studio Code se trata un editor de código fuente desarrollado por Microsoft. Es un software libre y multiplataforma, se integra bien con Git, admite la depuración de código y tiene innumerables extensiones que básicamente le permiten escribir y ejecutar código en cualquier lenguaje de programación.
### TURTLE
El módulo .tutle es una biblioteca pre-instalada en python con el fin de dar al usuario la posibilidad de crear gráficos e imágenes, dibujando figuras intrincadas usando programas que repiten movimientos simples.
Las clases usadas con este módulo en el proyecto fueron:

*Screen(): 
          -setx
          
          -sety
          
          -right
          
          -left
          
          -speed
          
          -xcor
          
          -ycor
          
          -penup
          
          -color
          
Y demas funciones fueron usadas para la creación de este programa, facilitando la interfaz gráfica del usuario con el algoritmo y dando la posibilidad de los movimientos y acciones que realiza el programa al ser ejecutado.
### RANDOM
Este módulo implementa al desarrollador la generación de números pseudoaleatorios para las distribuciones necesarias en el programa.
Para el programa se usa *random.randint* con el fin de generar la comida y enemigos de manera aleatoria en unas cordenadas que limita la función.
### TIME
Este módulo como su nombre lo indica, da lugar a la creación de funciones relacionadas con el tiempo. 

Para el proyecto se implemento la función time.sleep combinada junto a el módulo .turtle da lugar que el Pacman al acercarse con los límites del programa (bordes), o con los enemigos, este se reincie y de un tiempo de espera de un segundo para volver y aparecer en las coordenadas (0,0), con el fin de empezar de nuevo el programa.

## CODIFICACIÓN DEL PROGRAMA
Como se menciono a lo largo de la documentación, la codificación se basa en la importación de 3 bibliotecas pre-instaladas en python con el fin de dar una interfaz gráifca con el usuario al usar el programa.

.Turtle ; .time ; .random ; fueron las bibliotecas usadas, se crearon 2 varibles principales con el fin del uso del programa las cuales fueron: pacman y la ventana de salida al ejecutar el programa; 2 listas: enemigos y alimento. Todas estas con el uso de las bibliotecas, ya explicadas anteriormente.

## CONSLUSIONES
Al momento de pensar en programar un juego que ya existe, buscamos la idea de algo diferente iniciando de lo clásico, se puede pensar que es bastante sencillo de realizar, la creación de un juego nos ayudo a realizar una lógica diferente y como desde una codificación en un lenguaje sencillo, dar una interfaz al usuario buena y divertida, pensar en como dar límites, o como hacer que una puntuación sume cada vez que un "pacman" se acerca a una bola, y así mismo disminuir las vidas al tener contacto con un enemigo, podemos concluir que la realización de un código para el entretenimiento, es una manera de lograr lógica, y una oportunidad investigativa e interesante de realizar, el conocimiento en programación acerca de diseño, bibliotecas y demas ayudo a un nuevo modo de ver la programación que puede ir hacia un fin de diversión.

## REFERENCIAS
Python, R. (2020, febrero 26). The beginner’s guide to Python turtle. Realpython.com; Real Python. https://realpython.com/beginners-guide-python-turtle/

Python random module. (2021, julio 22). GeeksforGeeks. https://www.geeksforgeeks.org/python-random-module/

random —Generar números pseudoaleatorios — documentación de Python - 3.11.0. (s/f). Python.org. Recuperado el 20 de noviembre de 2022, de https://docs.python.org/es/3/library/random.html

time — Acceso a tiempo y conversiones — documentación de Python - 3.11.0. (s/f). Python.org. Recuperado el 20 de noviembre de 2022, de https://docs.python.org/es/3/library/time.html

turtle — Gráficos con Turtle — documentación de Python - 3.9.14. (s/f). Python.org. Recuperado el 20 de noviembre de 2022, de https://docs.python.org/es/3.9/library/turtle.html

(S/f). Amazon.com. Recuperado el 20 de noviembre de 2022, de https://aws.amazon.com/es/what-is/python/



