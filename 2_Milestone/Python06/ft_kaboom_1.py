if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION ")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    args: str = "bats, wind and fire"
    spell: str = "spell"
    print(f"({dark_spell_record(spell, args)})")
