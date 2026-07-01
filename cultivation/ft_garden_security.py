class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, init=True)
        self.set_age(age, init=True)

    def error_msg(self, error_arg: str, init: bool = False) -> None:
        print(f"{self.name}: Error, {error_arg} can't be negative")
        if not init:
            print(f"{error_arg.capitalize()} update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float, init: bool = False) -> bool:
        if height < 0:
            self.error_msg("height", init)
            return False
        self._height = float(height)
        if not init:
            print(f"Height updated: {height}cm")
        return True

    def set_age(self, age: int, init: bool = False) -> bool:
        if age < 0:
            self.error_msg("age", init)
            return False
        self._age = age
        if not init:
            print(f"Age updated: {age} days")
        return True

    def show(self) -> str:
        return (f"{self.name.capitalize()}: "
                f"{round(self.get_height(), 1)}cm, {self.get_age()} days old")


def main():
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}")
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-5)
    print("")
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()
