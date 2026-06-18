class Plant:
    def __init__(self, name: str, height: float, ages: int, grow_rate: float):
        self.name = name
        self.height = height
        self.ages = ages
        self.grow_rate = grow_rate

    def show(self):
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, {self.ages} days old")

    def grow(self):
        self.height += self.grow_rate

    def age(self):
        self.ages += 1

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("rose", 25.0, 30, 0.8)
    init_height = rose.height
    rose.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")
