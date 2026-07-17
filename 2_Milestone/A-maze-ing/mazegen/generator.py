import random


class MazeGenerator():
    DIRECTIONS: dict[str, tuple[int, int]] = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
        }
    OPPOSITE: dict[str, str] = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E",
    }
    PATTERN_42: list[str] = [
        "X.X.XXX",
        "X.X...X",
        "XXX.XXX",
        "..X.X..",
        "..X.XXX",
    ]

    def __init__(
            self, width: int, height: int, seed: int | None,
            perfect: bool, entry: tuple[int, int],
            exit_cell: tuple[int, int]) -> None:
        """Inicializa el generador de laberintos con los parámetros dados."""
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect = perfect
        self.entry = entry
        self.exit = exit_cell
        self.pattern_cells: set[tuple[int, int]] = set()

        random.seed(self.seed)

        self.grid: list[list[dict[str, bool]]] = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append({"N": True, "E": True, "S": True, "W": True})
            self.grid.append(row)

    def generate(self) -> None:
        """Genera el laberinto usando el algoritmo recursive backtracker.
        Crea un laberinto perfecto abriendo pasillos entre celdas.
        Si perfect es False, añade pasillos extra para crear bucles.
        """
        visited = set()
        visited.add(self.entry)
        stack = [self.entry]
        self.place_pattern_42()
        visited.update(self.pattern_cells)

        while stack:
            current: tuple[int, int] = stack[-1]
            x, y = current
            neighbors: list[tuple[str, tuple[int, int]]] = []
            for direction, delta in self.DIRECTIONS.items():
                dx, dy = delta
                nx = x + dx
                ny = y + dy
                if (
                    0 <= nx < self.width
                    and 0 <= ny < self.height
                    and (nx, ny) not in visited
                    and not self.would_create_3x3(x, y, nx, ny)
                ):
                    neighbors.append((direction, (nx, ny)))

            if neighbors:
                direction, (nx, ny) = random.choice(neighbors)
                self.grid[y][x][direction] = False
                self.grid[ny][nx][self.OPPOSITE[direction]] = False
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

        if not self.perfect:
            self.generate_pacman_board()

    def place_pattern_42(self) -> None:
        """Coloca el patrón '42' en el centro del laberinto.
        Marca las celdas del patrón como completamente cerradas para que
        el generador no abra pasillos a través de ellas. Imprime un mensaje
        de error si el laberinto es demasiado pequeño para el patrón.
        """

        if self.width < 9 or self.height < 7:
            print("El patrón 42 no cabe en el laberinto")
            return
        start_x = (self.width // 2) - (len(self.PATTERN_42[0]) // 2)
        start_y = (self.height // 2) - (len(self.PATTERN_42) // 2)
        for y, row in enumerate(self.PATTERN_42):
            for x, cell in enumerate(row):
                if cell == "X":
                    self.grid[y + start_y][x + start_x] = {
                        "N": True, "E": True, "S": True, "W": True
                        }
                    self.pattern_cells.add((x + start_x, y + start_y))

    def would_create_3x3(self, x: int, y: int, nx: int, ny: int) -> bool:
        """Comprueba si derribar la pared entre (x, y) y (nx, ny) crearía un
          área 3x3 abierta.
            Args:
                x: Columna de la celda actual.
                y: Fila de la celda actual.
                nx: Columna de la celda vecina.
                ny: Fila de la celda vecina.
            Returns:
                True si derribar la pared crearía un área 3x3 abierta,
                False en caso contrario.
        """
        for cx in range(min(x, nx) - 2, min(x, nx) + 1):
            for cy in range(min(y, ny) - 2, min(y, ny) + 1):
                if (
                    cx < 0 or cy < 0 or cx + 2 >= self.width
                    or cy + 2 >= self.height
                     ):
                    continue
                open_area = True
                for row in range(cy, cy + 3):
                    for col in range(cx, cx + 2):
                        if self.grid[row][col]["E"]:
                            open_area = False
                for row in range(cy, cy + 2):
                    for col in range(cx, cx + 3):
                        if self.grid[row][col]["S"]:
                            open_area = False
                if open_area:
                    return True
        return False

    def count_open_walls(self, x: int, y: int) -> int:
        """Cuenta cuántas paredes abiertas tiene la celda dada."""
        open_walls: int = 0
        for value in self.grid[y][x].values():
            if not value:
                open_walls += 1
        return open_walls

    def find_dead_ends(self) -> list[tuple[int, int]]:
        """Busca y devuelve todas las celdas que sean callejones sin salida."""
        dead_ends: list[tuple[int, int]] = []
        for y in range(self.height):
            for x in range(self.width):
                if self.count_open_walls(x, y) == 1:
                    dead_ends.append((x, y))
        return dead_ends

    def open_corners(self) -> None:
        """Asegura que las 4 esquinas y el centro tengan pasillos abiertos
        y conectados con el resto del laberinto.
        """
        corners = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1)
        ]

        center = (self.width // 2, self.height // 2)
        all_targets = corners + [center]

        for cx, cy in all_targets:
            for direction, (dx, dy) in self.DIRECTIONS.items():
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < self.width and 0 <= ny < self.height
                    and not self.would_create_3x3(cx, cy, nx, ny)
                    and (nx, ny) not in self.pattern_cells
                ):
                    self.grid[cy][cx][direction] = False
                    self.grid[ny][nx][self.OPPOSITE[direction]] = False
                    break

    def generate_pacman_board(self) -> None:
        """Modifica el laberinto para el modo Pac-Man (PERFECT=False).

        Abre las esquinas/centro y elimina sistemáticamente los callejones sin
        salida conectándolos con vecinos para crear múltiples rutas (bucles).
        """

        self.open_corners()

        while True:
            dead_ends = self.find_dead_ends()
            active_dead_ends = [
                (x, y) for (x, y) in dead_ends
                if (x, y) not in self.pattern_cells
            ]
            if not active_dead_ends:
                break

            any_wall_opened = False

            for x, y in active_dead_ends:
                closed_directions = []
                for direction in self.DIRECTIONS:
                    if self.grid[y][x][direction]:
                        closed_directions.append(direction)

                random.shuffle(closed_directions)

                for direction in closed_directions:
                    dx, dy = self.DIRECTIONS[direction]
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if (nx, ny) in self.pattern_cells:
                            continue
                        if self.would_create_3x3(x, y, nx, ny):
                            continue
                        self.grid[y][x][direction] = False
                        self.grid[ny][nx][self.OPPOSITE[direction]] = False
                        any_wall_opened = True
                        break

            if not any_wall_opened:
                break
