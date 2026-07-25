def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        # raise ValueError
        int("abc")
    elif operation_number == 1:
        # raise ZeroDivisionError
        10 / 0
    elif operation_number == 2:
        # raise FileNotFoundError
        open("non/existent/file")
    elif operation_number == 3:
        # raise TypeError
        "str" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for op_num in range(5):
        print(f"Testing operation {op_num}")
        try:
            garden_operations(op_num)
            print("Operation completed successfully")
        except Exception as err:
            print(f"Caught {err.__class__.__name__}: {err}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
