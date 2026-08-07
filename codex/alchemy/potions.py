import elements
from alchemy.elements import create_earth, create_air

__all__ = [
    "create_fire",
    "create_water",
    "create_earth",
    "create_air",
    "healing_potion",
    "strength_potion",
]

create_fire = elements.create_fire
create_water = elements.create_water


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )