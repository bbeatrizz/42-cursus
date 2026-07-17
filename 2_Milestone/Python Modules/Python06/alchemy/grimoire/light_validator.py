from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list[str] = light_spell_allowed_ingredients()
    lst_ingredients: list[str] = ingredients.lower().split()
    for item in lst_ingredients:
        if item in valid_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
