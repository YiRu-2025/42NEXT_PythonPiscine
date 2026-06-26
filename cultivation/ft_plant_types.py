from typing import override

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, init = True)
        self.set_age(age, init = True)

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
    
    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.state = False
    
    @override
    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        
    def bloom(self) -> None:
        if not self.state:
            print(f"{self.name.capitalize()} has not bloomed yet")
        self.state = True
        print(f"[asking the {self.name} to bloom]")
        self.show()
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    @override
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} "
              "now produces a shade of "
              f"{self._height}cm long and "
              f"{self.trunk_diameter}cm wide.")        

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    @override
    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self, days: int, grow_rate: float = 2.1) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self._height += days * grow_rate
        self._age += days
        self.nutritional_value += days
        self.show()

def main():
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5, 10, "April")
    print(f"==={rose.__class__.__name__}")
    rose.show()
    rose.bloom()
    print("")
    print(f"==={oak.__class__.__name__}")
    oak.show()
    oak.produce_shade()
    print("")
    print(f"==={tomato.__class__.__name__}")
    tomato.show()
    tomato.grow(days = 20, grow_rate = 2.1)
    
if __name__ == "__main__":
    main()
