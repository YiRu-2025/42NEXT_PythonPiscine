class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.grow_rate = round(height / age, 1)

    def show(self) -> str:
        return (f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
                f"{self.age} days old")

    def grow(self) -> None:
        self.height += self.grow_rate

    def aging(self) -> None:
        self.age += 1


def main():
    print("=== Garden Plant Growth ===")
    rose = Plant("rose", 25.0, 30)
    init_height = rose.height
    rose.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.grow()
        rose.aging()
        print(rose.show())
    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")


if __name__ == "__main__":
    main()
