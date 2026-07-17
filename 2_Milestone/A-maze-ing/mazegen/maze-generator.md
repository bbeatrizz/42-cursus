# Mazegen

Módulo Python para la generación de laberintos aleatorios y reproducibles.

## Instalación

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

## Uso básico

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
```

## Parámetros

| Parámetro | Tipo | Descripción |
|---|---|---|
| width | int | Ancho del laberinto (número de columnas) |
| height | int | Alto del laberinto (número de filas) |
| seed | int o None | Semilla para reproducibilidad. None = aleatorio |
| perfect | bool | Si True, un único camino entre entrada y salida |
| entry | tuple(x, y) | Coordenadas de la entrada |
| exit_cell | tuple(x, y) | Coordenadas de la salida |

## Acceder a la estructura

```python
# Acceder a una celda concreta (columna x, fila y)
celda = maze.grid[y][x]

# Cada celda es un diccionario con sus 4 paredes
# True = pared cerrada, False = pared abierta
print(celda)  # {"N": True, "E": False, "S": True, "W": True}

# Acceder a las celdas del patrón "42"
print(maze.pattern_cells)  # set de tuplas (x, y)

# Acceder a entrada y salida
print(maze.entry)   # (0, 0)
print(maze.exit)    # (19, 14)
```

## Obtener la solución

El módulo expone la estructura del laberinto pero no incluye
un pathfinder. Para obtener el camino más corto puedes usar
BFS sobre `maze.grid`:

```python
from collections import deque

def solve(maze):
    queue = deque([(maze.entry, [])])
    visited = {maze.entry}
    while queue:
        (cx, cy), path = queue.popleft()
        if (cx, cy) == maze.exit:
            return path
        for direction, (dx, dy) in maze.DIRECTIONS.items():
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < maze.width and 0 <= ny < maze.height
                    and not maze.grid[cy][cx][direction]
                    and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [direction]))
    return []

path = solve(maze)
print("".join(path))  # "EESENEE..."
```