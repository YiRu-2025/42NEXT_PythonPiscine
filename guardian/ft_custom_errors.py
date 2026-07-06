class GardenError(Exception):
    default_msg = "Unknown garden error"
    def __init__(self, msg: str = None ) -> None:
        super().__init__(msg or self.default_msg)


class PlantError(GardenError):
    default_msg = "Unknown plant error"


class WaterError(GardenError):
    default_msg = "Unknown water error"


def plant_check(plant: str, wilting: bool) -> None:
    if wilting:
        raise PlantError(f"The {plant} plant is wilting!")
    else:
        print(f"The {plant} plant is good.")

def water_check(level: int) -> None:
    if level < 10:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Enough water in the tank.")

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    tests = [("PlantError", lambda: plant_check("tomato", True)),
             ("WaterError", lambda: water_check(5))]
    for name, test in tests:
        print(f"\nTesting {name}...")
        try:
            test()
        except PlantError as err:
            print(f"Caught {err.__class__.__name__}: {err}")
        except WaterError as err:
            print(f"Caught {err.__class__.__name__}: {err}")   
    print("\nTesting catching all garden errors...")
    for name, test in tests:
        try:
            test()
        except GardenError as err:
            print(f"Caught GardenError: {err}")
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()