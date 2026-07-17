*Este proyecto ha sido creado como parte del currículo de 42 por migugonz, beamarti.*

# A-Maze-ing

## Descripción

A-Maze-ing es un generador de laberintos en Python que crea laberintos aleatorios
y reproducibles a partir de un archivo de configuración. El programa genera el
laberinto, calcula el camino más corto entre la entrada y la salida, lo exporta
en formato hexadecimal y lo visualiza en la terminal con colores ANSI.

El laberinto incluye el patrón "42" formado por celdas completamente cerradas,
visible en el centro del laberinto cuando el tamaño lo permite.

## Instrucciones

### Instalación

```bash
make install
```

### Ejecución

```bash
make run
```

O directamente:

```bash
python3 a_maze_ing.py config.txt
```

### Depuración

```bash
make debug
```

### Linting

```bash
make lint
```

## Configuración

El archivo `config.txt` debe contener los siguientes parámetros:

| Clave | Descripción | Ejemplo |
|---|---|---|
| WIDTH | Ancho del laberinto (número de celdas) | WIDTH=20 |
| HEIGHT | Alto del laberinto (número de celdas) | HEIGHT=15 |
| ENTRY | Coordenadas de la entrada (x,y) | ENTRY=0,0 |
| EXIT | Coordenadas de la salida (x,y) | EXIT=19,14 |
| OUTPUT_FILE | Nombre del archivo de salida | OUTPUT_FILE=maze.txt |
| PERFECT | Si True, laberinto perfecto (un solo camino) | PERFECT=True |
| SEED | Semilla para reproducibilidad (opcional) | SEED=42 |

Ejemplo de `config.txt`:

WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42

## Algoritmo

Se ha usado el algoritmo **Recursive Backtracker** (búsqueda en profundidad, DFS)
para la generación del laberinto. Este algoritmo:

- Empieza en la celda de entrada y va abriendo pasillos hacia celdas vecinas
  no visitadas, eligiendo una al azar en cada paso.
- Cuando llega a un callejón sin salida, retrocede hasta encontrar una celda
  con vecinas no visitadas.
- Termina cuando todas las celdas han sido visitadas.

Se eligió este algoritmo porque genera laberintos perfectos (un único camino
entre cualquier par de celdas) de forma natural, es sencillo de implementar
con una pila, y produce laberintos visualmente interesantes con pasillos largos
y sinuosos.

Para el camino más corto se usa **BFS** (Breadth-First Search), que garantiza
encontrar siempre el camino más corto entre la entrada y la salida.

### Modo `PERFECT=False`: tablero jugable estilo Pac-Man
 
Cuando `PERFECT=False` (valor por defecto), el laberinto generado por el DFS
(que produce un árbol perfecto, sin bucles) se transforma en un tablero
jugable mediante `generate_pacman_board()`, que aplica dos pasos:
 
1. **`open_corners()`**: fuerza a que las 4 esquinas y el centro del laberinto
   tengan al menos un pasillo abierto adicional, ya que en esas posiciones
   se sitúan los fantasmas/súper-pac-gums (esquinas) y el jugador (centro).
2. **Eliminación iterativa de callejones sin salida**: se buscan todas las
   celdas con una sola pared abierta (`find_dead_ends()`) y se abre una
   pared extra hacia un vecino para conectarlas con otra ruta, repitiendo el
   proceso hasta que no quede ningún callejón sin salida real (excluyendo las
   celdas del patrón "42", que están cerradas intencionadamente).
En ambos pasos se respetan las mismas reglas que durante la generación
inicial: nunca se abre una pared que cree un área 3x3 completamente abierta
(`would_create_3x3()`), y nunca se perfora una celda del patrón "42"
(`pattern_cells`).
 
El resultado es un tablero con múltiples rutas independientes (bucles) y,
en la práctica, sin ningún callejón sin salida real.

## Parte reutilizable

El módulo `mazegen` es instalable via pip:

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

Ejemplo de uso:

```python
from mazegen import MazeGenerator

maze = MazeGenerator(
    width=20,
    height=15,
    seed=42,
    perfect=True,
    entry=(0, 0),
    exit_cell=(19, 14)
)
maze.generate()

# Acceder a la rejilla
celda = maze.grid[y][x]  # diccionario con claves "N", "E", "S", "W"

# Acceder a las celdas del patrón 42
print(maze.pattern_cells)
```

Para reconstruir el paquete desde el código fuente:

```bash
pip install build
python -m build
```
Este módulo se distribuye bajo licencia MIT (ver LICENSE.md), que permite
su reutilización y distribución en proyectos futuros.

## Equipo y gestión del proyecto

### Roles

- **beamarti**: Clase `MazeGenerator`, módulo pip `mazegen`, `pathfinder.py`.
- **migugonz**: Parser de configuración, script principal `a_maze_ing.py`,
  serialización hexadecimal, visualización ASCII.

### Planificación

El proyecto se dividió desde el principio en dos partes independientes:
el módulo generador (reutilizable) y el script principal. Esto permitió
trabajar en paralelo sin interferencias.

### Herramientas

- Python 3.10+
- flake8 y mypy para linting y tipado estático.
- setuptools y wheel para el empaquetado pip.

## Resources

- [Maze generation algorithms - Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive Backtracker - Jamis Buck](https://weblog.jamisbuck.org/2010/12/27/maze-generation-depth-first-search)
- [BFS - Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Python packaging guide](https://packaging.python.org/en/latest/)

### Uso de IA

Se utilizaron **Claude (Anthropic)** y **Gemini (Google)** como herramientas 
de aprendizaje y apoyo durante todo el desarrollo, especialmente para plantear 
la arquitectura del proyecto.

Todo el código fue revisado, entendido y validado por el equipo antes de
integrarlo al proyecto.
