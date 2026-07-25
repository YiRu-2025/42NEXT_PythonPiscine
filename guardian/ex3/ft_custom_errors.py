class GardenError(Exception):
    """Base exception for all garden-related errors."""
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant-related problems."""
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering-related problems."""
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant_name: str | None = None, wilting: bool = True) -> None:
    if plant_name is None:
        raise PlantError()
    if wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")
    print(f"The {plant_name} plant is fine.")


def check_water(water_level: int | None = None) -> None:
    if water_level is None:
        raise WaterError()
    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")
    print("Enough water in the tank.")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        check_plant("tomato")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    try:
        print("\nTesting WaterError...")
        check_water(0)
    except WaterError as err:
        print(f"Caught WaterError: {err}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        check_water(0)
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
