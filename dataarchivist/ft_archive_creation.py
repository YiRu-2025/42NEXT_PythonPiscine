import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    try:
        with open(filename, "r") as file:
            print("---\n")
            content = file.read()
            print(content)
            print("\n---")
        print(f"File '{filename}' closed.")
        
        print("Transform data")
        new_cont = ""
        for c in content:
            if c == "\n":
                new_cont += "#\n"
            else:
                new_cont += c
        if content and not content.endswith("\n"):
            new_cont += "#"
        print("---")
        print(new_cont)
        print("---")

        
        new_file = input("Enter new file name (or empty): ")
        if not new_file:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            with open(new_file, "w") as nf:
                nf.write(new_cont)
            print(f"Data saved in file '{new_file}'")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")

if __name__ == "__main__":
    main()