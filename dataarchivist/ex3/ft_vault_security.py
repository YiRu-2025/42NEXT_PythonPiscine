def secure_archive(
    file_name: str, action: str = "r", content: str = "hello"
) -> tuple[bool, str]:
    try:
        with open(file_name, action) as f:
            state = True
            if action == "r":
                msg = f.read()
            elif action == "w":
                f.write(content)
                msg = 'Content successfully written to file'
    except Exception as e:
        state = False
        msg = str(e)
    return (state, msg)


def testing() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('nonfile'))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('nopermission.txt'))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('txt'))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('newfile', "w"))


if __name__ == "__main__":
    testing()
