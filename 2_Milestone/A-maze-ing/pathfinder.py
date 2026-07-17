from mazegen import MazeGenerator
from collections import deque


def solve(maze: MazeGenerator) -> list[str]:
    """Encuentra el camino más corto desde la entrada a la salida.
    Devuelve una lista de letras ['S', 'W', 'E', ...] que representan la ruta.
    """
    width = maze.width
    height = maze.height
    start = maze.entry
    end = maze.exit

    queue: deque[tuple[tuple[int, int], list[str]]] = deque([(start, [])])

    visited = {start}

    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
    }

    while queue:
        (cx, cy), path = queue.popleft()

        if (cx, cy) == end:
            return path

        current_cell_walls = maze.grid[cy][cx]

        for direction, (dx, dy) in directions.items():
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not current_cell_walls[direction]:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [direction]))
    return []
