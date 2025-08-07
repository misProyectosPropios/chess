from enum import Enum

class Pieza(Enum):
    """
    Piezas de ajedrez
    """
    PEON = 1
    ALFIL = 2
    TORRE = 3
    CABALLO = 4
    REY = 5
    REINA = 6

class Jugador(Enum):
    """
    Jugadores en una partida de ajedrez.
    """
    BLANCO = 1
    NEGRO = 2

 def __init__(self):
        """
        Constructor de la clase Tablero.
        Inicializa el tablero con las piezas en sus posiciones iniciales
        y establece el turno inicial al BLANCO.
        """
        self.tablero = self._crear_tablero_inicial()
        self.turno = Jugador.BLANCO

    def _crear_tablero_inicial(self) -> list[list[tuple[Pieza, Jugador] | None]]:
        """
        Método privado para inicializar la matriz del tablero con la disposición
        inicial de las piezas de ajedrez.
        Retorna una matriz de 8x8. Cada celda puede contener:
        - Una tupla (Pieza, Jugador) si hay una pieza.
        - None si la casilla está vacía.
        """
        tablero = [[None for _ in range(8)] for _ in range(8)]

        # Piezas Negras
        tablero[0][0] = (Pieza.TORRE, Jugador.NEGRO)
        tablero[0][1] = (Pieza.CABALLO, Jugador.NEGRO)
        tablero[0][2] = (Pieza.ALFIL, Jugador.NEGRO)
        tablero[0][3] = (Pieza.REINA, Jugador.NEGRO)
        tablero[0][4] = (Pieza.REY, Jugador.NEGRO)
        tablero[0][5] = (Pieza.ALFIL, Jugador.NEGRO)
        tablero[0][6] = (Pieza.CABALLO, Jugador.NEGRO)
        tablero[0][7] = (Pieza.TORRE, Jugador.NEGRO)
        for i in range(8):
            tablero[1][i] = (Pieza.PEON, Jugador.NEGRO)

        # Piezas Blancas
        tablero[7][0] = (Pieza.TORRE, Jugador.BLANCO)
        tablero[7][1] = (Pieza.CABALLO, Jugador.BLANCO)
        tablero[7][2] = (Pieza.ALFIL, Jugador.BLANCO)
        tablero[7][3] = (Pieza.REINA, Jugador.BLANCO)
        tablero[7][4] = (Pieza.REY, Jugador.BLANCO)
        tablero[7][5] = (Pieza.ALFIL, Jugador.BLANCO)
        tablero[7][6] = (Pieza.CABALLO, Jugador.BLANCO)
        tablero[7][7] = (Pieza.TORRE, Jugador.BLANCO)
        for i in range(8):
            tablero[6][i] = (Pieza.PEON, Jugador.BLANCO)

        return tablero

    def obtener_pieza(self, fila: int, columna: int) -> tuple[Pieza, Jugador] | None:
        """
        Devuelve la pieza en una casilla específica del tablero.
        """
        if 0 <= fila < 8 and 0 <= columna < 8:
            return self.tablero[fila][columna]
        return None # O podrías lanzar una excepción para coordenadas inválidas

    