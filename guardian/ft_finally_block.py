class GardenError(Exception):
    default_msg = "Unknown garden error"
    def __init__(self, msg: str = None ) -> None:
        super().__init__(msg or self.default_msg)


class PlantError(GardenError):
    default_msg = "Unknown plant error"


class WaterError(GardenError):
    default_msg = "Unknown water error"


def water_plant(plant_name: str) -> None:
    if "A" <= plant_name[0] <= "Z":
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
        return
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