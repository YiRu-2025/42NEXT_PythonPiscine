class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant-related problems."""

    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering-related problems."""

    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(factory: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in factory:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")


def main():
    valid_tests = ["Tomato", "Lettuce", "Carrots"]
    invalid_test = ["Tomato", "lettuce", "Carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(valid_tests)
    print("Testing invalid plants...")
    test_watering_system(invalid_test)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
