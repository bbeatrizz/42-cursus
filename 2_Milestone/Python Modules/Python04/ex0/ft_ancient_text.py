import sys


def main() -> None:
    num_args: int = len(sys.argv) - 1
    if num_args != 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    try:
        f = open(sys.argv[1], "r")
        print(f"Accessing file '{sys.argv[1]}'")
        print("---")
        contenido: str = f.read()
        print(f"\n{contenido}")
        f.close()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return


if __name__ == "__main__":
    main()
