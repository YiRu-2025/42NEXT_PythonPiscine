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
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return
    print("---\n" + content + "\n---")
    file.close()
    print(f"File '{filename}' closed.")

    print("Transform data")
    new_cont: str = ""
    for c in content:
        if c == "\n":
            new_cont += "#\n"
        else:
            new_cont += c
    if len(content) > 0 and content[len(content) - 1] != "\n":
        new_cont += "#"
    print("---")
    print(new_cont)
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file: str = sys.stdin.readline().strip()
    print(new_file)
    if not new_file:
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file}'")
    try:
        nf: typing.IO = open(new_file, "w")
        nf.write(new_cont)
        nf.close()
        print(f"Data saved in file '{new_file}'")
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{new_file}': {e}",
              file=sys.stderr)
        return


if __name__ == "__main__":
    main()
