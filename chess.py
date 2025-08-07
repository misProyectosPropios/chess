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

