import sys
import os
import random
from typing import Any
from mazegen import MazeGenerator
from pathfinder import solve


def parse_config(filepath: str) -> dict[str, Any]:
    """ Lee y valida el config.txt, gestiona errores de forma correcta"""
    config: dict[str, str] = {}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    print("Error de sintaxis en el archivo de"
                          f" configuración: '{line}'")
                    sys.exit(1)

                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    except FileNotFoundError:
        print(f"Error: El archivo de configuración '{filepath}' no existe")
        sys.exit(1)

    required_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
                     "OUTPUT_FILE", "PERFECT"]
    for key in required_keys:
        if key not in config:
            print("Error: Falta el parámetro obligatorio "
                  f"'{key}' en config.txt")
            sys.exit(1)

    try:
        width = int(config["WIDTH"])
        height = int(config["HEIGHT"])
        entry_x, entry_y = map(int, config["ENTRY"].split(","))
        exit_x, exit_y = map(int, config["EXIT"].split(","))

        seed_val = config.get("SEED", "")
        seed = int(seed_val) if seed_val else None

        parsed_data = {
            "width": width,
            "height": height,
            "seed": seed,
            "perfect": config["PERFECT"].lower() == "true",
            "entry": (entry_x, entry_y),
            "exit": (exit_x, exit_y),
            "output_file": config["OUTPUT_FILE"]
        }

        if width <= 0 or height <= 0:
            print("Error: El ancho y alto deben ser mayores que cero")
            sys.exit(1)

        if not (0 <= entry_x < width and 0 <= entry_y < height):
            print("Error: La entrada está fuera de los límites del laberinto")
            sys.exit(1)

        if not (0 <= exit_x < width and 0 <= exit_y < height):
            print("Error: La salida está fuera de los límites del laberinto")
            sys.exit(1)

        if (entry_x, entry_y) == (exit_x, exit_y):
            print("Error: La entrada y la salida no pueden ser la misma celda")
            sys.exit(1)

        return parsed_data

    except ValueError:
        print("Error: Formato numérico o de coordenadas"
              " inválido en config.txt")
        sys.exit(1)


def get_path_cells(
        start: tuple[int, int], path_str: str
        ) -> set[tuple[int, int]]:
    '''Convierte una cadena de solución en un conjunto
        de tuplas de coordenadas'''
    cells = {start}
    x, y = start
    deltas = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    for move in path_str:
        if move in deltas:
            dx, dy = deltas[move]
            x += dx
            y += dy
            cells.add((x, y))
    return cells


def render_ascii(
        maze: MazeGenerator, solution_path: str, show_path: bool,
        color_ansi: str) -> None:
    """Renderiza el laberinto en la terminal usando colores ANSI."""
    reset = "\033[0m"
    cyan = "\033[96m"
    magenta = "\033[95m"

    path_cells = (
        get_path_cells(maze.entry, solution_path)
        if show_path
        else set()
    )

    for y in range(maze.height):
        north_str = ""
        for x in range(maze.width):
            north = (
                color_ansi + "+---" + reset
                if maze.grid[y][x]["N"]
                else color_ansi + "+   " + reset
            )
            north_str += north
        print(north_str + color_ansi + "+" + reset)

        row_str = ""
        for x in range(maze.width):
            west = color_ansi + "|" + reset if maze.grid[y][x]["W"] else " "
            if (x, y) == maze.entry:
                interior = magenta + " E " + reset
            elif (x, y) == maze.exit:
                interior = magenta + " X " + reset
            elif (x, y) in maze.pattern_cells:
                interior = "\033[43m" + "   " + reset
            elif (x, y) in path_cells:
                interior = cyan + " • " + reset
            else:
                interior = "   "
            row_str += west + interior
        print(row_str + color_ansi + "|" + reset)

    south_str = ""
    for x in range(maze.width):
        south_str += color_ansi + "+---" + reset
    print(south_str + color_ansi + "+" + reset)


def export_to_hex_file(
        maze: MazeGenerator, filepath: str, solution_path: str) -> None:
    ''' Exporta la cuadrícula del laberinto en formato hexadecimal y
    añade metadatos los y la solución '''
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for y in range(maze.height):
                row_chars = []
                for x in range(maze.width):
                    mask = 0
                    if maze.grid[y][x]["N"]:
                        mask |= 1
                    if maze.grid[y][x]["E"]:
                        mask |= 2
                    if maze.grid[y][x]["S"]:
                        mask |= 4
                    if maze.grid[y][x]["W"]:
                        mask |= 8
                    row_chars.append(f"{mask:x}")
                f.write("".join(row_chars) + "\n")

            f.write("\n")

            f.write(f"{maze.entry[0]},{maze.entry[1]}\n")
            f.write(f"{maze.exit[0]},{maze.exit[1]}\n")
            f.write(f"{solution_path}\n")

        print(f"Laberinto exportado correctamente en: {filepath}")

    except Exception as e:
        print(f"Error al escribir el archivo de salida: {e}")
        sys.exit(1)


def interactive_loop(params: dict[str, Any]) -> None:
    """Gestiona las interacciones del usuario para regenerar,
    dibujar y colorear el laberinto."""
    colors = ["\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[97m"]
    color_idx = 0
    show_path = False

    maze = MazeGenerator(
        width=params["width"],
        height=params["height"],
        seed=params["seed"],
        perfect=params["perfect"],
        entry=params["entry"],
        exit_cell=params["exit"]
    )
    maze.generate()

    path_list = solve(maze)
    path_str = "".join(path_list)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        render_ascii(maze, path_str, show_path, colors[color_idx])

        print("\n=== A-Maze-ing ===")
        print("1. Regenerar nuevo laberinto")
        print("2. Mostrar/Ocultar camino solución")
        print("3. Cambiar color de las paredes")
        print("4. Exportar y salir")

        choice = input("\n¿Qué quieres hacer? (1-4): ").strip()

        if choice == "1":
            new_seed = random.randint(1, 99999)
            maze = MazeGenerator(
                width=params["width"],
                height=params["height"],
                seed=new_seed,
                perfect=params["perfect"],
                entry=params["entry"],
                exit_cell=params["exit"]
            )
            maze.generate()
            path_list = solve(maze)
            path_str = "".join(path_list)
        elif choice == "2":
            show_path = not show_path
        elif choice == "3":
            color_idx = (color_idx + 1) % len(colors)
        elif choice == "4":
            export_to_hex_file(maze, params["output_file"], path_str)
            print("¡Hasta la próxima! 👋")
            break
        else:
            print("Opción inválida. Elige de 1 a 4.")


def main() -> None:

    if len(sys.argv) != 2:
        print("Uso obligatorio: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    params = parse_config(sys.argv[1])
    interactive_loop(params)


if __name__ == "__main__":
    main()
