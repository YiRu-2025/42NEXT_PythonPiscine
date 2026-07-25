def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    testing = ["25", "abc", "100", "-50"]
    for case in testing:
        print(f"\nInput data is '{case}'")
        try:
            temp = input_temperature(case)
            print(f"Temperature is now {temp}°C")
        except Exception as err:
            print(f"Caught input_temperature error: {err}")
    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
