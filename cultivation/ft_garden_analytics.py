from typing import override

class Plant:
    class Stats:
        def __init__(self):
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0

        def display(self):
            print(f"Stats: {self._grow_call} grow, {self._age_call} age, {self._show_call} show")

    @staticmethod
    def age_check(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")
    
    @classmethod
    def anonymous(cls):
        return cls("Unknown plant",0.0, 0)

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, init = True)
        self.set_age(age, init = True)
        self._stats = Plant.Stats()

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
        self._stats._show_call += 1
        print(f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self._stats._grow_call += 1
    
    def age(self) -> None:
        self._stats._age_call += 1
    

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False
    
    @override
    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        self.state()

    def grow(self, grow_height: float) ->None:
        if grow_height == 0: return
        super().grow()
        self._height += grow_height
    
    def age(self, grow_age: int) -> None:
        if grow_age == 0: return
        super().age()
        self._age += grow_age 
    
    def state(self) -> None:
        if not self._bloomed:
            print(f"{self.name.capitalize()} has not bloomed yet")
        else:
            print(f"{self.name.capitalize()} is blooming beautifully!")

    def bloom(self, grow_height: float = 0.0, grow_age: int = 0) -> None:
        self._bloomed = True
        self.grow(grow_height)
        self.age(grow_age)
        self.show()

class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_call = 0
        
        def display(self):
            super().display()
            print(f"{self._shade_call} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._stats = Tree.Stats()
        self.trunk_diameter = trunk_diameter

    @override
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats._shade_call += 1
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

class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0
    
    @override
    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    @override
    def bloom(self, grow_height, grow_age):
        self.seeds = 42
        super().bloom(grow_height, grow_age)
        

def display_stats(plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()

def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.age_check(30)
    Plant.age_check(400)
    print("")

    rose = Flower("rose", 15, 10, "red")
    print(f"=== {rose.__class__.__name__}")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom(grow_height = 8)
    display_stats(rose)
    print("")

    oak = Tree("oak", 200.0, 365, 5.0)
    print(f"=== {oak.__class__.__name__}")
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")

    sunflower = Seed("sunflower", 80, 45, "yellow")
    print(f"=== {sunflower.__class__.__name__}")
    sunflower.show()
    print("make sunflower grow, age and bloom")
    sunflower.bloom(grow_height = 30, grow_age = 20)
    display_stats(sunflower)
    print("")

    anon = Plant.anonymous()
    print("=== Anonymous")
    anon.show()
    display_stats(anon)

if __name__ == "__main__":
    main()
