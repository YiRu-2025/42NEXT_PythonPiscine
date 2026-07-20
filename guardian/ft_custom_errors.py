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


def check_plant(plant_name=None, wilting=True):
    if plant_name is None:
        raise PlantError()

    if wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")

    print(f"The {plant_name} plant is fine.")


def check_water(water_level=None):
    if water_level is None:
        raise WaterError()

    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")

    print("Enough water in the tank.")


def main():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant("rose")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for func in (lambda: check_plant("sunflower"),
                 lambda: check_water(0)):
        try:
            func()
        except GardenError as error:
            print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
