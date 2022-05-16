import gamelib

ANCHO_JUEGO = 10
ALTO_JUEGO = 10
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
FICHA_X = 'X'
FICHA_O = 'O'
VACIO = ""

#Creo una matriz de valores vacios que se reemplazaran con el nombre de la ficha correspondiente al turno (X / O)
def juego_crear():
    juego = []
    for y in range(ALTO_JUEGO):
        fila = []
        for x in range(ANCHO_JUEGO):
            fila.append(VACIO)
        juego.append(fila)
    return juego

def juego_actualizar(juego, x, y, jugador, turno):
    #Realizo los corrimientos correspondientes a la posicion del tablero en la ventana y el tamaño de la celda
    fila = (y - 50) // 20
    columna = (x - 50) // 20
    if(juego[fila][columna] == ""):
        juego[fila][columna] = jugador
        turno += 1
    return juego, turno

def juego_mostrar(juego, jugador):
    """Actualizar la ventana"""
    #Se dibuja el texto con el nombre del juego
    gamelib.draw_text('5 en línea', 150, 20)
    #Dibujo cada celda del tablero como un rectangulo separado
    for i in range (50, 250, 20):
        for j in range (50, 250, 20):
            gamelib.draw_rectangle(i, j, i+20, j+20)
    #Recorro la matriz del juego para encontrar las posiciones donde escribir las letras correspondientes
    for i in range (0, 10, 1):
        for j in range (0, 10, 1):
            fila = (i * 20) + 60
            columna = (j * 20) + 60
            gamelib.draw_text(juego[i][j], columna, fila, fill = "black")
    #Dibujo el nombre del jugador de turno
    gamelib.draw_text("Es el turno del jugador: " + jugador, 150, 280)
    

def main():
    juego = juego_crear()
    jugador = FICHA_O
    turno = 0
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
    
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:

        gamelib.draw_begin()
            
        juego_mostrar(juego, jugador)

        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            #Verifico que la posicion clickeada este dentro del tablero de juego
            if (50 <= x <= 250 and 50 <= y < 250):
                juego, turno = juego_actualizar(juego, x, y, jugador, turno)
            #Verifico a qué jugador corresponde el turno (PAR / IMPAR) 
            if(turno % 2 == 0):
                jugador = FICHA_O
            else:
                jugador = FICHA_X

gamelib.init(main)
