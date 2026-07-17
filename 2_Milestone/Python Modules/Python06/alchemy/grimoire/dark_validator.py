from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list[str] = dark_spell_allowed_ingredients()
    lst_ingredients: list[str] = ingredients.lower().split()
    for item in lst_ingredients:
        if item in valid_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
