import sys


def main() -> None:
    num_args: int = len(sys.argv) - 1
    if num_args != 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

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

    print("\nTransform data:")
    print("---")
    print()
    f = open(sys.argv[1], "r")
    mod_lines = []
    for line in f:
        if line.endswith("\n"):
            new_line = line[:-1] + "#\n"
        else:
            new_line = line + "#\n"
        mod_lines.append(new_line)
    f.close()

    for line in mod_lines:
        print(line, end="")

    print()
    print("---")
    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    new_f = open(new_name, "w")
    for line in mod_lines:
        new_f.write(line)
    new_f.close()
    print(f"Data saved in file '{new_name}'.")
    print()


if __name__ == "__main__":
    main()
