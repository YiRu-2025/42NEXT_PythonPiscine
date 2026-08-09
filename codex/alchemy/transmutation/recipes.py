from alchemy.potions import strength_potion, create_fire
from ..elements import create_air

__all__ = ["lead_to_gold"]


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
        f"and '{strength_potion()}' mixed with '{create_fire()}'"
    )
