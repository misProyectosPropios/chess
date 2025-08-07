# Chess

## TODO
+ Enum a las piezas
+ Crear el tablero haciendolo de 8 x 8 ubicando a las piezas correctamente
+ Permitir el movimiento a las piezas (sin doble movimiento de piezas, ni fijandome si es ilegal)
+ Fijarse si una pieza no se puede poner en cierta ubicación porque genera un jaque
+ Poner stockfish

## Docuemtacion

### Class

### Piezas

**Enum de piezas**:
+ PEON
+ ALFIL
+ TORRE
+ CABALLO
+ REY
+ REINA

### Jugadores

**Enum de jugadores**:
+ BLANCO
+ NEGRO

#### Tablero

##### Datos

+ Tablero: List(List(Piezas))
    + matriz de 8 x 8 de piezas
+ Turno: Jugadores
    + El turno de cada 
+ PiezasNegro: Set(Piezas)
+ PiezasBlanco: Set(Piezas)
+ MovimientosRealizados: List(Movimientos)

##### Métodos

+ Crear() -> Tablero
    + Devuelve un tablero inicializado.
    + El turno asignado automáticamente al BLANCO.

+ movimiento_pieza(posPrev: tuple(int, int), posAfter: tuple(int, int)) -> Bool:
    + Devuelve si se puede efectuar el movimiento o no. 
    En caso de que se pueda, realiza el movimiento y cambia al jugador

+ _cambiarTurno() -> None:
    + Si el Turno == Blanco -> Turno == Negro
    + Si el Turno == Negro -> Turno == Blanco

+ movimientoPieza(pos: tuple(int, int)) -> Set(tuple(int, int))
    + Devuelve el conjunto con todas las posiciones a las que una pieza en la posición pos pueda realizar legalmente

+ imprimir_tablero() -> None
    + Muestra el tablero

+ obtener_pieza(fila: int, columna: int) -> tuple[Pieza, Jugador] | None:
    + Devuelve la pieza en la posición o None en caso de no haber

