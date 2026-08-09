__all__ = ["validate_ingredients"]


def validate_ingredients(ingredients: str) -> str:
    # Deferred (local) import: breaks the circular dependency that would
    # otherwise occur if this were placed at module level, since
    # light_spellbook.py imports validate_ingredients from this module.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    if any(item in ingredients_lower for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
