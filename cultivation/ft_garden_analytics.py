from typing import override
'''
Requirements:
• Create a class method that allows you to create an “anonymous” plant directly when you
do not yet have all the information. -> don't know how to do it?

• Each Plant has an internal system, implemented as a nested class, that holds statistical
data: number of grow() calls, number of age() calls, number of show() calls. Encapsu-
lation is required, as well as a display function.
• Trees need an extra piece of statistical data: number of produce_shade() calls.
• Finally, create a unique function, not part of any class, that displays statistics for any kind
of plant.
'''
class Plant:
    #  Create a static method for the Plant class that checks if a specific age given as a parameter is older than a year. -> finished, but how to call it? must use Plant.age_check(age = age)?
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

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant",0.0, 0)

    
# example for flower class:
'''
=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[statistics for Rose]
Stats: 0 grow, 0 age, 1 show
[asking the rose to grow and bloom]
Rose: 23.0cm, 10 days old
Color: red
Rose is blooming beautifully!
[statistics for Rose]
Stats: 1 grow, 0 age, 2 show
'''
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
'''
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
0 shade
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
1 shade
'''
class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_call = 0
        
        def display(self):
            super.display()
            print(f"{self._shade_call} shade")

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

'''
=== Seed
Sunflower: 80.0cm, 45 days old
Color: yellow
Sunflower has not bloomed yet
Seeds: 0
[make sunflower grow, age and bloom]
Sunflower: 110.0cm, 65 days old
Color: yellow
Sunflower is blooming beautifully!
Seeds: 42
[statistics for Sunflower]
Stats: 1 grow, 1 age, 2 show
'''
class Seed(Flower):
# • Create a Seed class that inherits from Flower, and holds the number of seeds once the
# flower has bloomed. The show() method must be improved accordingly.


def main():
    print("=== Garden statistics ===")
    Plant.age_check(10)
    Plant.age_check(400)

    rose = Flower("rose", 15, 10, "red")
    print(f"==={rose.__class__.__name__}")
    rose.show()
    rose.bloom()
    print("")

    oak = Tree("oak", 200.0, 365, 5.0)
    print(f"==={oak.__class__.__name__}")
    oak.show()
    oak.produce_shade()
    print("")

if __name__ == "__main__":
    main()
