from .light_validator import validate_ingredients

__all__ = ["light_spell_allowed_ingredients", "light_spell_record"]


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    verdict = result.rsplit(" - ", 1)[-1]
    if verdict == "VALID":
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
