import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO = open(filename, "r")
        content: str = file.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}")
        return
    print("---\n\n" + content + "\n\n---")
    file.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
