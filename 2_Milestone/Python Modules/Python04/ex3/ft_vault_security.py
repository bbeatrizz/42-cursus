def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as f:
                file_content = f.read()
                return (True, file_content)
        elif action == "w":
            with open(filename, "w") as f:
                f.write(content)
                return (True, 'Content successfully written to file')
        else:
            return (False, "Invalid action")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    result1: tuple[bool, str] = secure_archive("sd", "r")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(result1)

    result2: tuple[bool, str] = secure_archive(
                "C:\\Windows\\System32\\config\\SAM", "r")
    print("\nUsing 'secure_archive' to read from a inaccesible file:")
    print(result2)

    result_r: tuple[bool, str] = secure_archive("ancient_fragment.txt", "r")
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(result_r)
    if result_r[0]:
        result_w: tuple[bool, str] = secure_archive("new_arch.txt",
                                                    "w", result_r[1])
        print("\nUsing 'secure_archive' to write previous"
              " content to a new file:")
        print(result_w)


if __name__ == "__main__":
    main()
