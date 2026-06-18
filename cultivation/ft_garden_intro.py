class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def plant_info(self):
        print(f"Plant: {self.name}",
              f"Height: {self.height}cm",
              f"Age: {self.age} days", sep = "\n")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    rose.plant_info()
    print("=== End of Program ===")
