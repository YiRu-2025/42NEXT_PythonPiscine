def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature():
    print("=== Garden Temperature ===")
    testing = ["25", "abc"]
    for case in testing:
        print(f"Input data is '{case}'")
        try:
            temp = input_temperature(case)
            print(f"Temperature is now {temp}°C")
        except Exception as err:
            print(f"Caught input_temperature error: {err}")
    print("All tests completed - program didn't crash")

if __name__ == "__main__":
    test_temperature()