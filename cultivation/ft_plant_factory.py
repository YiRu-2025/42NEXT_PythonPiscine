class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.grow_rate = round(height / age, 1)

    def show(self) -> str:
        return (f"{self.name.capitalize()}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.grow_rate

    def aging(self) -> None:
        self.age += 1


def main():
    rose = Plant("rose",25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    garden = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in garden:
        print(f"Created: {plant.show()}")

if __name__ == "__main__":
    main()
