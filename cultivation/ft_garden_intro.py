class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def plant_info(self) -> None:
        print(f"Plant: {self.name}",
              f"Height: {self.height}cm",
              f"Age: {self.age} days", sep="\n")


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    rose.plant_info()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
